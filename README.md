# Prepation of the environment

## Libraries
- Java - openjdk v1.8.0_265
- Docker - v19.03.7
- Docker-compose - v1.23.1
- Node - v12.18.3
- Python - v3.7
- Anaconda - (https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh)

## Bash commands
- bc
- wget

## Machine requirements
Ubuntu 16.04 with Intel(R) Xeon(R) Platinum 8160, CPU 2.10GHz and 700Gb RAM.


# Experiments

## Research questions
1. What is the impact of data duplication rate in the execution time of a knowledge graph creation approach? 
2. What is the impact of different types of complexity over transformation functions during a knowledge graph creation process? 
3. How does the repetition of a same function in different mappings affect the existing RML engines?
4. What is the impact of relational data sources in the knowledge graph creation process?

## Data
To the best of our knowledge, there are no testbeds to evaluate the performance of a knowledge graph construction approach that applies functional mappings. Consequently, following the real-world scenario that initially motivated this research, we create our testbed from the biomedical domain. We generate a baseline dataset by randomly selecting 20,000 records from the coding point mutation dataset in [COSMIC](https://cancer.sanger.ac.uk/cosmic) GRCh37, version90, released August 2019 database. We keep all 39 attributes of the original dataset in the baseline dataset, while only five to seven of them are utilized in mappings. In total, four different mapping files are generated consisting of one __FunctionMap__ and four, six, eight, or ten __TriplesMaps__ with a __predicateObjectMap__ linked to the function. To additionally validate FunMap in case of large-sized data, we create another dataset following the same criteria, with 4,000,000 records and the size of about 1.3GB.

## Engines
The baselines of our study are three different open source RML-complaint engines that are able to execute RML+FnO mappings and have been extensively utilized in multiple applications and tested by the community: 
1. SDM-RDFizer v3.0 (named SDM-RDFizer\*\*(RML+FnO))
2. RMLMapper v4.7 (named RMLMapper\*\*(RML+FnO))
3. RocketRML v1.6. (named RocketRML\*\*(RML+FnO). 

In order to evaluate the impact of transformation rules, we implement FunMap v1.0 on the top of the aforementioned engines with DTR2 optimization as an optional parameter. We refer to the approach which applies FunMap excluding DTR2 as FunMap<sup>-</sup> (in the experiment scripts and results it will appear as FunMap-Basic. The combination of each configurations are:
1. FunMap+SDM-RDFizer
2. FunMap+RMLMapper
3. FunMap+RocketRML
4. FunMap<sup>-</sup>+SDM-RDFizer 
5. FunMap<sup>-</sup>+RMLMapper
6. FunMap<sup>-</sup>+RocketRML


## Metrics
Elapsed time spent by an engine to complete the creation of a knowledge graph and also counts FunMap pre-processing; it is measured as the absolute wall-clock system time as reported by the **time** command of the Linux operating system. Each experiment was executed five times and average is reported.


## Setups
Based on our research questions, we set up in overall 198 experiments as the combinations of the following scenarios. We create two datasets from our baseline with 25% and 75% duplicates which means in the 25% duplicate dataset, 25% and in the 75% duplicate dataset, 75% of the records are duplicated. Additionally, two functions with different levels of complexity are created. We describe the complexity level of the functions based on the number of required input attributes and operations to be performed. Accordingly, "simple" function is defined to receive one input attribute and perform one operation, while a "complex" function receives two input attributes and completes five operations. In total, we create eight mapping files including four, six, eight, and ten **TriplesMap** and one **FunctionMap** to be either "simple" or  "complex". Additionally, six experiments using 75% duplicate datasets of 20,000 and 4,000,000 records and a mapping file including ten complex functions are set up in order to be run over a relational database (RDB) implemented in MySQL 8.0.   

## How to reproduce it?

Follow this steps to reproduce the experiments shown in the paper:

1) Go to RDB-Preparation folder and following the instructions in README.md file to prepare the RDBs.
2) Go to the folder of each engine and read the instructions in each README.md file to execute the experiments.
