#!/bin/bash

clear

echo -e "
+---------------------------+
|         Packages          |
+---------------------------+
| Visual Studio Code        |
| Discord                   |
| Git Kraken (Git UI)       |
| Vim (Editor)              |
| Guake (Fast Terminal F12) |
| -                         |
| Virtualbox Guest          |
| Build Essential           |
| Manpages Dev              |
| CCMake                    |
| CMake                     |
| G++                       |
| -                         |
| Git Lens                  |
| MS C++                    |
| Prettier                  |
| Cmake Tools               |
+---------------------------+
"

REQUIRED_PKG="whiptail"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
echo Checking for $REQUIRED_PKG: $PKG_OK
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get --yes install $REQUIRED_PKG
fi

# shellcheck disable=SC1073
if (whiptail --title "Dialog" --yesno "Ro Workspace Installer | This script will install core pkgs for a better workflow and update pkgs. This pkg includes rust, ..., and other quality of life extensions." 10 100 --defaultno" 8 78); then
  CHOICE=$(whiptail --menu "Options" 18 100 10 \
      "Install Rust." \
      "Update" "Update all packages." \
      "something else" 3>&1 1>&2 2>&3)

      if [ -z "$CHOICE" ]; then
          echo "No option was chosen \(user hit Cancel\)"
          else
              echo "The user chose $CHOICE"
              if [[ "$CHOICE" == *"Install Tools"* ]]; then
                  read -r -p "Are you sure you want to continue? [Y/N] "
      elif [[ "$CHOICE" == *"Update"* ]]; then
            sudo apt update
            sudo snap refresh
      fi
else
  echo "Exit"
fi