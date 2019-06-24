#!/usr/bin/env python3


import subprocess
import sys
import re


# get lines from the definition file, strip empty line and comments
filename = sys.argv[1]
with open(filename, "r") as f:
    lines = [ re.sub(r' +', ' ', x.strip()).strip().split(" ") for x in f.read().split("\n") if len(x.strip()) > 0 and x.strip()[0] != '#' ]

conf_repo = None
conf_additive = None
conf_worker = None
conf_target = None
conf_compression = None

target_vm = "vgw"
if len(sys.argv) >= 3:
    target_vm = sys.argv[2]

# config pass


for line in lines:
    if line[0] == "vgw":
        print("vgw")
    if line[0] == "worker":
        conf_worker = line[1]
    if line[0] == "compression":
        conf_compression = line[1]
    if line[0] == "repo":
        conf_repo = line[1]
    if line[0] == "additive":
        conf_additive = line[1]
    if line[0] == "target":
        conf_target = line[1]



worker_tmpdir = subprocess.check_output("ssh %s mktemp -d -p /tmp additive-XXXXXXXXXXXX" % conf_worker, universal_newlines=True, shell=True).split("\n")[0].strip()

subprocess.check_output("ssh %s mkdir -p %s/%s" % (conf_worker, worker_tmpdir, conf_additive), universal_newlines=True, shell=True).split("\n")[0].strip()


print("Worker: %s" % worker_tmpdir)


for line in lines:
    if line[0] == target_vm:
        localfile = line[1]
        remotefile = line[2]
        s_owner = line[3]
        s_permissions = line[4]
        cmd = "ssh %s mkdir -p %s/%s/%s" % (conf_worker, worker_tmpdir, conf_additive, "/".join(remotefile.split("/")[:-1]))
        print(cmd)
        subprocess.check_output(cmd, universal_newlines=True, shell=True)
        
        # copy localfile

        if localfile.find("::") == 0:
            # files outside the repo will have a "::" in the defenition
            cmd = "scp %s %s:%s/%s/%s" % (localfile.replace("::", ""), conf_worker, worker_tmpdir, conf_additive, remotefile)
        else:
            cmd = "scp %s/%s %s:%s/%s/%s" % (conf_repo, localfile, conf_worker, worker_tmpdir, conf_additive, remotefile)
            
        print(cmd)
        subprocess.check_output(cmd, universal_newlines=True, shell=True)
        
        cmd = "ssh %s chown %s %s/%s/%s" % (conf_worker, s_owner, worker_tmpdir, conf_additive, remotefile)
        print(cmd)
        subprocess.check_output(cmd, universal_newlines=True, shell=True)
        cmd = "ssh %s chmod %s %s/%s/%s" % (conf_worker, s_permissions, worker_tmpdir, conf_additive, remotefile)
        print(cmd)
        subprocess.check_output(cmd, universal_newlines=True, shell=True)

cmd = "ssh %s 'cd %s/%s; tar cfJ ../%s.tar.xz *'" % (conf_worker, worker_tmpdir, conf_additive, conf_additive)
subprocess.check_output(cmd, universal_newlines=True, shell=True)

cmd = "scp %s:%s/%s.tar.xz /tmp" % (conf_worker, worker_tmpdir, conf_additive)
subprocess.check_output(cmd, universal_newlines=True, shell=True)



if target_vm == "vadm":
    print("vadm installation")

    cmd = "ssh %s ssh vadm 'mount /dev/sda1 /mnt'" % (conf_target)
    subprocess.check_output(cmd, universal_newlines=True, shell=True)

    cmd = "scp /tmp/%s.tar.xz %s:/tmp" % (conf_additive, conf_target)
    subprocess.check_output(cmd, universal_newlines=True, shell=True)

    cmd = "ssh %s scp /tmp/%s.tar.xz vadm:/mnt" % (conf_target, conf_additive)
    subprocess.check_output(cmd, universal_newlines=True, shell=True)


    cmd = "ssh %s scp vadm:/mnt/boot/grub/grub.cfg /tmp" % (conf_target)
    subprocess.check_output(cmd, universal_newlines=True, shell=True)

    cmd = "ssh %s cat /tmp/grub.cfg" % (conf_target)
    grub = subprocess.check_output(cmd, universal_newlines=True, shell=True)

    print("grub-1:%s" % grub)
    additive_option = "additive=%s.tar.xz" % conf_additive
    additive_filename = "%s.tar.xz" % conf_additive
    if grub.find(additive_filename) < 0:
        print("Grub is missing the additive... adding... %s" % additive_option)
        if grub.find("additive=") < 0:
            # easy, no other additives
            grub = grub.replace(" osarch=", " %s osarch=" % additive_option)
        else:
            # add the additive to the already existing additive option
            old_additive = grub[grub.find("additive="):].split(" ")[0].split("=")[1]
            grub = grub.replace("additive=%s"%old_additive, "additive=%s,%s"%(old_additive,additive_filename))
    
    cmd = "ssh %s 'cat >/tmp/grub.cfg'" % (conf_target)
    p = subprocess.Popen(cmd, universal_newlines=True, shell=True, stdin=subprocess.PIPE)
    p.communicate(input=grub)

    cmd = "ssh %s scp /tmp/grub.cfg vadm:/mnt/boot/grub/grub.cfg" % (conf_target)
    subprocess.check_output(cmd, universal_newlines=True, shell=True)

    cmd = "ssh %s ssh vadm 'umount /mnt'" % (conf_target)
    subprocess.check_output(cmd, universal_newlines=True, shell=True)


if target_vm == "vgw":

    cmd = "ssh %s 'mount /dev/sda1 /mnt'" % (conf_target)
    subprocess.check_output(cmd, universal_newlines=True, shell=True)
    
    cmd = "scp /tmp/%s.tar.xz %s:/mnt/" % (conf_additive, conf_target)
    subprocess.check_output(cmd, universal_newlines=True, shell=True)
    
    cmd = "ssh %s 'cat /mnt/boot/grub/grub.cfg'" % (conf_target)
    grub = subprocess.check_output(cmd, universal_newlines=True, shell=True)
    additive_option = "additive=%s.tar.xz" % conf_additive
    additive_filename = "%s.tar.xz" % conf_additive
    if grub.find(additive_filename) < 0:
        print("Grub is missing the additive... adding... %s" % additive_option)
        if grub.find("additive=") < 0:
            # easy, no other additives
            grub = grub.replace(" osarch=", " %s osarch=" % additive_option)
        else:
            # add the additive to the already existing additive option
            old_additive = grub[grub.find("additive="):].split(" ")[0].split("=")[1]
            grub = grub.replace("additive=%s"%old_additive, "additive=%s,%s"%(old_additive,additive_filename))
    
    cmd = "ssh %s 'cat >/mnt/boot/grub/grub.cfg'" % (conf_target)
    p = subprocess.Popen(cmd, universal_newlines=True, shell=True, stdin=subprocess.PIPE)
    p.communicate(input=grub)
    
    cmd = "ssh %s 'umount /mnt'" % (conf_target)
    subprocess.check_output(cmd, universal_newlines=True, shell=True)

    cmd = "ssh %s 'reboot'" % (conf_target)
    subprocess.check_output(cmd, universal_newlines=True, shell=True)
    