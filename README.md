# Online appendix to: Optimizing Navigational Graph Queries
This repository functions as an online appendix to the paper titled "Optimizing Navigational Graph Queries".

# Contents
+ the `queries` directory contains the exact set of queries used in experiments, subdivided into
  - the `sql` directory which contains SQL specifications for the query templates
  - the `sparql` directory which contains SPARQL specifications for the query templates (excluding the Regular Query)
  - the `dbpedia_instances.csv` file which specifies the values for edge labels and filter constants for the queries on DBPedia
  - the `string_instances.csv` file which specifies the values for edge labels and filter constants for the queries on StringDB
  - the `generate.py` file which can be run (run instructions in its comments) to substitute values from the instance files into the query templates to generate concrete queries in the `generated` directory
+ the `Enumeration Rules.pdf` file which specifies the enumeration rules not discussed in the paper
+ this `readme`
  
