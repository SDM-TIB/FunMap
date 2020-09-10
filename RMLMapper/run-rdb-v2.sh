# /bin/bash

############################# Running over 20k-records dataset ##############################
echo "---------Experiments over RDB with RMLMapper---------"

## mappings to be applied in the experiments
cp ./mappings/complex_sameFunction10_RDB.ttl mapping.ttl

## create result files
echo "dataset,mapping,time,iteration" > results-rdb-funmap-rmlmapper.csv
echo "dataset,mapping,time,iteration" > results-rdb-rmlmapper.csv


echo "Running experiment complex_sameFunction10_RDB.ttl"

for i in 1 2 3 4 5
do
	echo "FunMap+RMLMapper over RDB: iteration $i"
	start=$(date +%s.%N)
	## Running FunMap:
	python3 ./FunMap/run_translator.py config_rdb.ini
	## Running RMLMapper over the results:
	java -jar rmlmapper.jar -m mappings/transfered_mapping_joinInQuery_rmlmapper.ttl -o output.nt
	dur=$(echo "$(date +%s.%N) - $start" | bc)
	echo "veracity75,complex_sameFunction10_RDB.ttl,$dur,$i"  >> results-rdb-funmap-rmlmapper.csv

	echo "RMLMapper over RDB: iteration $i"
	start=$(date +%s.%N)
	java -jar rmlmapper.jar -m mapping.ttl -f functions_complex.ttl -o output-rdb.nt -d
	dur=$(echo "$(date +%s.%N) - $start" | bc)
	echo "veracity75.csv,complex_sameFunction10_RDB.ttl,$dur,$i"  >> results-rdb-rmlmapper.csv
done


rm mapping.ttl

