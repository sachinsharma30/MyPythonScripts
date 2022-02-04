"""
Prerequisites:
have csv file installed
"""

import csv
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
regions = []

while(True):
    debianinput = input("Please enter the Debian Linux Version (Type \"exit\" to end the program): ")
    if(debianinput == "exit"):
        break

    regioninput = input("Please enter the Region (Press enter if you want to view all regions): ")
    if regioninput == "":
        debcounter = 0
        for current_line in csv_list:
            if debianinput == current_line[version_column]:
                debcounter = debcounter+1
        print(f"\nDebian Linux | {debianinput} | {debcounter} resources found in all regions\n")             
        continue
    matchcounter=0

    for current_line in csv_list:
        if current_line[version_column] == debianinput and current_line[location_column] == regioninput:
            matchcounter = matchcounter+1
    
    print(f"\nDebian Linux | {debianinput} | {matchcounter} resources found in {regioninput}\n")
        
print("")