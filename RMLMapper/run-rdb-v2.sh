# /bin/bash

############################# Running over 20k-records dataset ##############################

## mappings to be applied in the experiments
cp ./mappings/complex_sameFunction10_RDB.ttl mapping.ttl

## create result files
echo "dataset,mapping,time,iteration" > results-rdb-FunMap-rmlmapper.csv
echo "dataset,mapping,time,iteration" > results-rdb-rmlmapper.csv

########################################################################################
#################### Running FunMap+RMLMapper experiments ############################
########################################################################################
echo "---------Running FunMap with RMLMapper over RDB and complex functions---------"

for i in 1 2 3 4 5
do
	echo "---------Running iteration $i---------"
	start=$(date +%s.%N)
	## Running FunMap:
	python3 ./FunMap/run_translator.py config_rdb.ini
	## Running RMLMapper over the results:
	java -jar rmlmapper.jar -m mappings/transfered_mapping_joinInQuery_rmlmapper.ttl -o output.nt
	dur=$(echo "$(date +%s.%N) - $start" | bc)
	echo "veracity75.csv,complex_sameFunction10_RDB.ttl,$dur,$i"  >> results-rdb-FunMap-rmlmapper.csv
done


########################################################################################
#################### Running RMLMapper+Functions experiments #########################
########################################################################################
echo "---------Running RMLMapper over RDB and complex functions---------"

for i in 1 2 3 4 5
do
	echo "---------Running iteration $i---------"
	start=$(date +%s.%N)
	java -jar rmlmapper.jar -m mapping.ttl -f functions_complex.ttl -o output-rdb.nt -d
	dur=$(echo "$(date +%s.%N) - $start" | bc)
	echo "veracity75.csv,complex_sameFunction10_RDB.ttl,$dur,$i"  >> results-rdb-rmlmapper.csv
done

