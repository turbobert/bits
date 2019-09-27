#!/bin/bash


set -x

F="$1"

#mount /dev/sda1 /mnt
realfile=$(readlink /mnt/OS.tar.xz)
echo "Will update the following OS archive: ($realfile)"
echo "With file ($F)"

echo "Searching if this file exists in the OSARCH..."
tar tfJ /mnt/$realfile | grep "^$F$"
EC=$?
echo $EC


D=$(mktemp -d -p /tmp os-XXXXXXX)

echo "Extracting..."
( cd $D && tar xfJ /mnt/$realfile )
( cd $D && rm -f $F )
( cd $D && cp -a /$F $F )
#TODO: mkdir -p if necessary for new folders

echo "Repacking..."

rm -f /mnt/$realfile

( cd $D && tar cfJ /mnt/realfile * )

#rm -fr $D

# umount /mnt

