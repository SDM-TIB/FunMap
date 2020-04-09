#!/bin/bash


declare -a mappings=("complex_sameFunction.ttl" "complex_sameFunction2.ttl" "complex_sameFunction3.ttl" "complex_sameFunction4.ttl")
declare -a dataArray=("veracity25.csv" "veracity50.csv"  "veracity75.csv" "veracity100.csv")
echo "engine,dataset,mapping,time,results" > results.csv

for data in "${dataArray[@]}"
do
	echo "---------Running transformation for $data------------"
	cp $data data.csv
	for mapping in "${mappings[@]}"
	do
		echo "Running $mapping"
		for i in 1 2 3 4 5
		do
			start=$(date +%s.%N)
			java -jar rmlmapper.jar -m $mapping -f function_complex.ttl -o output.nt -d
			dur=$(echo "$(date +%s.%N) - $start" | bc)
			noutput=$(wc -l output.nt | cut -d " " -f 1)
			echo "rmlmapper,$data,$mapping,$dur,$noutput"  >> results.csv
			rm output.nt
		done	
	done	
done