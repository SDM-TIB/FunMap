# create databases

DROP DATABASE IF EXISTS `largeData`;
CREATE DATABASE IF NOT EXISTS `largeData`;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
GRANT FILE ON *.* TO 'root'@'%';
SET GLOBAL local_infile = 'ON';
USE `largeData`;
DROP TABLE IF EXISTS data;
CREATE TABLE data (`Gene name` VARCHAR(200),`Accession Number` VARCHAR(200),`Gene CDS length` VARCHAR(200),`HGNC ID` VARCHAR(200),`Sample name` VARCHAR(200),`ID_sample` VARCHAR(200),`ID_tumour` VARCHAR(200),`Primary site` VARCHAR(200),`Site subtype 1` VARCHAR(200),`Site subtype 2` VARCHAR(200),`Site subtype 3` VARCHAR(200),`Primary histology` VARCHAR(200),`Histology subtype 1` VARCHAR(200),`Histology subtype 2` VARCHAR(200),`Histology subtype 3` VARCHAR(200),`Genome-wide screen` VARCHAR(200),`GENOMIC_MUTATION_ID` VARCHAR(200),`LEGACY_MUTATION_ID` VARCHAR(200),`MUTATION_ID` VARCHAR(200),`Mutation CDS` VARCHAR(200),`Mutation AA` VARCHAR(200),`Mutation Description` VARCHAR(200),`Mutation zygosity` VARCHAR(200),`LOH` VARCHAR(200),`GRCh` VARCHAR(200),`Mutation genome position` VARCHAR(200),`Mutation strand` VARCHAR(200),`SNP` VARCHAR(200),`Resistance Mutation` VARCHAR(200),`FATHMM prediction` VARCHAR(200),`FATHMM score` VARCHAR(200),`Mutation somatic status` VARCHAR(200),`Pubmed_PMID` VARCHAR(200),`ID_STUDY` VARCHAR(200),`Sample Type` VARCHAR(200),`Tumour origin` VARCHAR(200),`Age` VARCHAR(200),`cFormat` VARCHAR(200),`pFormat` VARCHAR(200));
DROP TABLE IF EXISTS PROJECT1;
CREATE TABLE PROJECT1 (`Gene name` VARCHAR(200),`Mutation CDS` VARCHAR(200));
DROP TABLE IF EXISTS PROJECT2;
CREATE TABLE PROJECT2 (`Gene name` VARCHAR(200),`Mutation CDS` VARCHAR(200),`cFormat` VARCHAR(200));
DROP TABLE IF EXISTS PROJECT3;
CREATE TABLE PROJECT3 (`Gene name` VARCHAR(200),`Mutation CDS` VARCHAR(200));
DROP TABLE IF EXISTS PROJECT4;
CREATE TABLE PROJECT4 (`Gene name` VARCHAR(200),`Mutation CDS` VARCHAR(200),`GENOMIC_MUTATION_ID` VARCHAR(200));
DROP TABLE IF EXISTS PROJECT5;
CREATE TABLE PROJECT5 (`Gene name` VARCHAR(200),`Primary site` VARCHAR(200),`Mutation CDS` VARCHAR(200));
DROP TABLE IF EXISTS PROJECT6;
CREATE TABLE PROJECT6 (`Gene name` VARCHAR(200),`Mutation CDS` VARCHAR(200));
DROP TABLE IF EXISTS PROJECT7;
CREATE TABLE PROJECT7 (`Gene name` VARCHAR(200),`Primary site` VARCHAR(200),`Mutation CDS` VARCHAR(200));
DROP TABLE IF EXISTS PROJECT8;
CREATE TABLE PROJECT8 (`Gene name` VARCHAR(200),`Mutation CDS` VARCHAR(200));
DROP TABLE IF EXISTS PROJECT9;
CREATE TABLE PROJECT9 (`Gene name` VARCHAR(200),`Mutation CDS` VARCHAR(200),`cFormat` VARCHAR(200));
DROP TABLE IF EXISTS PROJECT10;
CREATE TABLE PROJECT10 (`Gene name` VARCHAR(200),`Primary site` VARCHAR(200),`Mutation CDS` VARCHAR(200),`GENOMIC_MUTATION_ID` VARCHAR(200));
DROP TABLE IF EXISTS OUTPUT1;
CREATE TABLE OUTPUT1 (`Gene name` VARCHAR(200),`Mutation CDS` VARCHAR(200),`OUTPUT1` VARCHAR(200));

LOAD DATA LOCAL INFILE '/data/5millionRecords_veracity75.csv' INTO TABLE data FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
INSERT INTO PROJECT1 SELECT `Gene name`, `Mutation CDS` FROM data;
INSERT INTO PROJECT2 SELECT `Gene name`, `Mutation CDS`, `cFormat` FROM data;
INSERT INTO PROJECT3 SELECT `Gene name`, `Mutation CDS` FROM data;
INSERT INTO PROJECT4 SELECT `Gene name`, `Mutation CDS`, `GENOMIC_MUTATION_ID` FROM data; 
INSERT INTO PROJECT5 SELECT `Gene name`, `Primary site`, `Mutation CDS` FROM data;
INSERT INTO PROJECT6 SELECT `Gene name`, `Mutation CDS` FROM data;
INSERT INTO PROJECT7 SELECT `Gene name`, `Primary site`, `Mutation CDS` FROM data;
INSERT INTO PROJECT8 SELECT `Gene name`, `Mutation CDS` FROM data;
INSERT INTO PROJECT9 SELECT `Gene name`, `Mutation CDS`, `cFormat` FROM data;
INSERT INTO PROJECT10 SELECT `Gene name`, `Primary site`, `Mutation CDS` FROM data;
INSERT INTO OUTPUT1 SELECT `Gene name`, `Mutation CDS`, `OUTPUT1` FROM data;


