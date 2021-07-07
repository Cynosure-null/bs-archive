#! /bin/bash

RED='\033[0;31m'
NC='\033[0m' # No Color
GREEN='\033[0;32m'

chmod +x ./fossil.sh

if [[ $1 == -l ]]; then
    #make install file
    echo "#! usr/bin/bash" > fossil.sh || printf "${RED} FATAL ERROR. OPERATION ABORTED. \n Error created while making line one of the install file \n"; exit
    echo "python3.8 ~/.local/bin/fossil/main.py" >> fossil.sh || printf "${RED} FATAL ERROR. OPERATION ABORTED. \n Error created while making line two of the install file \n"; exit
    #copy files
    mv ./fossil ~/.local/bin/ || printf "${RED} FATAL ERROR. OPERATION ABORTED. \n"; exit
    mv ./fossil.sh ~/.local/bin/ || printf "${RED} FATAL ERROR. OPERATION ABORTED. \n"; exit
    printf "${GREEN} Fossil installed to ./local/bin."

elif [[ $1 == -g ]]; then
    echo "#! usr/bin/bash" > fossil.sh || printf "${RED} FATAL ERROR. OPERATION ABORTED. \n Error created while making line one of the install file \n"; exit
    echo "python3.8 /usr/bin/fossil/main.py" >> fossil.sh || printf "${RED} FATAL ERROR. OPERATION ABORTED. \n Error created while making line two of the install file \n"; exit
    mv ./fossil /usr/bin/ || printf "${RED} FATAL ERROR. OPERATION ABORTED. Are you root? \n"; exit
    mv ./fossil.sh /usr/bin/ || printf "${RED} FATAL ERROR. OPERATION ABORTED. Are you root? \n"; exit
    printf "${GREEN} Fossil installed to /usr/bin/fossil."

elif [[ $1 == -c ]]; then
    echo "#! usr/bin/bash" > fossil.sh || printf "${RED} FATAL ERROR. OPERATION ABORTED. \n Error occurred while making line one of the install file \n"; exit
    echo "python3.8 ${2}/fossil/main.py" >> fossil.sh || printf "${RED} FATAL ERROR. OPERATION ABORTED. \n Error created while making line two of the install file \n";exit 
    mv ./fossil ${2} || printf "${RED} FATAL ERROR. OPERATION ABORTED. \n"; exit
    mv ./fossil ${2} || printf "${RED} FATAL ERROR. OPERATION ABORTED. \n"; exit
    printf "${GREEN} fossil installed to $2 "

else
    printf "${RED} No path supported. Aborting. \n"; exit
fi
echo "done"
exit


