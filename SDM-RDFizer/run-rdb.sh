# /bin/bash

############################# Running arrays ##############################
echo "---------Experiments over RDB with SDM-RDFizer (note that experiments with complex_sameFunction10_RDB_5millionRecords.ttl could not finish in SDM-RDFizer configuration---------"

declare -a mappings=("complex_sameFunction10_RDB.ttl" "complex_sameFunction10_RDB_5millionRecords.ttl")

## create result files
echo "mapping,time,iteration" > complete-results-rdb-funmap-sdmrdfizer.csv
echo "mapping,time,iteration" > complete-results-rdb-sdmrdfizer.csv

echo "mapping,time" > results-rdb-funmap-sdmrdfizer.csv
echo "mapping,time" > results-rdb-sdmrdfizer.csv

sed -i 's/db: largeData/db: funmap/g' config-rdb-funmap.ini	
sed -i 's/db: largeData/db: funmap/g' config-rdb-SDM.ini	

########################################################################################
#################### Running FunMap+SDM-RDFizer experiments ############################
########################################################################################
echo "---------Running FunMap with SDM-RDFizer---------"
for mapping in "${mappings[@]}"
do
	cp ./mappings/$mapping mapping.ttl
	echo "Running experiment $mapping"
	total=0
	for i in 1 2 3 4 5
	do
		echo "FunMap+SDM-RDFizer over RDB: iteration $i"
		start=$(date +%s.%N)
		## Running FunMap:
		python3 ./FunMap/run_translator.py config-rdb-funmap.ini
		## Running SDM-RDFizer over the results:
		python3 ./SDM-RDFizer/rdfizer/run_rdfizer.py config-rdb-SDM.ini
		dur=$(echo "$(date +%s.%N) - $start" | bc)
		total=$(echo "$total+$dur" | bc)
		echo "$mapping,$dur,$i"  >> complete-results-rdb-funmap-sdmrdfizer.csv
	done
	total=$(echo "$total/5" | bc -l)
	echo "$mapping,$total"  >> results-rdb-funmap-sdmrdfizer.csv
	sed -i 's/db: funmap/db: largeData/g' config-rdb-funmap.ini
	sed -i 's/db: funmap/db: largeData/g' config-rdb-SDM.ini
done

sed -i 's/db: largeData/db: funmap/g' config-rdb-funmap.ini	
sed -i 's/db: largeData/db: funmap/g' config-rdb-SDM.ini	
sed -i 's/db: largeData/db: funmap/g' config-rdb-SDM-function.ini
########################################################################################
#################### Running SDM-RDFizer+Functions experiments #########################
########################################################################################
echo "---------Running SDM-RDFizer---------"
for mapping in "${mappings[@]}"
do
	cp ./mappings/$mapping mapping.ttl
	echo "Running experiment $mapping"
	total=0
	for i in 1 2 3 4 5
	do
		echo "SDM-RDFizer over RDB: itearion $i"
		start=$(date +%s.%N)
		python3 ./SDM-RDFizer-Functions/rdfizer/run_rdfizer.py config-rdb-SDM-function.ini
		dur=$(echo "$(date +%s.%N) - $start" | bc)
		echo "$mapping,$dur,$i"  >> complete-results-rdb-sdmrdfizer.csv
		total=$(echo "$total+$dur" | bc)
	done
	total=$(echo "$total/5" | bc -l)
	echo "$mapping,$total"  >> results-rdb-sdmrdfizer.csv
	sed -i 's/db: funmap/db: largeData/g' config-rdb-SDM-function.ini
done
rm mapping.ttl
sed -i 's/db: largeData/db: funmap/g' config-rdb-SDM-function.ini

