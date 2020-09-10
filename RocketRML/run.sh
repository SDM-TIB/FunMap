#! /bin/bash

#############################################################################
######################## Running Rocketrml experiments ######################
#############################################################################

## mappings to be applied in the experiments


echo "dataset,mapping,time,iteration" > complete-results-rocketrml.csv
echo "dataset,mapping,time,iteration" > complete-results-funmap-rocketrml.csv
echo "dataset,mapping,time,iteration" > complete-results-funmap-basic-rocketrml.csv

echo "dataset,mapping,time" > results-rocketrml.csv
echo "dataset,mapping,time" > results-funmap-rocketrml.csv
echo "dataset,mapping,time" > results-funmap-basic-rocketrml.csv

echo "---------Running experiments over RocketRML------------"
echo "---------Running first FunMap over RocketRML---------"

#### mapping with 4 same simple functions:
declare -a mappings=("4" "6" "8" "10")
## datasets to be applied in the experiments
declare -a dataArray=("veracity75.csv" "veracity25.csv")

echo "---------Running FunMap+RocketRML------------"

for mapping in "${mappings[@]}"
do
        for data in "${dataArray[@]}"
        do
        	echo "-----Running experiment for $mapping on $data------"
                total1=0
                total2=0
        	for i in 1 2 3 4 5
        	do
        		cp ./data/$data data.csv
        		cp ./mappings/sameFunction_${mapping}.ttl mapping.ttl
                        echo "FunMap+RocketRML: iteration $i"
        		start=$(date +%s.%N)
        		python3 ./FunMap/run_translator.py config.ini
        		node --max-old-space-size=32000 index-FunMap_${mapping}Triples.js
        		dur=$(echo "$(date +%s.%N) - $start" | bc)
                        total1=$(echo "$total1+$dur" | bc)
        		echo "$data,sameFunction_${mapping}.ttl,$dur,$i" >> complete-results-funmap-rocketrml.csv

                        echo "FunMap-Basic+RocketRML: iteration $i"
                        start=$(date +%s.%N)
                        python3 ./FunMap/run_translator.py config-basic.ini
                        node --max-old-space-size=32000 index-FunMap_${mapping}Triples.js
                        dur=$(echo "$(date +%s.%N) - $start" | bc)
                        total2=$(echo "$total2+$dur" | bc)
                        echo "$data,sameFunction_${mapping}.ttl,$dur,$i" >> complete-results-funmap-basic-rocketrml.csv
                       
        		rm data.csv
        		rm mapping.ttl
        	done
                total1=$(echo "$total1/5" | bc -l)
                total2=$(echo "$total2/5" | bc -l)
                echo "$data,$mapping,$total1"  >> results-funmap-rocketrml.csv
                echo "$data,$mapping,$total2"  >> results-funmap-basic-rocketrml.csv
        done
done

declare -a mappings=("sameFunction_4_rocketrml.ttl" "sameFunction_6_rocketrml.ttl" "sameFunction_8_rocketrml.ttl" "sameFunction_10_rocketrml.ttl")

echo "---------Running RocketRML with simple function---------"

for mapping in "${mappings[@]}"
do
        for data in "${dataArray[@]}"
        do
                echo "Running experiment for $mapping on $data"
                total=0
                for i in 1 2 3 4 5
                do
                        cp ./data/$data data.csv
                        cp ./mappings/$mapping mapping.ttl
                        echo "RocketRML: iteration $i"
                        start=$(date +%s.%N)
                        node --max-old-space-size=32000  index.js
                        dur=$(echo "$(date +%s.%N) - $start" | bc)
                        total=$(echo "$total+$dur" | bc)
                        echo "$data,$mapping,$dur,$i"  >> complete-results-rocketrml.csv
                        rm data.csv
                        rm mapping.ttl
                done
                total=$(echo "$total/5" | bc -l)
                echo "$data,$mapping,$total"  >> results-rocketrml.csv
        done
done