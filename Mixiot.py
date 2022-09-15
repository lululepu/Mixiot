import os
import json
import time
import socket
import tempfile
import subprocess
temp=tempfile.gettempdir()
cwd=os.getcwd()
try:
    E=subprocess.getstatus("py")
    py=1
    os.system("cls")
except:
    py=0
    os.system("cls")
try:
    from pytube import *
except:
    if py==1:
        os.system("python -m pip install pytube")
    else:
        os.system("py -m pip install pytube")
try:
    from pystyle import *
except:
    if py==1:
        os.system("python -m pip install pystyle")
    else:
        os.system("py -m pip install pystyle")
try:
    from pytube.cli import *
except:
    if py==1:
        os.system("python -m pip install pytube.cli")
    else:
        os.system("py -m pip install pytube.cli")
try:
    import requests
except:
    if py==1:
        os.system("python -m pip install requests")
    else:
        os.system("py -m pip install requests")
try:
    from pythonping import ping
except:
    if py==1:
        os.system("python -m pip install pythonping")
    else:
        os.system("py -m pip install pythonping")
try:
    from termcolor import * 
except:
    if py==1:
        os.system("python -m pip install termcolor")
    else:
        os.system("py -m pip install termcolor")
from pytube import *
from pystyle import *
from pytube.cli import *
import requests
from pythonping import ping
from termcolor import *
try:
    def clear():
        os.system("cls")
    path = os.path.dirname(os.path.abspath(__file__))
    username = os.getenv('USERNAME')

    __liscense__="Created by lululepu#3412"

    banner = r"""
            .-~~``~~-,
          (          \
       .--'`-.__,     \
      /      |\O/      |
     |,      /         |
     \   ,--`\         |
      `.(   /          \
           /            \
          / .  ;    :.   \
         /__;   \   | \   \
         /   '. |\_ /-.'-._\
        |      `   `        \
        |    /               \
        |    |                |
        |    |                \
        \    \                 |
         \    |  |   |   \     \
          \   \  \   \    \     |
           '.  \  \  ' \   \     \
             \  \  `\   `\  `\    \
              |  `\  `\   `.  '.   \
               \   `-. '._  '-. '._/\
                |     \-._;-._ '-._  \
                \      `\     `--` `--\
                 ;_      `-.           |
    ~==~=~~=~=~=~,-.-.-'`;'=~=-.,_   __/=~=~=~~=
      =_ = -_ -( ( ( .-`( ( ( .-``"`-_ = - _ -
    - -   =   - ` ` ` _= ` ` `   =  -  -    =
    ~~==~=~~==~=~~=~~=~=~==~~=~~==~~=~~=~~~===~~
                             \ . \  . '|
                              \   . .' /
                               '.   \.'|
                                 '-.__/"""[1:]

    def ascii():
        System.Title("Mixiot")
        System.Size(90, 50)
        Anime.Fade(Center.Center(banner), Colors.yellow_to_red, Colorate.Vertical, interval=0.01, enter=True)
    ascii()

    def pscan():
        try:
            System.Title("IP port scanner")
            fport=[]
            System.Size(140, 35)
            clear()
            text=("""
     ______     ____   _______    _________      _______   ______      __      ____  _____ ____  _____ _________ _______    
    |_   __ \ .'    \.|_   __ \  |  _   _  |    /  ___  |./ ___  |    /  \    |_   \|_   _|_   \|_   _|_   ___  |_   __ \   
      | |__) |  .--.  \ | |__) | |_/ | | \_|   |  (__ \_| ./   \_|   / /\ \     |   \ | |   |   \ | |   | |_  \_| | |__) |  
      |  ___/| |    | | |  __ /      | |        '.___\-.| |         / ____ \    | |\ \| |   | |\ \| |   |  _|  _  |  __ /   
     _| |_   \  \--'  /_| |  \ \_   _| |_      |\\____) | \.___.'\_/ /    \ \_ _| |_\   |_ _| |_\   |_ _| |___/ |_| |  \ \_ 
    |_____|   \.____.'|____| |___| |_____|     |_______.'\._____.'____|  |____|_____|\____|_____|\____|_________|____| |___|""")
            print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
            target = input("\nIP/Domain: ")
            try:
                ping(target)
            except(KeyboardInterrupt):
                clear()
                print(colored("Stopped", "green"))
                time.sleep(2)
                main()
            except:
                input(colored("Bad ip!", "red"))
                pscan()
            if target == "back":
                ip_service()
            pstart = input("Starting port(blank for 0): ")
            if pstart == "":
                pstart=int(float(1))
            else:
                pstart=int(pstart)
            pstart=pstart-1
            pmax = int(input("Max port to scan: "))
            if pmax == "back":
                main()
            print("-" * 40)
            print("Scanning Target: " + target)
            print("The start can be long")
            print("-" * 40)
            x=pstart
            opened=False
            while x < pmax:
                x=x+1
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.1)
                result=s.connect_ex((target,x))
                if result == 0:
                    print(colored("Port {} is open".format(x), "green"))
                    fport.append("{}".format(x))
                    opened=True
                else:
                    print(colored("Port {} is closed".format(x), "red"))
                s.close()
            if opened==True:
                print(colored('Open port: '+', '.join(fport), 'green'))
            else:
                print(colored('No port open', 'red'))
            input()
            main()
        except(KeyboardInterrupt):
            clear()
            main()


    def tracker():
        System.Title("IP tracker")
        System.Size(120, 35)
        clear()
        text=("""
     _____ ______       _________ _______         __        ______ ___  ____  _________ _______    
    |_   _|_   __ \    |  _   _  |_   __ \       /  \     ./ ___  |_  ||_  _||_   ___  |_   __ \   
      | |   | |__) |   |_/ | | \_| | |__) |     / /\ \   / ./   \_| | |_/ /    | |_  \_| | |__) |  
      | |   |  ___/        | |     |  __ /     / ____ \  | |        |  __'.    |  _|  _  |  __ /   
     _| |_ _| |_          _| |_   _| |  \ \_ _/ /    \ \_\ \.___.'\_| |  \ \_ _| |___/ |_| |  \ \_ 
    |_____|_____|        |_____| |____| |___|____|  |____|\._____.'____||____|_________|____| |___|""")
        print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
        IP = input("\n\nIP: ")
        if IP == "back":
            ip_service()
        r=requests.get("http://ip-api.com/json/"+IP).text
        y = json.loads(r)
        if y["status"] != "success":
            input(colored("Bad ip!", "red"))
            tracker()
        print("\nCity: "+y["city"])
        print("Operator: "+y["as"])
        print("Country: "+y["country"])
        input()
        main()

    def pinger():
        System.Title("IP pinger")
        try:
            System.Size(120, 35)
            clear()
            text=("""
         _____ ______       ______   _____ ____  _____   ______   _________ _______    
        |_   _|_   __ \    |_   __ \|_   _|_   \|_   _|.' ___  | |_   ___  |_   __ \   
          | |   | |__) |     | |__) | | |   |   \ | | / .'   \_|   | |_  \_| | |__) |  
          | |   |  ___/      |  ___/  | |   | |\ \| | | |    ____  |  _|  _  |  __ /   
         _| |_ _| |_        _| |_    _| |_ _| |_\   |_\ \.___]  _|_| |___/ |_| |  \ \_ 
        |_____|_____|      |_____|  |_____|_____|\____|\._____.' |_________|____| |___|""")
            print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
            IP = input("\n\nIP: ")
            if IP == "back":
                ip_service()
            try:
                ping(IP, verbose=True, timeout=0.1, count=float("inf"), size=1)
            except(KeyboardInterrupt):
                clear()
                print(colored("Stopped", "green"))
                main()
            except:
                input(colored("Bad ip!", "red"))
                pinger()
            input()
            main()
        except(KeyboardInterrupt):
            main()
    def python_obf():
        try:
            System.Title("Python obfuscator")
            System.Size(180, 35)
            os.system("mkdir "+cwd+"\\Obfuscated >nul 2>&1")
            clear()
            text=("""
     _______  ____  ____  _________  ____  ____   ___   ____  _____        ___   ______   ________  _____  _____   ______     ______       _     _________    ___   _______     
    |_   __ \|_  _||_  _||  _   _  ||_   ||   _|.'   `.|_   \|_   _|     .'   `.|_   _ \ |_   __  ||_   _||_   _|.' ____ \  .' ___  |     / \   |  _   _  | .'   `.|_   __ \    
      | |__) | \ \  / /  |_/ | | \_|  | |__| | /  .-.  \ |   \ | |      /  .-.  \ | |_) |  | |_ \_|  | |    | |  | (___ \_|/ .'   \_|    / _ \  |_/ | | \_|/  .-.  \ | |__) |   
      |  ___/   \ \/ /       | |      |  __  | | |   | | | |\ \| |      | |   | | |  __'.  |  _|     | '    ' |   _.____`. | |          / ___ \     | |    | |   | | |  __ /    
     _| |_      _|  |_      _| |_    _| |  | |_\  `-'  /_| |_\   |_     \  `-'  /_| |__) |_| |_       \ \__/ /   | \____) |\ `.___.'\ _/ /   \ \_  _| |_   \  `-'  /_| |  \ \_  
    |_____|    |______|    |_____|  |____||____|`.___.'|_____|\____|     `.___.'|_______/|_____|       `.__.'     \______.' `.____ .'|____| |____||_____|   `.___.'|____| |___| 
            """)
            print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
            fpath=input("Drag the file to obfuscate here: ")
            with open(temp+"\\tempobf.bat", 'w') as f:
                f.write(r"""
@echo off
color 0A & Mode 90,4
python -OO -m py_compile %~1
cd "%~1\..\__pycache__"
rename *.pyc obfuscated_%~nx1
move *.py """+cwd+r"""\Obfuscated >nul
cd ../
rmdir __pycache__
echo(
echo         Please wait a while ... Encoding %~nx1 is in progress ...
cls
echo(
echo   Obfuscated file path: """+cwd+r"""\Obfuscated\obfuscated_%~nx1
echo                           Finished press enter to continue

                """)
                f.close()
            os.system(temp+"\\tempobf.bat "+fpath+"")
            input()
            main()
        except(KeyboardInterrupt):
            clear()
            main()

    def webdelet():
        try:
            System.Title("WebHook Deleter")
            System.Size(167, 35)
            clear()
            text=("""
 ____      ____  ________  ______   ____  ____   ___      ___   ___  ____   ______       ______   ________  _____     ________  _________  ________  _______     
|_  _|    |_  _||_   __  ||_   _ \ |_   ||   _|.'   `.  .'   `.|_  ||_  _|.' ____ \     |_   _ `.|_   __  ||_   _|   |_   __  ||  _   _  ||_   __  ||_   __ \    
  \ \  /\  / /    | |_ \_|  | |_) |  | |__| | /  .-.  \/  .-.  \ | |_/ /  | (___ \_|      | | `. \ | |_ \_|  | |       | |_ \_||_/ | | \_|  | |_ \_|  | |__) |   
   \ \/  \/ /     |  _| _   |  __'.  |  __  | | |   | || |   | | |  __'.   _.____`.       | |  | | |  _| _   | |   _   |  _| _     | |      |  _| _   |  __ /    
    \  /\  /     _| |__/ | _| |__) |_| |  | |_\  `-'  /\  `-'  /_| |  \ \_| \____) |     _| |_.' /_| |__/ | _| |__/ | _| |__/ |   _| |_    _| |__/ | _| |  \ \_  
     \/  \/     |________||_______/|____||____|`.___.'  `.___.'|____||____|\______.'    |______.'|________||________||________|  |_____|  |________||____| |___| 
            """)
            print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
            webhooks=input("Webhook url: ")
            if "api/webhooks/" in webhooks:
                try:
                    x=requests.delete(webhooks.rstrip()).text
                    input(colored("Successfully deleted", "green"))
                    main()
                except:
                    clear()
                    input(colored("Invalid Webhooks", "red"))
                    webdelet()
            else:
                clear()
                input(colored("Invalid Webhooks", "red"))
                webdelet()
        except(KeyboardInterrupt):
            clear()
            main()

    def webspam():
        try:
            System.Title("WebHook Spammer")
            System.Size(170, 35)
            clear()
            text=("""
 ____      ____  ________  ______   ____  ____   ___      ___   ___  ____   ______        ______   _______     _       ____    ____  ____    ____  ________  _______     
|_  _|    |_  _||_   __  ||_   _ \ |_   ||   _|.'   `.  .'   `.|_  ||_  _|.' ____ \     .' ____ \ |_   __ \   / \     |_   \  /   _||_   \  /   _||_   __  ||_   __ \    
  \ \  /\  / /    | |_ \_|  | |_) |  | |__| | /  .-.  \/  .-.  \ | |_/ /  | (___ \_|    | (___ \_|  | |__) | / _ \      |   \/   |    |   \/   |    | |_ \_|  | |__) |   
   \ \/  \/ /     |  _| _   |  __'.  |  __  | | |   | || |   | | |  __'.   _.____`.      _.____`.   |  ___/ / ___ \     | |\  /| |    | |\  /| |    |  _| _   |  __ /    
    \  /\  /     _| |__/ | _| |__) |_| |  | |_\  `-'  /\  `-'  /_| |  \ \_| \____) |    | \____) | _| |_  _/ /   \ \_  _| |_\/_| |_  _| |_\/_| |_  _| |__/ | _| |  \ \_  
     \/  \/     |________||_______/|____||____|`.___.'  `.___.'|____||____|\______.'     \______.'|_____||____| |____||_____||_____||_____||_____||________||____| |___| 
        """)
            print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
            webhook=input("Webhook url: ")
            avatar=input("\nWant an avatar (y/n): ")
            if avatar=="n" or avatar=="y":
                g=True
            else:
                input(colored("\nInvalid choice", "red"))
                webspam()
            if avatar=="y":
                avatar_url=input("\nAvatar url: ")
                try:
                    requests.get(avatar_url)
                except:
                    input(colored("\nInvalid url", "red"))
                    webspam()
            else:
                avatar_url=""
            username=input("Webhook username: ")
            if username=="":
                input(colored("\nInvalid username", "red"))
                webspam()
            else:
                g=True
            message=input("Message to spam: ")
            if message=="":
                input(colored("\nInvalid message", "red"))
                webspam()
            else:
                g=True
            input(colored("\nPress enter to start (ctrl+c to stop)", "green"))
            while True:
                r = requests.post(webhook.rstrip(), json={"avatar_url": avatar_url, "username": username, "content": message})
                print(colored("sent", "green"))
                r = str(r)
                if "204" not in r:
                    print(colored("Rate Limited, Please wait...", "red"))
                    time.sleep(3)
        except(KeyboardInterrupt):
            clear()
            main()

    def webhooks():
        try:
            System.Title("WebHook")
            System.Size(38, 30)
            clear()
            text=("""
    ╠════════════════════════════╣
    ║ [1] Webhook spammer        ║
    ║ [2] Webhook deleter        ║
    ╠════════════════════════════╣
            """)
            print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
            choice1 = ("\n              Choice: ")
            if choice1 == "back":
                main()
            print(Colorate.Horizontal(Colors.yellow_to_red, choice1, 1))
            choice=input("                 ")
            if choice == "back":
                main()
            if choice == "1":
                webspam()
            elif choice == "2":
                webdelet()
            elif choice == "3":
                pscan()
            else:
                ip_service()
        except(KeyboardInterrupt):
            clear()
            main()



    def ip_service():
        try:
            System.Title("IP services")
            System.Size(36, 30)
            clear()
            text=("""
   ╠════════════════════════════╣
   ║ [1] IP pinger              ║
   ║ [2] IP tracker             ║
   ║ [3] IP port scanner        ║
   ╠════════════════════════════╣
            """)
            print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
            choice1 = ("\n              Choice: ")
            if choice1 == "back":
                main()
            print(Colorate.Horizontal(Colors.yellow_to_red, choice1, 1))
            choice=input("                 ")
            if choice == "back":
                main()
            if choice == "1":
                pinger()
            elif choice == "2":
                tracker()
            elif choice == "3":
                pscan()
            else:
                ip_service()
        except(KeyboardInterrupt):
            clear()
            main()


    def ytb_dl():
        try:
            System.Title("Youtube Downloader")
            clear()
            text = """
     ____  ____ _________ ______       ________     ____   _____  _____ ____  _____ _____      ____        __      ________   _________ _______    
    |_  _||_  _|  _   _  |_   _ \     |_   ___ \. .'    \.|_   _||_   _|_   \|_   _|_   _|   .'    \.     /  \    |_   ___ \.|_   ___  |_   __ \   
      \ \  / / |_/ | | \_| | |_) |      | |   \. \  .--.  \ | | /\ | |   |   \ | |   | |    /  .--.  \   / /\ \     | |   \. \ | |_  \_| | |__) |  
       \ \/ /      | |     |  __/.      | |    | | |    | | | |/  \| |   | |\ \| |   | |   _| |    | |  / ____ \    | |    | | |  _|  _  |  __ /   
       _|  |_     _| |_   _| |__) |    _| |___.' /  \--'  / |   /\   |  _| |_\   |_ _| |__/ |  \--'  /_/ /    \ \_ _| |___.' /_| |___/ |_| |  \ \_ 
      |______|   |_____| |_______/    |________.' \.____.'  |__/  \__| |_____|\____|________|\.____.'|____|  |____|________.'|_________|____| |___|\n\n"""
            System.Size(150, 35)
            print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
            link = input("\n\nLink: ")
            if link == "back":
                main()
            if link == "":
                ytb_dl()
            if not "youtu" in link:
                ytb_dl()
            f = open(path+'\\Config\\config.json')
            data = json.load(f)
            f.close()
            yt=YouTube(link)
            if data["youtube_default"] == "mp4":
                choice = input("[1]MP3 Default:[2]MP4: ")
                if choice == "":
                    ys = yt.streams.get_highest_resolution()
                    ys.download(path+"\\MP4")
                    print("Download completed!!")
                    input()
                    main()
                if choice == "2":
                    ys = yt.streams.get_highest_resolution()
                    print("\nDownloading '" + yt.title + "'")
                    ys.download(path+"\\MP4")
                    print("Download completed!!")
                    input()
                    main()
                if choice == "1":
                    video = yt.streams.filter(only_audio=True).first()
                    isExist = os.path.exists(path+"\\MP3")
                    if isExist == False:
                        os.system("mkdir MP3")
                    print("\nDownloading '" + yt.title + "'")
                    out_file = video.download(output_path=path+"\\MP3")
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    print("Download completed!!")
                    input()
                    main()
            if data["youtube_default"] == "mp3":
                choice = input("Default:[1]MP3 [2]MP4: ")
                if choice == "":
                    video = yt.streams.filter(only_audio=True).first()
                    isExist = os.path.exists(path+"\\MP3")
                    if isExist == False:
                        os.system("mkdir MP3")
                    print("\nDownloading '" + yt.title + "'")
                    out_file = video.download(output_path=path+"\\MP3")
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    print("Download completed!!")
                if choice == "2":
                    ys = yt.streams.get_highest_resolution()
                    print("\nDownloading '" + yt.title + "'")
                    ys.download(path+"\\MP4")
                    print("Download completed!!")
                    input()
                    main()
                if choice == "1":
                    video = yt.streams.filter(only_audio=True).first()
                    isExist = os.path.exists(path+"\\MP3")
                    if isExist == False:
                        os.system("mkdir MP3")
                    print("\nDownloading '" + yt.title + "'")
                    out_file = video.download(output_path=path+"\\MP3")
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    print("Download completed!!")
                    input()
                    main()
            if choice == "back":
                main()
            if link == "back":
                main()
            

            print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
            choice1 = ("\n                   Choice: ")
            print(Colorate.Horizontal(Colors.yellow_to_red, choice1, 1))
            choice=input("                      ")
        except(KeyboardInterrupt):
            clear()
            main()

    def batch_obf():
        os.system("mkdir "+cwd+"\\Obfuscated >nul 2>&1")
        System.Title("Batch obfuscator")
        clear()
        System.Size(180, 35)
        text=("""
 ______        _     _________    ______  ____  ____         ___   ______   ________  _____  _____   ______     ______       _     _________    ___   _______     
|_   _ \      / \   |  _   _  | .' ___  ||_   ||   _|      .'   `.|_   _ \ |_   __  ||_   _||_   _|.' ____ \  .' ___  |     / \   |  _   _  | .'   `.|_   __ \    
  | |_) |    / _ \  |_/ | | \_|/ .'   \_|  | |__| |       /  .-.  \ | |_) |  | |_ \_|  | |    | |  | (___ \_|/ .'   \_|    / _ \  |_/ | | \_|/  .-.  \ | |__) |   
  |  __'.   / ___ \     | |    | |         |  __  |       | |   | | |  __'.  |  _|     | '    ' |   _.____`. | |          / ___ \     | |    | |   | | |  __ /    
 _| |__) |_/ /   \ \_  _| |_   \ `.___.'\ _| |  | |_      \  `-'  /_| |__) |_| |_       \ \__/ /   | \____) |\ `.___.'\ _/ /   \ \_  _| |_   \  `-'  /_| |  \ \_  
|_______/|____| |____||_____|   `.____ .'|____||____|      `.___.'|_______/|_____|       `.__.'     \______.' `.____ .'|____| |____||_____|   `.___.'|____| |___| 
        """)
        print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
        fpath=input("\nDrag the file to obfuscate here: ")
        with open(temp+"\\tempbat.bat", 'w') as f:
            f.write(r"""
@echo off
set "TempFile=%Temp%\Temp_b64 
set "OutputFile=%~nx1_encoded%~x0"
color 0A & Mode 90,4
echo(
echo         Please wait a while ... Encoding %~nx1 is in progress ...
If exist "%OutputFile%" Del "%OutputFile%" >nul 2>&1
certutil.exe -f -encode "%~1" "%TempFile%" >nul 2>&1
(
   echo @echo off 
   echo set dsqfdfsds=set
   echo %%dsqfdfsds%% dsfgdjs=CERTUTIL
   echo %%dsqfdfsds%% qfdsgsdgsq=decode
   echo %%dsqfdfsds%% qfdsqdsqfq=f
   echo %%dsfgdjs%% -%%qfdsqdsqfq%% -%%qfdsgsdgsq%% "%%~f0" "%%Temp%%\%~nx1" ^>nul 2^>^&1 
   echo "%%Temp%%\%~nx1"
)>> "%OutputFile%"
copy "%OutputFile%" /b + "%TempFile%" /b >nul 2>&1
If exist "%TempFile%" Del "%TempFile%" >nul 2>&1
cls
echo(
echo   Obfuscated file path: """+cwd+r"""\Obfuscated\%~nx1_encoded%~x0
echo                           Finished press enter to continue
copy %~nx1_encoded%~x0 """+cwd+r"""\Obfuscated >nul
del %~nx1_encoded%~x0 >nul 2>&1
            """)
            f.close()
        os.system(temp+"\\tempbat.bat "+fpath+"")
        input()
        main()
    def obfuscator():
        System.Title("Obfuscator")
        System.Size(36, 30)
        text=("""
   ╠════════════════════════════╣
   ║ [1] Python obfuscator      ║
   ║ [2] Batch obfuscator       ║
   ║ [3] Test                   ║
   ╠════════════════════════════╣
        """)
        print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
        choice1 = ("\n              Choice: ")
        if choice1 == "back":
            main()
        print(Colorate.Horizontal(Colors.yellow_to_red, choice1, 1))
        choice=input("                 ")
        if choice == "back":
            main()
        if choice == "1":
            python_obf()
        elif choice == "2":
            batch_obf()
        elif choice == "3":
            pscan()
        else:
            obfuscator()

    def credit():
        System.Title("Credits")
        System.Size(80, 30)
        clear()
        print(colored(r"""
Mixiot is created by lululepu#3412
The code is open source if you want to copy give credit :)

License:
Mixiot is under the MIT License
Using it without giving credit would lead to Breaking the License law""", "green"))
        input()
        main()
    def main():
        System.Title("Mixiot")
        System.Size(63, 30)
        text=("""
   ╠═══════════════════════════════════════════════════════╣
   ║                    Welcome """+username+"""                       ║
   ╠═══════════════════════════════════════════════════════╣
   ║ [1] IP services          █     [5] Test               ║
   ║ [2] Youtube Downloader   █     [6] Test               ║
   ║ [3] Webhooks             █     [7] Test               ║
   ║ [4] Obfuscator           █     [8] Exit               ║
   ╠═══════════════════════════════════════════════════════╣
   ║                     [c] Credits                       ║
   ╠═══════════════════════════════════════════════════════╣
        """)
        print(Colorate.Horizontal(Colors.yellow_to_red, text, 1))
        choice1 = ("\n                           Choice: ")
        print(Colorate.Horizontal(Colors.yellow_to_red, choice1, 1))
        choice=input("                              ")
        if choice == "1":
            ip_service()
        elif choice == "2":
            ytb_dl()
        elif choice == "3":
            webhooks()
        elif choice == "4":
            obfuscator()
        elif choice == "5":
            print("5")
            main()
        elif choice == "6":
            print("6")
            main()
        elif choice == "7":
            print("7")
            main()
        elif choice == "c":
            credit()
        elif choice == "8":
            clear()
            print(colored("Stopped", "green"))
            quit()
        else:
            main()

    main()
except(KeyboardInterrupt):
    clear()
    print(colored("Stopped", "green"))
    exit()
