#!/bin/bash

for word in $(cat personas)
do
	gen=$(curl https://api.genderize.io/?name=$word | jq '.gender')
	na=$(curl https://api.nationalize.io/?name=$word | jq '.country[0].country_id')
	echo "El genero de $word es : $gen";
	echo "Su nacionalidad es : $na";
done
