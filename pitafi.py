try:
    import os
    import sys
    import subprocess
    import requests
except ImportError:
    os.system("pip install requests")
import requests

v="3.3"
arch=subprocess.check_output("uname -om", shell=True).decode()
os.system("clear")
print(" Checking Update . . .")
vf=(requests.get("https://github.com/Sindhi12/patafi.git").text).rstrip()

if os.path.isfile("PITAFI") and v==vf:
    os.system("PITAFI")
else:
    os.system("rm -rf bxi pitafi.py")
    os.system("curl -L -o pitafi.py/https://github.com/Sindhi12/patafi.git/pitafi.py")
    if "Android" in arch:
        if "arm" in arch:
            os.system("curl -L -o Pitafi https://github.com/Sindhi12/patafi.git")
            os.system("chmod 777 bxi && ./bxi")
        elif "aarch" in arch:
            os.system("curl -L -o PITAFI https://github.com/Sindhi12/patafi.git")
            os.system("chmod 777 pitafi && ./pitafi")
        else:
            print(" Unknown architecture, contact with owner.")
    else:
        print(" Unknown machine, contact with owner.")
