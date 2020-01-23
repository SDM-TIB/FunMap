# How to run RMLMapper with RML+FnO?


1) Create your mapping document following RML+FnO specification (example in the folder)
2) Define your functions following the FnO in a functions.ttl file similar as it is shown in the example file.
3) Implement your functions in Java and create a .jar file
4) Download the last version of RMLMapper from https://github.com/RMLio/rmlmapper-java/releases/ and run:
```bash
java -jar rmlmapper.jar -m mapping.rml.ttl -o output.nt -d -f functions.ttl
```

For more info visit: https://github.com/RMLio/rmlmapper-java