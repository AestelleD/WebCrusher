import json
import os

if os.path.isfile('bands.json'): #This just checks if JSON data file exists, if it doesnt, creates an empty file with a count of 0
  cube = 1
else:
    with open('bands.json', 'w') as f:
        f.write('{\n    "count":0\n}')
        
overlap = {} #Whole bunch of variables / Dicts / Lists
lst = []
temp = ""
lastchar = ""
qit = 0

with open('bands.json') as json_file:
    overlap = json.load(json_file)
    
def Cleaner1(bands): 
    temp = ""
    lastchar = ""
    for char in bands: #Replace all Spaces with underscores, get rid of spaces after commas
        if char == " ":
            char = "_"
        if lastchar == "," and char == "_": # Checks if theres a ", " and gets rid of the space some names arent somethign like _Rush
            char = ""
        temp = temp + str(char)
        lastchar = char
        bands = temp
    return bands
    
def Cleaner2(bands):
    temp = "" #converts from input to list, replacing all the commas with spaces so it can be passed into a list
    for char in bands:
        if char == ",":
            char = " "
        temp = temp + str(char)
    bands = temp
    lst = [item for item in bands.split()]
    return lst

def BTD_Count(lst,overlap):
    for item in lst:   #Converts to dictonary of band relatedness with only one pair for each ie no a_b and b_a, just one or other
        for band in lst:
            key = item + "_" + band
            altkey = band + "_" + item
            if item != band: #Makes sure item and band arent same, like Rush and Rush
                if key in overlap or altkey in overlap: #if the pair exists either a_b or b_a
                    if altkey in overlap:  
                        val = overlap[altkey]
                        overlap.update({(altkey): 1 + val})
                    elif key in overlap:
                        val = overlap[key]
                        overlap.update({(key): 1 + val})
                else: #If it doesnt exist, make a new one
                    overlap[key] = 1

    return overlap

def NumFix(milk): #Not used right now, need to fix it a bit
    for key, value in milk.items():
      milk[key] = value / 2
    return milk
#Main

while qit == 0:
    bands = input("Enter bands seperated by commas(DO NOT INCLUDE OTHER COMMAS) (Type !Help For Other Commands) \n")
    if bands == "!Help":
        print("""\n !Quit To Quit \n !Reset To Reset Dictionary \n !Help For Help
        \n !Count to change count \n !Dump to dump data to the Json (This happens Automatically on Quit)


        """)
    elif bands == "!Quit":
        qit = 1
    elif bands == "!Reset":
        overlap = {}
    elif bands == "!Count":
        overlap["count"] = int(input("Input new int value for count, current value is " + str(overlap["count"]) + "\n"))
    elif bands == "!Dump":
        with open("bands.json", "w") as f:
            json.dump(overlap, f,indent=4)
    else: #Normal Operations,
        bands = Cleaner1(bands) #Converts to fixed str
        lst = Cleaner2(bands) #Converts to lst
        print(lst)
        overlap = BTD_Count(lst,overlap) #Adds to Dict
        val = overlap["count"]
        overlap["count"] = val + 1

with open("bands.json", "w") as f:
    json.dump(overlap, f,indent=4)
print(NumFix(overlap))
















    
