
import csv
import requests

print("\n")

userinput = raw_input("Please enter the csv file name: ")

userin = './' + userinput
with open(userin, 'r') as f:
    reader = csv.reader(f)
    csv_list = list(reader)
    headers = csv_list[0]

    # Figure out what column in the CSV we're looking for
    endpoint_column = headers.index('ENDPOINT.Name')

    # Get the headers out of our main list
    csv_list.pop(0)
    title = userin[:-4]
    filename = title + 'websites.txt'

    print("\nOutput written to " + userinput[:-4] + "websites.txt\n")

    with open(filename, 'w') as f:
	    f.write("\n\n")
	    i = 0
	    for current_line in csv_list:
		i=i+1
		try:
			response = requests.get(current_line[endpoint_column])
		except requests.exceptions.ConnectTimeout:
			f.write("\nEndpoint: " + current_line[endpoint_column])
			f.write("\nResponse Code: ")
                        f.write(str(response))
			f.write("\nThe site could not be reached\n\n")
			print('Completed Line ' + str(i) + '!')
			continue
		except requests.exceptions.InvalidSchema:
			f.write("\nEndpoint: " + current_line[endpoint_column])
			f.write("\nResponse Code: ")
                        f.write(str(response))
			f.write("\nNo connection adapters were found for the site\n\n")
			print('Completed Line ' + str(i) + '!')
			continue
        	f.write("Endpoint: " + current_line[endpoint_column])

       		if response.status_code < 400:
           		f.write("\nResponse Code = " + str(response) + "; Response: ")
			try:
				f.write(response.text)
			except UnicodeEncodeError:
				f.write("\nThere was an error encoding\n\n")
				print('Completed Line ' + str(i) + '!')
				continue
		else:
			f.write("\nResponse Code: ")
			f.write(str(response))

		print('Completed Line ' + str(i) + '!')

       		f.write("\n\n")
