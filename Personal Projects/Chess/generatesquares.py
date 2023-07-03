print("squares = [")
files = list("abcdefgh")

for filenum in range(0,8):
    for rank in range(1,9):
        file = files[filenum]
        print(f"\t'{file.lower()}{rank}': chess.{file.upper()}{rank}")
print("]")