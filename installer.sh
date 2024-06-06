#!/bin/bash

# Author : B1B3K S4H
# Copyright ©2020
# Script follows here:
clear
cd $HOME
sleep 2.0
echo -e "\x1b[92m
 ________   ______     ________  _________  ______    ________   ______   ________       
/_______/\ /_____/\   /_______/\/________/\/_____/\  /_______/\ /_____/\ /_______/\      
\::: _  \ \\:::_ \ \  \__.::._\/\__.::.__\/\:::_ \ \ \::: _  \ \\::::_\/_\::: _  \ \     
 \::(_)  \ \\:(_) ) )_   \::\ \    \::\ \   \:(_) ) )_\::(_)  \ \\:\/___/\\::(_)  \ \    
  \:: __  \ \\: __ `\ \  _\::\ \__  \::\ \   \: __ `\ \\:: __  \ \\_::._\:\\:: __  \ \   
   \:.\ \  \ \\ \ `\ \ \/__\::\__/\  \::\ \   \ \ `\ \ \\:.\ \  \ \ /____\:\\:.\ \  \ \  
    \__\/\__\/ \_\/ \_\/\________\/   \__\/    \_\/ \_\/ \__\/\__\/ \_____\/ \__\/\__\/  
                                                                                       
                                                                                                                                                                                                                                                                     "

termux-setup-storage
sleep 7.0
rm -rf phoneinfoga.sh > /dev/null 2>&1
echo -e '\033[1;91m[''\033[0m*''\033[1;91m]''\033[1;91m It will install AZ-Unlimitedx'
echo
sleep 2.0
echo
sleep 2.0
echo -e '\033[1;92m[''\033[0m*''\033[1;92m]''\033[1;92m Please wait...'
sleep 2.0
echo
echo -e '\033[1;92m[''\033[0m*''\033[1;92m]''\033[1;92m Updating...'
echo
apt --assume-yes update > /dev/null 2>&1 && apt --assume-yes upgrade -y > /dev/null 2>&1
echo -e '\033[1;92m[''\033[0m*''\033[1;92m]''\033[1;92m Required Packages Installing...'
echo
command -v git > /dev/null 2>&1 || { echo -e >&2 "\033[1;91mI require git but it's not installed, Now Installing.\e[1;92m"; pkg install git -y; echo; }
command -v python > /dev/null 2>&1 || { echo -e >&2 "\033[1;91mI require python but it's not installed, Now Installing.\e[1;92m"; pkg install python -y; echo; }
command -v python2 > /dev/null 2>&1 || { echo -e >&2 "\033[1;91mI require python2 but it's not installed, Now Installing.\e[1;92m"; pkg install python2 -y; echo; }

sleep 2.0
echo -e '\033[1;92m[''\033[0m*''\033[1;92m]''\033[1;92m Required Packages Installed.'
rm -rf PhoneInfoga > /dev/null 2>&1
rm -rf phoneinfoga > /dev/null 2>&1
echo
sleep 2.0
echo -e '\033[1;92m[''\033[0m*''\033[1;92m]''\033[1;92m PhoneInfoga Installing...'
git clone https://github.com/aritrasa45/AZ-Unlimitedx > /dev/null 2>&1 && cd AZ-Unlimitedx > /dev/null 2>&1 && unzip Packs > /dev/null 2>&1 && python3 -m pip install -r requirements.txt > /dev/null 2>&1 && pip2 install colorama > /dev/null 2>&1
rm -rf packs.zip > /dev/null 2>&1
rm -rf installer.sh > /dev/null 2>&1
chmod +x *
sleep 2.0
echo
echo -e '\033[1;92m[''\033[0m*''\033[1;92m]''\033[1;92m AZ-Unlimitedx Successfully Installed.'
sleep 2.0
echo
printf $'\n\e[1;94m[\e[0m\e[1;77m*\e[0m\e[1;94m] Press Enter To Exit: \e[0m'
read a1
clear
sleep 2.0