#!/bin/sh
#scan with theHarvester
echo "start scanning"
read -p "Plz type the namelist: " namelist
read -p "Choose a theHarvester searching engine(google,bing,bingapi,pgp,linkedin,google-profiles,people123,jigsaw,all)(default:google): " engine
engine=${engine:-"google"}
namelist=${namelist}".txt"
rfile="./""${namelist}"
foldername="Scanning"$(date +%R)
mkdir ${foldername}
while IFS= read line
do
        # display $line or do somthing with $line
	echo ${line}
	filename=${line}
	filename=${filename}".txt"
	touch ${filename}
	echo "result with write into $(pwd)/${foldername}/""${filename}"
	wfile="./""${filename}"
	echo ${line} > ${wfile}
	echo "TheHarvester Scanning"
	echo "TheHarvester Scanning:" >> ${wfile}
	echo "$(theharvester -d ${line} -l 500 -b google)" >> ${wfile}
	mv ${filename} "./${foldername}"
done <"$rfile"


