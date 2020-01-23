# How to run RocketRML with RML+FnO?

1. Create your mapping document following RML+FnO specification (example in the folder)
	1. Issue: no empty prefix are allowed (:s_0) in the mapping
2. Implement your functions in the javascript file "index.js"
3. Edit inputFiles variables at "index.js" with your datasources
4. Install rocketrml with npm (npm install rocketrml) and fs (npm install fs)
5. Run:
```bash
node index.js
```
