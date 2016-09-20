# OSSAnalyser
Gather statistical data from the Web Statistics Module of OpenSim, analyse them and visualize them

Author
-----
Hussein Bakri

Program Name
-----------
OSSAnalyser 1.0

License
-------
This program is licensed under GNU GPL v3 License - you are free to distribute, change, enhance and include any of the code of this application in your tools.
I only expect adequate attribution of this work. The attribution should include the title of the program, the author and the site or the document where the program is taken from.

Description
-----------
Parses HTML files from Web Statistics AJAX module into ONE CSV file for later statistical analysis.
It utilizes the BeautifulSoup Python module (bs4) which needs to be installed. 
It utilizes also the csv module which needs to be available.

ParseHTMLToCSVsimstatsajax.py
-----------------------------
This script Parses the HTML files obtained and stored in SStats_simstatsajax and transform all of them into one CSV file for statistical analysis

requestTest.py
--------------
This script transform Transform JSON files that Web Statistics AJAX module through UXSimStatus into ONE CSV file for later statistical analysis
It uses the Request module to request every 1 second for 3 minutes (180 seconds)  http://0.0.0.0:9000/SStats/simstatsajax.html'
It Implements another shell script named: "SStatscript" using the Python requests module

SStatscript.sh shell script
--------------------------
This Bash shell script saves statistics every 1 second for 3 minutes (during 180 seconds) from the OpenSim Web Statistics Module
OpenSim Wiki article : http://opensimulator.org/wiki/Web_Statistics_Module
The challenge solved is to get the XHR calls URLs of the AJAX page - This was done through using the Developer tools of Web browsers mainly the Network Inspectors. 

The 3 XHR call URLS are being fetched regularly on the AJAX page:
http://0.0.0.0:9000/SStats/simstatsajax.html - have useful Simulator stats

http://0.0.0.0:9000/SStats/activelogajax.html - NOTHING USEFUL HERE. It is retrieved for completion sake

http://0.0.0.0:9000/SStats/activeconnectionsajax.html - has useful stats about packets in the different channels of circuits of each region.

The Shell script fetches XHR URLs using wget command and stores the output as HTML files in seperate folders (3 folders)
Python scripts will later -in each folder- parse the HTML files and store their content into ONE CSV file for later statistical Analysis.
This script will generate many files and take some time....

Technicalities
-------------
This tool uses Python 3.5.2
To install Python BeautifulSoup module on Linux: sudo pip3 install BeautifulSoup

TODO
-----
1)needs improvement 
2)include matplotlib, numpy and scipy functionality for useful stats

Enjoy!
