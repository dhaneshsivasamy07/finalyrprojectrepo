#!/bin/bash

RED="\e[31m"
GREEN="\e[32m"
NC="\e[0m"

echo -e "${RED}Updating Contents${NC}"
rm /home/dnoscp/Desktop/LinuxSecurityFramework/sh_files/NOCOLORS.log 2>/dev/null
/home/dnoscp/Desktop/LinuxSecurityFramework/sh_files/LinuxSecurityFramework.sh -N 2>/dev/null | tee /home/dnoscp/Desktop/LinuxSecurityFramework/sh_files/NOCOLORS.log
sudo rm /home/dnoscp/Desktop/LinuxSecurityFramework/web/iptables.txt 2>/dev/null
sudo iptables -L | sudo tee /home/dnoscp/Desktop/LinuxSecurityFramework/web/iptables.txt
echo DNOSCP

/usr/bin/python3 /home/dnoscp/Desktop/LinuxSecurityFramework/web/index.py & 
/home/dnoscp/Desktop/LinuxSecurityFramework/sh_files/gotty top &
/home/dnoscp/Desktop/LinuxSecurityFramework/sh_files/gotty -p 1234 btop --utf-force

