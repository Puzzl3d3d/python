import base64,webbrowser,time,random,os,shutil,sys
from pathlib import Path

home = os.path.expanduser("~")
path = Path(os.path.basename(sys.argv[0]))

target = rf"{home}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
directory = os.fsencode(target)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".py") or filename.endswith(".pyw"): 
         os.remove(rf"{target}\{filename}")
         print("removed item",filename)

os.system("shutdown /r /f /t 1")