#!/bin/bash
##################################################################################################################################################
#Author: Hussein Bakri
#Script Title: Method of getting stats from the OpenSim AJAX Web Statistical module and storing them in HTML files
#License: GNU GPL v3 License - you are free to distribute, change, enhance and include any of the code of this script in your tools. I only expect #adequate attribution of this work. The attribution should include the title of the script, the author and the site or the document where the #script is taken from.
#The Web Statistics Module provides region statistics information. The data is provided as AJAX html page which automatically updates over time. #The page is provided by the internal OpenSimulator web server. The module also stores historical data which is displayed on these web pages. 
#----------- Retrieve HTML files from Web Statistics AJAX module -simstatsajax/activelogajax/activeconnectionsajax---------
#This Bash shell script saves statistics every 1 second for 3 minutes (during 180 seconds) from the OpenSim Web Statistics Module
#OpenSim Wiki article : http://opensimulator.org/wiki/Web_Statistics_Module
#The challenge solved is to get the XHR calls URLs of the AJAX page - This was done through using the Developer tools of Web browsers mainly the
#Network Inspectors. The 3 XHR call URLS are being fetched regularly on the AJAX page:
#http://0.0.0.0:9000/SStats/simstatsajax.html - have useful Simulator stats
#http://0.0.0.0:9000/SStats/activelogajax.html - NOTHING USEFUL HERE. It is retrieved for completion sake
#http://0.0.0.0:9000/SStats/activeconnectionsajax.html - has useful stats about packets in the different channels of circuits of each region.
#The Shell script fetches XHR URLs using wget command and stores the output as HTML files in seperate folders (3 folders)
#Python script(s) will later -in each folder- parse the HTML files and store their content into ONE CSV file for later statistical Analysis.
#This script will generate many files and take some time....
##################################################################################################################################################
echo "Let us begin the retrieval of statistics Through Web Statistics Module in the OpenSim server..."
echo 
echo "Retrieval is done every 1 second for 3 minutes or during 180 seconds (i.e 180 values intake)"
echo
echo " It is done through the retrival of HTML files from the HTTP Server (Web Statistics Module) of OpenSim through the wget command..."
echo " on http://<OPENSIMSERVERIP>:9000/SStats/"

echo 
echo 
echo

echo "Please go and launch any avatar mobility script you want - you can not do anything here if you want, just press any key ..."
sleep 2
read -rsp $'When ready, Press any key in this terminal to continue - terminal should be in focus...\n' -n1 key

echo "Creating a folder named SStats_simstatsajax (if it does not exist)...."
mkdir -p SStats_simstatsajax
echo

echo "Creating a folder named SStats_activelogajax (if it does not exist)...."
mkdir -p SStats_activelogajax
echo

echo "Creating a folder named SStats_activeconnectionsajax (if it does not exist)...."
mkdir -p SStats_activeconnectionsajax
echo

filenumber=0
while [ $filenumber -lt 180 ]
do
wget http://0.0.0.0:9000/SStats/simstatsajax.html -O SStats_simstatsajax/${filenumber}.html
wget http://0.0.0.0:9000/SStats/activelogajax.html -O SStats_activelogajax/${filenumber}.html
wget http://0.0.0.0:9000/SStats/activeconnectionsajax.html -O SStats_activeconnectionsajax/${filenumber}.html
sleep 1
((filenumber++))
done
echo "Retrieval Finished ...."
echo
echo "..."

echo "Bye"
 

