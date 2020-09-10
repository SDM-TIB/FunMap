#!/bin/bash


## mappings to be applied in the experiments
declare -a mappings=("sameFunction_4.ttl" "sameFunction_6.ttl" "sameFunction_8.ttl" "sameFunction_10.ttl" "complex_sameFunction4.ttl" "complex_sameFunction6.ttl" "complex_sameFunction8.ttl" "complex_sameFunction10.ttl" )
## datasets to be applied in the experiments
declare -a dataArray=("veracity75.csv" "veracity25.csv")

## Running FunMap+SDM-RDFizer
echo "dataset,mapping,time,iteration" > results-funmap-sdmrdfizer.csv
## Running FunMap(-)+SDM-RDFizer
echo "dataset,mapping,time,iteration" > results-funmap-basic-sdmrdfizer.csv
## Running SDM-RDFizer+Functions experiments
echo "dataset,mapping,time,iteration" > results-sdmrdfizer.csv


echo "---------Running experiments over SDM-RDFizer------------"

for mapping in "${mappings[@]}"
do    
        for data in "${dataArray[@]}"
        do
                echo "Running experiment $mapping and $data"
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
                        echo "$data,$mapping,$dur,$i" >> results-funmap-sdmrdfizer.csv
                        

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
                        echo "$data,$mapping,$dur,$i" >> results-funmap-basic-sdmrdfizer.csv

        		########################################################################################
                        #################### Running SDM-RDFizer+Functions experiments #########################
                        ########################################################################################
        		echo "SDM-RDFizer: iteration $i"
                        start=$(data +%s.%N)
        		python3 ./SDM-RDFizer-Functions/rdfizer/run_rdfizer.py config-SDM-function.ini
        		dur=$(echo "$(date +%s.%N) - $start" | bc)
        		echo "$data,$mapping,$dur,$i" >> results-sdmrdfizer.csv
        		
        	done
        done
done

rm data.csv
rm maping.ttl



