# FunMap: Functional Mappings for Scaled-Up Knowledge Graph Creation

We present FunMap, an interpreter of RML+FnO,that converts a data integration system defined using RML+FnO into an equivalent data integration system where RML mappings are function-free. FunMap resembles existing mapping translation proposals and empowers the  knowledge  graph  creation  process  with  optimization  techniques  to  reduce execution  time.  Transformations  of  data  sources  include  the  projection  of  the attributes used in the RML+FnO mappings. They are supported on well-known properties of the relational algebra, e.g., the pushing down of projections and selections into the data sources, and enable not only the reduction of the size of  data  sources  but  also  the  elimination  of  duplicates.  Additionally,  FunMap materializes  functions  –expressed  in  FnO–  and  represents  the  results  as  data sources of the generated data integration system; the translation of RML+FnO into RML mappings that integrate the materialization of functions is performed by means of joins between the generated RML mappings. 

![FunMap-workflow](images/architecture.png?raw=true "FunMap-workflow")


## How to run FunMap?

### Configuration file
```
[default]
main_directory: / 

[datasets]
number_of_datasets: 1
name: funmap # name of dataset
output_folder: ${default:main_directory}results/ # path of results
enrichment: yes # yes executes FunMap, no executes FunMap- (without projections)
dbType: mysql # only for RDB instance

[dataset1]
name: funmap
mapping: ${default:main_directory}mappings/mapping.ttl # mapping path
user: user # only for RDB, user to access DB
password: pass # only for RDB, password to access DB
host: 127.0.0.1 # only for RDB, host to access DB
port: 3306 # only for RDB, port to access DB
db: dbName # only for RDB, database name 
```




### Run with Docker 
```
# Preparation
docker build -t funmap .

# For CSV files
docker-compose up -d
# If your sources are CSV files, the path of the files has to be: /data/nameOfTheFile.csv.
cp csvFiles.csv data/
cp mapping.ttl mappings/

# For RDB instance
mkdir sql
cp sqlScript.sql sql/
docker-compose up -d 
cp mapping.ttl mappings/

# Execution
docker exec -it funmap python3 /funmap/run_translator.py /funmap/config[_rdb].ini
```

### Run with Python3
```
pip install -r requirements.txt
python3 run_translator.py config[_rdb].ini
```

## Authors

- Samaneh Jozashoori (samaneh.jozashoori@tib.eu)
- David Chaves-Fraga (dchaves@fi.upm.es)
- Enrique Iglesias ( s6enigle@uni-bonn.de)
- Oscar Corcho (ocorcho@fi.upm.es)
- Maria-Esther Vidal (maria.vidal@tib.eu)
