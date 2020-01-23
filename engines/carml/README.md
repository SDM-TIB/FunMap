# How to run CARML with RML+FnO?


1. Create your mapping document following RML+FnO specification (example in the folder)
	1. Issue 1: The URI for the FnO needs to be: http://semweb.datasciencelab.be/ns/function#
	1. Issue 2: The fnml:functionValue needs to explicit declare a rr:subjectMap (empty rr:template is enough)
2. Implement your functions in the java class "Functions"
3. Put mapping and data in the root folder
4. Run:
```bash
mvn assembly:assembly -DdescriptorId=jar-with-dependencies
cp target/carml-cli-1.0.0-jar-with-dependencies.jar ./carml-cli-1.0.0.jar
java -cp .:carml-cli-1.0.0.jar:rdf4j-rio-ntriples-2.3.2.jar es.upm.fi.dia.oeg.CarmlCli
```
