#!/bin/bash


## mappings to be applied in the experiments
declare -a mappings=("sameFunction_4.ttl" "sameFunction_6.ttl" "sameFunction_8.ttl" "sameFunction_10.ttl" "complex_sameFunction4.ttl" "complex_sameFunction6.ttl" "complex_sameFunction8.ttl" "complex_sameFunction10.ttl" )
## datasets to be applied in the experiments
declare -a dataArray=("veracity75.csv" "veracity25.csv")

## Running FunMap+SDM-RDFizer
echo "dataset,mapping,time,iteration" > complete-results-funmap-sdmrdfizer.csv
echo "dataset,mapping,time,iteration" > complete-results-funmap-basic-sdmrdfizer.csv
echo "dataset,mapping,time,iteration" > complete-results-sdmrdfizer.csv

echo "dataset,mapping,time" > results-funmap-sdmrdfizer.csv
echo "dataset,mapping,time" > results-funmap-basic-sdmrdfizer.csv
echo "dataset,mapping,time" > results-sdmrdfizer.csv

echo "---------Running experiments over SDM-RDFizer------------"

for mapping in "${mappings[@]}"
do    
        for data in "${dataArray[@]}"
        do
                echo "Running experiment $mapping and $data"
                total1=0
                total2=0
                total3=0
                for i in 1 2 3 4 5
                do
                        cp ./data/$data data.csv
                        cp ./mappings/$mapping mapping.ttl
                        ########################################################################################
                        #################### Running FunMap+SDM-RDFizer experiments ############################
                        ########################################################################################
        		echo "FunMap+SDM-RDFizer: iteration $i"
                        start=$(date +%s.%N)
        		## Running FunMap:
        		python3 ./FunMap/run_translator.py config-funmap.ini
        		## Running SDM-RDFizer over the results:
                        python3 ./SDM-RDFizer/rdfizer/run_rdfizer.py config-SDM.ini
                        dur=$(echo "$(date +%s.%N) - $start" | bc)
                        total1=$(echo "$total1+$dur" | bc)
                        echo "$data,$mapping,$dur,$i" >> complete-results-funmap-sdmrdfizer.csv
                        

                        ########################################################################################
                        #################### Running FunMap(-)+SDM-RDFizer experiments ############################
                        ########################################################################################
                        echo "FunMap-Basic+SDM-RDFizer: iteration $i"
                        start=$(date +%s.%N)
                        ## Running FunMap:
                        python3 ./FunMap/run_translator.py config-funmap-basic.ini
                        ## Running SDM-RDFizer over the results:
                        python3 ./SDM-RDFizer/rdfizer/run_rdfizer.py config-SDM.ini
                        dur=$(echo "$(date +%s.%N) - $start" | bc)
                        total2=$(echo "$total2+$dur" | bc)
                        echo "$data,$mapping,$dur,$i" >> complete-results-funmap-basic-sdmrdfizer.csv

        		########################################################################################
                        #################### Running SDM-RDFizer+Functions experiments #########################
                        ########################################################################################
        		echo "SDM-RDFizer: iteration $i"
                        start=$(date +%s.%N)
        		python3 ./SDM-RDFizer-Functions/rdfizer/run_rdfizer.py config-SDM-function.ini
        		dur=$(echo "$(date +%s.%N) - $start" | bc)
                        total3=$(echo "$total3+$dur" | bc)
        		echo "$data,$mapping,$dur,$i" >> complete-results-sdmrdfizer.csv
        		
        	done
                total1=$(echo "$total1/5" | bc -l)
                total2=$(echo "$total2/5" | bc -l)
                total3=$(echo "$total2/5" | bc -l)
                echo "$data,$mapping,$total1"  >> results-funmap-sdmrdfizer.csv
                echo "$data,$mapping,$total2"  >> results-funmap-basic-sdmrdfizer.csv
                echo "$data,$mapping,$total3"  >> results-sdmrdfizer.csv
        done
done

rm data.csv
rm maping.ttl



