"""
@author: cyb3ranarch
"""
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("FileDir",help="the file needs to be in the same folder as the script and include the filetype")
args = parser.parse_args()

Pfile=args.FileDir

file = open(Pfile,encoding="UTF-8")
data = file.read()

result = data

file.close()

howMany  = input("enter how many characters/words you want to remove from this file:\n")
newHowMany = input ("enter how many occurences of the word you want  to remove(leave empty if all):\n")
if not newHowMany:
  newHowMany = -1

else:
  newHowMany
  

removecharacters = input("enter the characters/words you want to remove from this file seperating them with ',':\n")

beingRemoved = removecharacters.split(",",int(howMany))

for alldata in beingRemoved:
    result = result.replace(alldata,"",int(newHowMany))

formatter = input("Enter the character used to format for a table(leave empty if you don't need to format your data to a table):\n")

if not formatter:
    final = result
else:
    formatter
    final = result.replace(formatter,"\t")

new_file = open('results.txt','w')
new_file.writelines(final)


print(final)
new_file.close()
