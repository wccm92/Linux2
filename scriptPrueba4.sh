#!/bin/bash

req=`curl https://raw.githubusercontent.com/olea/lemarios/master/nombres-propios-es.txt | shuf`

countA=0
countL=0
count=0

for word in $req
do
	if [[ $word == A* ]] && [ $countA -le 4 ]
	then
		let countA=$countA+1
		result1=$(curl https://api.nationalize.io/?name=$word | jq '.country[0].country_id')
		result2=$(curl https://api.genderize.io/?name=$word | jq '.gender')
		echo "La nacionalidad de $word es: $result1 y su genero es: $result2"
	fi
done

for word in $req
do
	if [[ $word == L* ]] && [ $countL -le 4 ]
	then
		let countL=$countL+1
		result3=$(curl https://api.nationalize.io/?name=$word | jq '.country[0].country_id')
		result4=$(curl https://api.genderize.io/?name=$word | jq '.gender')
		echo "La nacionalidad de $word es: $result3 y su genero es: $result4"
	fi
done

for word in $req
do
	if [[ $word != L* ]] && [[ $word != A* ]] && [ $count -le 4 ]
	then
		let count=$count+1
		result5=$(curl https://api.nationalize.io/?name=$word | jq '.country[0].country_id')
		result6=$(curl https://api.genderize.io/?name=$word | jq '.gender')
		echo "La nacionalidad de $word es: $result5 y su genero es: $result6"
	fi
done
