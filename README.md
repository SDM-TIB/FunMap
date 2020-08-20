# FunMap: Functional Mappings for Scaled-Up Knowledge Graph Creation

We present FunMap, an interpreter of RML+FnO,that converts a data integration system defined using RML+FnO into an equivalent data integration system where RML mappings are function-free. FunMap resembles existing mapping translation proposals and empowers the  knowledge  graph  creation  process  with  optimization  techniques  to  reduce execution  time.  Transformations  of  data  sources  include  the  projection  of  the attributes used in the RML+FnO mappings. They are supported on well-known properties of the relational algebra, e.g., the pushing down of projections and selections into the data sources, and enable not only the reduction of the size of  data  sources  but  also  the  elimination  of  duplicates.  Additionally,  FunMap materializes  functions  –expressed  in  FnO–  and  represents  the  results  as  data sources of the generated data integration system; the translation of RML+FnO into RML mappings that integrate the materialization of functions is performed by means of joins between the generated RML mappings. 

![FunMap-workflow](images/architecture.png?raw=true "FunMap-workflow")


## ISWC experiments

Data Folder: CSV and RDB used for the experiments. RDB provide a docker compose to create automatically the databases
Mappings folder: mappings for FunMap (CSV and RDB), RocketRML (CSV), RMLMapper (CSV and RDB) and SDM-RDFizer (CSV and RDB)
Engines folder: FunMap, RocketRML, RMLMapper and SDM-RDFizer docker images to run the experiments

