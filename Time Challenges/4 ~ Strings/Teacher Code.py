def Initials(first,last,middle="Z"):
    return first.upper()[0]+middle.upper()[0]+last.upper()[0]

print(Initials("Oliver", "Norval"))
print(Initials("Nico", "Saunders", middle="Juan"))