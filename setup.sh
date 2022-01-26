#!/bin/bash
port=/dev/cu.usbserial-0001

echo "Hold and release the boot button foreach step
"
# change boot config
echo -ne "Removing boot.py"
sh ./loading.sh ampy --port /dev/cu.usbserial-0001 rm boot.py &> /dev/null

echo -ne "Loading boot.py"
sh ./loading.sh ampy --port /dev/cu.usbserial-0001 put boot.py &> /dev/null

# load script
echo -ne "Removing scripts"
sh ./loading.sh ampy --port /dev/cu.usbserial-0001 rmdir src &> /dev/null

echo -ne "Loading scripts"
sh ./loading.sh ampy --port /dev/cu.usbserial-0001 put src &> /dev/null