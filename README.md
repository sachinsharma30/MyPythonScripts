# My Script Notes

websiteresponses.py
  This program allows the user to enter a csv file with AWS web servers (HTTP endpoints) and will display the output from the websites onto a new text file
  user input: csv file name (servers.csv)
  output to text file (serverswebsites.txt): Endpoint (ex: http://54.37.12.91) Response code (ex: 200, 404), Website output (only prints output if endpoint doesn't display error code 

versions.py
  This program allows the user to enter a csv file with Linux versions and regions and will return the number of instances with the specific region & version
  user input: csv file name (ex: Linux.csv), Linux version (ex: 10.10), region (ex: us-west1)
    (ex output: 5 10.10 instances found in us-west1) 

versions2.py
  This program is a variation of versions.py in which the user does not have to specify the region. The program will output all speicified instances in all regions
