lyrics = [
    "{} green bottle{} hanging on the wall,",
    "{} green bottle{} hanging on the wall,",
    "and if one green bottle should accidentally fall,",
    "there'd be {} green bottle{} hanging on the wall.\n\n"
]

def tick(n):
    for lyric in lyrics:
        if lyric == lyrics[3]: n -= 1
        print(lyric.format(n if n > 0 else "no", "" if n == 1 else "s").capitalize())
    return n

def greenBottles(n):
    for i in range(n, -1, -1):
        n = tick(i)
    
greenBottles(10)