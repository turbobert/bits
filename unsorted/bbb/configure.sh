#!/bin/bash

# for SSH Access
HOST=bbb1
OF=system-setup-now.sh


echo "#!/bin/bash" >$OF
echo "" >>$OF

UDCNAME=$(ssh $HOST ls /sys/class/udc 2>/dev/null)

echo "UDC=$UDCNAME" >>$OF
echo "VENDOR='TURBOBERT HARDWARE'" >>$OF
echo "SERIAL='12341234'" >>$OF
#echo "IDPRODUCT='0xa4ac'" >>$OF
#echo "IDVENDOR='0x0525'" >>$OF
echo "IDPRODUCT='0x0250'" >>$OF
echo "IDVENDOR='0x05ac'" >>$OF
echo "PRODUCT='Keyboard Emulation'" >>$OF
echo "CONFIG_NAME='Conf1'" >>$OF
echo "MAX_POWER_MA=120" >>$OF
echo "PROTOCOL=1" >>$OF
echo "SUBCLASS=1" >>$OF
echo "REPORT_LENGTH=8" >>$OF
echo "DESCRIPTOR='/config/usb_gadget/keyboardgadget/functions/hid.usb0/report_desc'" >>$OF
echo "" >>$OF
echo "modprobe libcomposite" >>$OF
echo "mkdir /config" >>$OF
echo "mount none /config -t configfs" >>$OF
echo "mkdir -p /config/usb_gadget/keyboardgadget" >>$OF
echo "mkdir -p /config/usb_gadget/keyboardgadget/configs/c.1" >>$OF
echo "mkdir -p /config/usb_gadget/keyboardgadget/functions/hid.usb0" >>$OF
echo "echo \$PROTOCOL > /config/usb_gadget/keyboardgadget/functions/hid.usb0/protocol" >>$OF
echo "echo \$SUBCLASS > /config/usb_gadget/keyboardgadget/functions/hid.usb0/subclass" >>$OF
echo "echo \$REPORT_LENGTH > /config/usb_gadget/keyboardgadget/functions/hid.usb0/report_length" >>$OF
cat >>$OF <<EOF
echo -ne '\x05\x01\x09\x06\xa1\x01\x05\x07\x19\xe0\x29\xe7\x15\x00\x25\x01\x75\x01\x95\x08\x81\x02\x95\x01\x75\x08\x81\x01\x05\x08\x19\x01\x29\x05\x95\x05\x75\x01\x91\x02\x95\x01\x75\x03\x91\x01\x05\x07\x19\x00\x2a\xff\x00\x95\x05\x75\x08\x15\x00\x26\xff\x00\x81\x00\x05\xff\x09\x03\x75\x08\x95\x01\x81\x02\xc0' >\$DESCRIPTOR
EOF
echo "mkdir -p /config/usb_gadget/keyboardgadget/strings/0x409" >>$OF
echo "mkdir -p /config/usb_gadget/keyboardgadget/configs/c.1/strings/0x409" >>$OF
echo "echo \$IDPRODUCT > /config/usb_gadget/keyboardgadget/idProduct" >>$OF
echo "echo \$IDVENDOR > /config/usb_gadget/keyboardgadget/idVendor" >>$OF
echo 'echo "$SERIAL" > /config/usb_gadget/keyboardgadget/strings/0x409/serialnumber' >>$OF
echo 'echo "$VENDOR" > /config/usb_gadget/keyboardgadget/strings/0x409/manufacturer' >>$OF
echo 'echo "$PRODUCT" > /config/usb_gadget/keyboardgadget/strings/0x409/product' >>$OF
echo 'echo "$CONFIG_NAME" > /config/usb_gadget/keyboardgadget/configs/c.1/strings/0x409/configuration' >>$OF
echo 'echo "$MAX_POWER_MA" > /config/usb_gadget/keyboardgadget/configs/c.1/MaxPower' >>$OF
echo "( cd /config/usb_gadget/keyboardgadget && ln -s functions/hid.usb0 configs/c.1 )" >>$OF

echo 'echo "$UDC" >/config/usb_gadget/keyboardgadget/UDC' >>$OF
