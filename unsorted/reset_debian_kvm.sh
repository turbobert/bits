#!/bin/bash



NAME="$1"
IP="$2"
H="$3"
DISKORIG="$4"
DISKCURRENT="$5"
ESTIMATED="$6"

if [ ! "$7" = "-f" ]; then
    echo "Press ENTER to reswt Execution Host 1 - or CTRL-C to abort"
    read
fi

steps=12
step=1

say() {
    echo "[$(date -u)] ($step/$steps) $1"
    (( step = step + 1 ))
}

ttl=$ESTIMATED
ttl_=$(date -u +%s)

ttlstring() {
    ttl__=$(date -u +%s)
    elaps=$(( ttl__ - ttl_ ))
    remain=$(( ttl - elaps ))
    echo "approx. $remain second(s) remaining"
}

say "Destroying VM... (all in all will be about 2m30s)"
ssh $H "virsh destroy $NAME" 1>/dev/null 2>/dev/null
say "Done"

sleep 2

say "Checking if machine is really off... $(ttlstring)"
off=$(ssh wb "virsh list --all | grep 'shut off' | awk -F ' ' '{print \$2}' | grep ^$NAME$ | wc -l" 2>/dev/null)
say "Done (off=$off)"

if [ ! "$off" = "1" ]; then
    say "error - could not switch off virtual machine"
    exit 1
fi

say "Restoring VM harddisk... $(ttlstring)"
ssh $H "cat $DISKORIG >$DISKCURRENT" 1>/dev/null 2>/dev/null
say "Done"

say "Starting VM... $(ttlstring)"
ssh $H "virsh start $NAME" 1>/dev/null 2>/dev/null
say "Done, will wait for system to come up"


say "Will wait until system ping returns $(ttlstring)"
while true; do
    ping -n -c 1 -W 2 $IP 1>/dev/null 2>/dev/null
    C=$?
    if [ "$C" = "0" ]; then
	say "OK, system is up"
	break
    else
	sleep 5
    fi
done

sleep 5

say "Checking SSH connectivity... $(ttlstring)"
X=$(ssh $NAME uname 2>/dev/null)

if [ "$X" = "Linux" ]; then
    say "SSH is up"
else
    say "ERROR: Unable to connect via SSH"
fi
