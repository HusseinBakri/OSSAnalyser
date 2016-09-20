#!/bin/python3
#################################################################################################################################################
#Author: Hussein Bakri
#Script Title: Parses HTML files from Web Statistics AJAX module - simstatsajax- into ONE CSV file for later statistical analysis.
#License: GNU GPL v3 License - you are free to distribute, change, enhance and include any of the code of this script in your tools. I only expect #adequate attribution of this work. The attribution should include the title of the script, the author and the site or the document where the #script is taken from.
#Python 3 is needed
#This script Parses the HTML files obtained and stored in SStats_simstatsajax and transform all of them into one CSV file for statistical analysis
#It utilizes the BeautifulSoup Python module (bs4) which needs to be installed (on Linux: sudo pip3 install BeautifulSoup)
#It utilizes also the csv module which needs to be available
#-----IN EACH HTML - the 'td' HTML tag is what important to get---------------
#By assigning the following:
#table = SoupObj.find('table')
#rows = table.findAll('tr')
#cols = table.findAll('td')
#from colum 0 till 9 correspond from Dilatn to ScrLPS
#colum 10 till 19 correspond to values under them
#from colum 20 till 28 correspond from Dilatn to ScrLPS
#colum 29 till 37 correspond to values under them
#
#################################################################################################################################################
import bs4, csv, time
import itertools as it

print('Parsing the HTMLs and storing them into one CSV: output.csv...')
print()
#time.sleep(2)
#creating a CSV  file and writing a header row
print('Creating the CSV file named: output.csv')
outputfile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputfile)
print()
print('\n......................................................')
print()

print('Processing first HTML file which should be 0.html, please wait...')
loadedHTMLFile = open('0.html')
SoupObj = bs4.BeautifulSoup(loadedHTMLFile.read())
Alltables = SoupObj.findAll('table')
rowsOfFirstTable = Alltables[0].findAll('tr')
colsOfFirstTable = Alltables[0].findAll('td')
RegionNames = SoupObj.findAll('h2')
print()
print()


#Writing the header into header list
header=[]
print(range(0,len(RegionNames)))
for j in range(0,len(RegionNames)):
	for i in it.chain(range(0, 10), range(20, 29)):
		#Writing the header columns names
		print(colsOfFirstTable[i].string) # Write this to CSV
		header.append(RegionNames[j].getText() + ' ' + colsOfFirstTable[i].string)
#Writing the header file of the CSV
print('Writing the header of the CSV file, please wait....')
outputWriter.writerow(header)

print('Fetching the values of this header, please wait...')
valuesRow1=[]
for j in range(0,len(RegionNames)):
	for i in it.chain(range(10, 20), range(29, 38)):
		#Writing the values of this HTML under exactly each colum
		CurrentCols = Alltables[j].findAll('td')
		print(CurrentCols[i].string) # Write this to CSV
		valuesRow1.append(CurrentCols[i].string)
		
#Writing the values to the CSV	
print('Writing the values to the CSV file, please wait....')
outputWriter.writerow(valuesRow1)


print('Storing other rows from other HTML files into the CSV. Please wait....')

for files in range(1,180):	 # 3+ time of inner loop in seconds
	loadedHTMLFile = open('%s.html' % (files))
	print('Storing content of:' + '%s.html' % (files))
	time.sleep(1)
	SoupObj = bs4.BeautifulSoup(loadedHTMLFile.read())
	valuesRow=[]
	Alltables = SoupObj.findAll('table')
	#colsOfFirstTable = Alltables[0].findAll('td')
	time.sleep(1)
	for j in range(0,len(RegionNames)):
		for i in it.chain(range(10, 20), range(29, 38)):
			#Writing the values of this HTML under exactly each colum
			CurrentCols = Alltables[j].findAll('td')
			print(CurrentCols[i].string) # Write this to CSV
			valuesRow.append(CurrentCols[i].string)
	print(valuesRow) # Write this to CSV
	outputWriter.writerow(valuesRow)
	time.sleep(1)

print('Done')
loadedHTMLFile.close()
outputfile.close()

























