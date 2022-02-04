# This runs only on Python3
import csv
from re import L
import requests

print("")


while True:

    userinput = input("Please enter the csv file name: ")
    userin = './' + userinput

    try:
        with open(userin, 'r') as f:
            reader = csv.reader(f)
            csv_list = list(reader)
            headers = csv_list[0]
            break
    except FileNotFoundError:
        print("File does not exist\n")
        
print("")


version_column = headers.index('HOSTED_TECHNOLOGY.version')
location_column = headers.index('HOSTED_TECHNOLOGY.region')

csv_list.pop(0)

regionarray = []
regioncounter = []

for i in csv_list:
    exists = i[location_column] in regionarray
    if(exists == False):
        regionarray.append(i[location_column])
        regioncounter.append(0)


while(True):
    debianinput = input("Please enter the Debian Linux Version (Type \"exit\" to end the program): ")
    if(debianinput == "exit"):
        break
    for current_line in csv_list:
        if debianinput == current_line[version_column]:
            regioncounter[regionarray.index(current_line[location_column])]+=1 

    count = 0
    
    exists = False
    for cur in regionarray:
        if(regioncounter[count]>0):
            print(f"Debian Linux | {debianinput} | {regioncounter[count]} resources found in {regionarray[count]}")
            exists=True
        regioncounter[count] = 0
        count+=1
    
    if exists == False:
        print(f"Debian Linux | {debianinput} |  No resources found")
    
    print("")
    
