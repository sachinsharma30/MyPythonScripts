import json
import csv
from urllib import response
import requests

print("\nWelcome to Stocks Tracking!")

ticker = input('Please enter the ticker for the stock you would like to view: ')
startdate = input("Please enter the start date for when you would like to track the stock (YYYY-MM-DD): ")
enddate = input("Please enter the end date for when you would like to track the stock (YYYY-MM-DD): ")

link = 'https://api.polygon.io/v2/aggs/ticker/' + ticker + '/range/1/day/'+startdate+'/'+enddate+'?apiKey=SHeTNppmJP5_JLzJhMW8CyR27xhOtqEe'
r = requests.get(link)
data = json.loads(r.text)
i=1
try:
	for counter in data["results"]:
		print(f"Day {i}:\nHigh: {counter['h']}\nLow: {counter['l']}\n")
		i+=1
except KeyError:
	 print("One or more of the entries was invalid\n")
