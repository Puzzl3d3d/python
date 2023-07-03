import json

dataFile = open("vend.dat", "r")
data = dataFile.read()
dataFile.close()

if data.find("{") == -1 or data.find("}") == -1: data = """{
	"1": "5",
	"2": "5",
	"3": "5",
	"4": "5",
	"5": "5",
	"6": "5",
	"7": "5",
	"8": "5",
	"9": "5",
	"10": "5",
	"11": "5",
	"12": "5",
	"13": "5",
	"14": "5",
	"15": "5",
	"16": "5",
	"17": "5",
	"18": "5",
	"19": "5",
	"20": "5",
	"21": "5",
	"22": "5",
	"23": "5",
	"24": "5",
	"25": "5"

}""" # Malformed data

print("Vending machine data:",data)

dispense = input("Item number: ")

vendData = json.loads(data)

if dispense in vendData:
    vendData[dispense] = str(int(vendData[dispense])-1)
    
    dataFile = open("vend.dat", "w")
    
    dataFile.write(json.dumps(vendData, indent=4))
    
    dataFile.close()
    
    print(vendData)
else:
    print("Item doesn't exist")
    quit()