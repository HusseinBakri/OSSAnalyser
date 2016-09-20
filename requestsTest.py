#!/bin/python3
#################################################################################################################################################
#Author: Hussein Bakri
#Script Title: Retrieve HTML files from Web Statistics AJAX module - simstatsajax
#License: GNU GPL v3 License - you are free to distribute, change, enhance and include any of the code of this script in your tools. I only expect #adequate attribution of this work. The attribution should include the title of the script, the author and the site or the document where the #script is taken from.
#---------- 
#
#Python 3 is needed
#This script transform Transform JSON files that Web Statistics AJAX module through UXSimStatus into ONE CSV file for later statistical analysis
# It uses the Request module to request every 1 second for 3 minutes (180 seconds)  http://0.0.0.0:9000/SStats/simstatsajax.html'
# It Implements another shell script named: "SStatscript" using the Python requests module
#
#################################################################################################################################################
import webbrowser, requests, time, sys, bs4, os

print('Implementing the shell script using the Python requests module...')
print("Let us begin the retrieval of statistics Through SStats in the OpenSim server.")
print() 
print("Retrieval is done every 1 second for 3 minutes or during 180 seconds (i.e 180 values intake)")
print()
print(" It is done through the retrival of HTML files from the HTTP Server (Web Statistics Module) of OpenSim thorough Python requests module...")
print(" on http://0.0.0.0:9000/SStats/")

print()
print()
print()

print("Please go and launch any avatar mobility script you want - you can not do anything here if you want, just press any key ...")
time.sleep(2)

print("Creating a folder named SStats_simstatsajax (if it does not exist)....")
if not os.path.exists('SStats_simstatsajax'):
    os.makedirs('SStats_simstatsajax')


print("Creating a folder named SStats_activelogajax (if it does not exist)....")
if not os.path.exists('SStats_activelogajax'):
    os.makedirs('SStats_activelogajax')

print("Creating a folder named SStats_activeconnectionsajax (if it does not exist)....")
if not os.path.exists('SStats_activeconnectionsajax'):
    os.makedirs('SStats_activeconnectionsajax')

print('\n..............................................')
print()

for i in range(0,180):
	print(i)
	#if request succeed, the downloaded web page is stored as a string in the Response object res text variable
	res = requests.get('http://0.0.0.0:9000/SStats/simstatsajax.html') 
	res.raise_for_status()
	print('\nLength of the response: ' + str(len(res.text)))
	HTMLFile = open('SStats_simstatsajax/%s.html' % (i) , 'wb')  #wb: for write binary mode-this to maintain the unicode encoding of the text
	for chunck in res.iter_content(int(len(res.text))):
		HTMLFile.write(chunck)
	time.sleep(1)

#check if the files needs to be closed! maybe not
#print(type(res))
#print(res.status_code == requests.codes.ok)
#print(len(res.text))
#print(res.text[:90000])























