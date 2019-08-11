#!/bin/bash
#/////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////
#////                                                                                     ////
#////  _   _           _      _____                              _   _                    ////
#//// | \ | |         | |    / ____|                            | | (_)                   ////
#//// |  \| |   ___   | |_  | |  __   _   _    __ _   _ __    __| |  _    __ _   _ __     ////
#//// | . ` |  / _ \  | __| | | |_ | | | | |  / _` | | '__|  / _` | | |  / _` | | '_ \    ////                        
#//// | |\  | | (_) | | |_  | |__| | | |_| | | (_| | | |    | (_| | | | | (_| | | | | |   ////
#//// |_| \_|  \___/   \__|  \_____|  \__,_|  \__,_| |_|     \__,_| |_|  \__,_| |_| |_|   ////
#////                                                                                     ////
#/////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////

g="\033[32m"
b="\033[1;34m"
c="\033[1;36m"
r="\033[1;31m"
y="\033[1;93m"
h="\033[0;30m"
clear
echo $y "::::::::::     :::      ::::::::  :::::::::: :::::::::  :::::::::  :::    ::: ::::::::::: ::::::::::
:+:          :+: :+:   :+:    :+: :+:        :+:    :+: :+:    :+: :+:    :+:     :+:     :+:
+:+         +:+   +:+  +:+        +:+        +:+    +:+ +:+    +:+ +:+    +:+     +:+     +:+
:#::+::#   +#++:++#++: +#+        +#++:++#   +#++:++#+  +#++:++#:  +#+    +:+     +#+     +#++:++#
+#+        +#+     +#+ +#+        +#+        +#+    +#+ +#+    +#+ +#+    +#+     +#+     +#+
#+#        #+#     #+# #+#    #+# #+#        #+#    #+# #+#    #+# #+#    #+#     #+#     #+#
###        ###     ###  ########  ########## #########  ###    ###  ########      ###     ########## v1.0

╔═════════════════════════════════════════════════╗
║Tools     : ₣aceBruteV1.0               
║Author    : NotGuardian
║Github    : https://github.com/NotHax
║Instagram : https://instagram.com/notguardianyt
║Jika Ada Bug Tinggal DM Author Aja Ya
╚═════════════════════════════════════════════════╝"
echo $c " [$y 01 $c] $g Mulai Cracking "
echo $c " [$y 02 $c] $g Buat WorldList "
echo $c " [$y 00 $c] $r Keluar"
echo $y "Pilih 1/2/3?"
read -p "" pil;

case $pil in
01)echo $y "Memilih Nomor 01"
sleep 1
python2 FaceBrute.py

;;

1)clear
 echo "Memilih Nomor 1"
sleep 1
python2 FaceBrute.py

;;

02) clear
echo "Memilih Nomor 02"
sleep 1
echo "Tips Buat WorldList Adalah Tempat Password Target"
sleep 2
nano WorldList
echo $y "WorldList Tersimpan"
sleep 1
sh FaceBruteMenu.sh

;;

2)  clear
echo "Memilih Nomor 2"
sleep 1
echo "Tips Buat WorldList Adalah Tempat Password Target"
sleep 2
nano WorldList
echo $y "WorldList Tersimpan"
sleep 1
sh FaceBruteMenu.sh

;;

00)echo "Memilih Nomor 00"
echo $y"Sampai Jumpa Lagi"
exit

;;

0)echo $y "Memilih Nomor 0"
echo $y "Sampai Jumpa Lagi"
exit

*) echo $y "Maaf encarian Anda Tidak Ditemukan"
sleep 2.1
esac
done
done
