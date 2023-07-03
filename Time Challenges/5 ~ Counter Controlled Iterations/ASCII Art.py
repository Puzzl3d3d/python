#+-+-+-+-+-+-+-+-+-+-+-+-+
#|C|R|A|I|G|'|N|'|D|A|V|E|
#+-+-+-+-+-+-+-+-+-+-+-+-+

def ASCII(text):
    top = ""
    for i in range(len(text)*2 + 1):
        top += "+" if i%2 != 1 else "-"
        
    print(top)
    
    for char in text:
        print(f"|{char}",end="")
    print("|")
    
    print(top)

while True: ASCII(input("Billboard text: "))