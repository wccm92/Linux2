#!/bin/bash

for word in $(cat personas)
do
	if [ $word = "juan" ]
	then
		echo "Encontre a juan"
	else
		let a=$a+1
	fi
done
echo $a
