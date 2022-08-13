#!/bin/bash

#test=$(curl "https://api.genderize.io/?name=emilio" | jq '.gender')
#echo $test

var1 = 1

if [$var1 -eq 1]
then
	echo "iguales"
else
	echo "diferentes"
fi
