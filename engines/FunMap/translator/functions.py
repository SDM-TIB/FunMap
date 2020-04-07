import re
import csv
import sys
import os


# returns a string in lower case
def tolower(value):
    return value.lower()


# return a string in upper case
def toupper(value):
    return value.upper()


# return a string in title case
def totitle(value):
    return value.title()


# return a string after removing leading and trailing whitespaces
def trim(value):
    return value.strip()


# return a string without s2
def chomp(value, toremove):
    return value.replace(toremove, '')


#return the substring (index2 can be null, index2 can be negative value)
def substring(value, index1, index2):
    if index2 is None:
        return value[int(index1):]
    else:
        return value[int(index1):int(index2)]


#replace value2 by value3
def replaceValue(value, value2, value3):
    return value.replace(value2, value3)


#returns the first appearance of the regex in value
def match(value, regex):
    return re.match(regex, value)[0]


def variantIdentifier(column1, column2,prefix):
    value = ""
    if (str(column1) != "" and str(column1) != " "):
        value = re.sub('_.*','',str(column2))+"_"+str(column1).split(".")[1].replace(">", "~")
        value = prefix+value
    return value

def prefix_extraction(uri):
    prefix = ""
    url = ""
    value = ""
    if "#" in uri:
        if "ru" in uri:
            prefix = "ru"
        elif "rdf-schema" in uri:
            prefix = "rdfs"
        elif "rdf-syntax-ns" in uri:
            prefix = "rdf"
        elif "rev" in uri:
            prefix = "rev"
        elif "owl" in uri:
            prefix = "owl"
        elif "fnml" in uri:
            prefix = "fnml"
        elif "function" in uri:
            prefix = "fno"
        elif "XML" in uri:
            prefix = "xsd"
        url, value = uri.split("#")[0]+"#", uri.split("#")[1]
    else:
        if "resource" in uri:
            prefix = "sio"
        elif "af" in uri:
            prefix = "af"
        elif "example" in uri:
            prefix = "ex"
        elif "term" in uri:
            prefix = "dcterms"
        elif "elements" in uri:
            prefix = "dce"
        elif "iasis" in uri:
            prefix = "iasis"
        else:
            prefix = uri.split("/")[len(uri.split("/"))-2]
        value = uri.split("/")[len(uri.split("/"))-1]
        char = ""
        temp = ""
        temp_string = uri
        while char != "/":
            temp = temp_string
            temp_string = temp_string[:-1]
            char = temp[len(temp)-1]
        url = temp
    return prefix, url, value

def update_mapping(triple_maps, dic, output, original, join):
    mapping = ""
    for triples_map in triple_maps:

        if triples_map.function:
            pass
        else:
            if "#" in triples_map.triples_map_id:
                mapping += "<#" + triples_map.triples_map_id.split("#")[1] + ">\n"
            else: 
                mapping += "<#" + triples_map.triples_map_id + ">\n"

            mapping += "    a rr:TriplesMap;\n"

            mapping += "    rml:logicalSource [ rml:source \"" + triples_map.data_source +"\";\n"
            if str(triples_map.file_format).lower() == "csv" and triples_map.query == "None": 
                mapping += "                rml:referenceFormulation ql:CSV\n" 
            mapping += "                ];\n"

            
            mapping += "    rr:subjectMap [\n"
            if triples_map.subject_map.subject_mapping_type is "template":
                mapping += "        rr:template \"" + triples_map.subject_map.value + "\";\n"
            elif triples_map.subject_map.subject_mapping_type is "reference":
                mapping += "        rml:reference " + triples_map.subject_map.value + ";\n"
            elif triples_map.subject_map.subject_mapping_type is "constant":
                mapping += "        rr:constant " + triples_map.subject_map.value + ";\n"
            elif triples_map.subject_map.subject_mapping_type is "function":
                mapping = mapping[:-2]
                mapping += "<" + triples_map.subject_map.value + ">;\n"
            if triples_map.subject_map.rdf_class is not None:
                prefix, url, value = prefix_extraction(triples_map.subject_map.rdf_class)
                mapping += "        rr:class " + prefix + ":" + value  + "\n"
            mapping += "    ];\n"

            for predicate_object in triples_map.predicate_object_maps_list:
                
                mapping += "    rr:predicateObjectMap [\n"
                if "constant" in predicate_object.predicate_map.mapping_type :
                    prefix, url, value = prefix_extraction(predicate_object.predicate_map.value)
                    mapping += "        rr:predicate " + prefix + ":" + value + ";\n"
                elif "constant shortcut" in predicate_object.predicate_map.mapping_type:
                    prefix, url, value = prefix_extraction(predicate_object.predicate_map.value)
                    mapping += "        rr:predicate " + prefix + ":" + value + ";\n"
                elif "template" in predicate_object.predicate_map.mapping_type:
                    mapping += "        rr:predicateMap[\n"
                    mapping += "            rr:template \"" + predicate_object.predicate_map.value + "\"\n"  
                    mapping += "        ];\n"
                elif "reference" in predicate_object.predicate_map.mapping_type:
                    mapping += "        rr:predicateMap[\n"
                    mapping += "            rml:reference \"" + predicate_object.predicate_map.value + "\"\n" 
                    mapping += "        ];\n"

                mapping += "        rr:objectMap "
                if "constant" in predicate_object.object_map.mapping_type:
                    mapping += "[\n"
                    mapping += "        rr:constant \"" + predicate_object.object_map.value + "\"\n"
                    mapping += "        ]\n"
                elif "template" in predicate_object.object_map.mapping_type:
                    mapping += "[\n"
                    mapping += "        rr:template  \"" + predicate_object.object_map.value + "\"\n"
                    mapping += "        ]\n"
                elif "reference" == predicate_object.object_map.mapping_type:
                    mapping += "[\n"
                    mapping += "        rml:reference \"" + predicate_object.object_map.value + "\"\n"
                    mapping += "        ]\n"
                elif "parent triples map function" in predicate_object.object_map.mapping_type:
                    mapping += "[\n"
                    mapping += "        rr:parentTriplesMap <" + predicate_object.object_map.value + ">;\n"
                    mapping += "        rr:joinCondition [\n"
                    mapping += "            rr:child <" + predicate_object.object_map.child + ">;\n"
                    mapping += "            rr:parent <" + predicate_object.object_map.parent + ">;\n"
                    mapping += "        ]\n"
                elif "parent triples map parent function" in predicate_object.object_map.mapping_type:
                    mapping += "[\n"
                    mapping += "        rr:parentTriplesMap <" + predicate_object.object_map.value + ">;\n"
                    mapping += "        rr:joinCondition [\n"
                    mapping += "            rr:child \"" + predicate_object.object_map.child + "\";\n"
                    mapping += "            rr:parent <" + predicate_object.object_map.parent + ">;\n"
                    mapping += "        ]\n"
                elif "parent triples map child function" in predicate_object.object_map.mapping_type:
                    mapping += "[\n"
                    mapping += "        rr:parentTriplesMap <" + predicate_object.object_map.value + ">;\n"
                    mapping += "        rr:joinCondition [\n"
                    mapping += "            rr:child \"" + predicate_object.object_map.child + "\";\n"
                    mapping += "            rr:parent <" + predicate_object.object_map.parent + ">;\n"
                    mapping += "        ]\n"
                elif "parent triples map" in predicate_object.object_map.mapping_type:
                    mapping += "[\n"
                    mapping += "        rr:parentTriplesMap <" + predicate_object.object_map.value + ">\n"
                    if (predicate_object.object_map.child is not None) and (predicate_object.object_map.parent is not None):
                        mapping = mapping[:-1]
                        mapping += ";\n"
                        mapping += "        rr:joinCondition [\n"
                        mapping += "            rr:child \"" + predicate_object.object_map.child + "\";\n"
                        mapping += "            rr:parent \"" + predicate_object.object_map.parent + "\";\n"
                        mapping += "        ]\n"
                    mapping += "        ]\n"
                elif "constant shortcut" in predicate_object.object_map.mapping_type:
                    mapping += "[\n"
                    mapping += "        rr:constant \"" + predicate_object.object_map.value + "\"\n"
                    mapping += "        ]\n"
                elif "reference function" in predicate_object.object_map.mapping_type:
                    if join:
                        mapping += "[\n"
                        mapping += "        rr:parentTriplesMap <#" + dic[predicate_object.object_map.value]["output_name"] + ">;\n"
                        for attr in dic[predicate_object.object_map.value]["inputs"]:
                            if attr[1] is not "constant":
                                mapping += "        rr:joinCondition [\n"
                                mapping += "            rr:child \"" + attr[0] + "\";\n"
                                mapping += "            rr:parent \"" + attr[0] +"\";\n"
                                mapping += "            ];\n"
                        mapping += "        ];\n"
                    else:
                        mapping += "[\n"
                        mapping += "        rml:reference \"" + dic[predicate_object.object_map.value]["output_name"] + "\";\n"
                        mapping += "        ];\n"
                mapping += "    ];\n"
            if triples_map.function:
                pass
            else:
                mapping = mapping[:-2]
                mapping += ".\n\n"

    if join:
        for function in dic.keys():
            mapping += "<#" + dic[function]["output_name"] + ">\n"
            mapping += "    a rr:TriplesMap;\n"
            mapping += "    rml:logicalSource [ rml:source \"" + dic[function]["output_file"] +"\";\n"
            if "csv" in dic[function]["output_file"]:
                mapping += "                rml:referenceFormulation ql:CSV\n" 
            mapping += "            ];\n"
            mapping += "    rr:subjectMap [\n"
            if dic[function]["termType"]:
                mapping += "        rr:template \"" + dic[function]["output_name"] + "\"\n"
            else:
                mapping += "        rml:reference \"" + dic[function]["output_name"] + "\"\n"
            mapping += "    ].\n\n"

    prefix_string = ""
    
    f = open(original,"r")
    original_mapping = f.readlines()
    for prefix in original_mapping:
        if ("prefix" in prefix) or ("base" in prefix):
           prefix_string += prefix
        else:
            break
    f.close()  

    prefix_string += "\n"
    prefix_string += mapping

    mapping_file = open(output + "/transfered_mapping.ttl","w")
    mapping_file.write(prefix_string)
    mapping_file.close()

def execute_function(row,dic):
    if "tolower" in dic["function"]:
        return tolower(row[dic["func_par"]["value"]])
    elif "toupper" in dic["function"]:
        return toupper(row[dic["func_par"]["value"]])
    elif "totitle" in dic["function"]:
        return totitle(row[dic["func_par"]["value"]])
    elif "trim" in dic["function"]:
        return trim(row[dic["func_par"]["value"]])
    elif "chomp" in dic["function"]:
        return chomp(row[dic["func_par"]["value"]],dic["func_par"]["toremove"])
    elif "substring" in dic["function"]:
        if "index2" in dic["func_par"].keys():
            return substring(row[dic["func_par"]["value"]],dic["func_par"]["index1"],dic["func_par"]["index2"])
        else:
            return substring(row[dic["func_par"]["value"]],dic["func_par"]["index1"],None)
    elif "replaceValue" in dic["function"]:
        return replaceValue(row[dic["func_par"]["value"]],dic["func_par"]["value2"],dic["func_par"]["value3"])
    elif "match" in dic["function"]:
        return match(dic["func_par"]["regex"],row[dic["func_par"]["value"]])
    elif "variantIdentifier" in dic["function"]:
        return variantIdentifier(dic["func_par"]["column1"],dic["func_par"]["column2"],dic["func_par"]["prefix"])
    else:
        print("Invalid function")
        print("Aborting...")
        sys.exit(1)

def join_csv(source, dic, output):
    with open(source, "r") as source_csv:
        with open(output + "/" + dic["output_name"] + ".csv", "w") as temp_csv:
            writer = csv.writer(temp_csv, quoting=csv.QUOTE_ALL)
            reader = csv.DictReader(source_csv, delimiter=',')

            keys = []
            for attr in dic["inputs"]:
                if attr[1] is not "constant":
                    keys.append(attr[0])
            keys.append(dic["output_name"])
            writer.writerow(keys)

            values = {}
            if "variantIdentifier" in dic["function"]:
                for row in reader:
                    if (row[dic["func_par"]["column1"]]+row[dic["func_par"]["column2"]] not in values) and (row[dic["func_par"]["column1"]]+row[dic["func_par"]["column2"]] is not ''):
                        value = execute_function(row,dic)
                        line = []
                        for attr in dic["inputs"]:
                            if attr[1] is not "constant":
                                line.append(row[attr[0]])
                        line.append(value)
                        writer.writerow(line)
                        values[row[dic["func_par"]["column1"]]+row[dic["func_par"]["column2"]]] = value
            else: 
                for row in reader:
                    if (row[dic["func_par"]["value"]] not in values) and (row[dic["func_par"]["value"]] is not ''):
                        value = execute_function(row,dic)
                        line = []
                        for attr in dic["inputs"]:
                            if attr[1] is not "constant":
                                line.append(row[attr[0]])
                        line.append(value)
                        writer.writerow(line)
                        values[row[dic["func_par"]["value"]]] = value

def join_csv_URI(source, dic, output):
    with open(source, "r") as source_csv:
        with open(output + "/" + dic["output_name"] + ".csv", "w") as temp_csv:
            writer = csv.writer(temp_csv, quoting=csv.QUOTE_ALL)
            reader = csv.DictReader(source_csv, delimiter=',')

            keys = []
            for attr in dic["inputs"]:
                if attr[1] is not "constant":
                    keys.append(attr[0])
            keys.append(dic["output_name"])
            writer.writerow(keys)

            values = {}
            if "variantIdentifier" in dic["function"]:
                for row in reader:
                    if (row[dic["func_par"]["column1"]]+row[dic["func_par"]["column2"]] not in values) and (row[dic["func_par"]["column1"]]+row[dic["func_par"]["column2"]] is not ''):
                        value = "<" + execute_function(row,dic) + ">"
                        line = []
                        for attr in dic["inputs"]:
                            if attr[1] is not "constant":
                                line.append(row[attr[0]])
                        line.append(value)
                        writer.writerow(line)
                        values[row[dic["func_par"]["column1"]]+row[dic["func_par"]["column2"]]] = value
            else: 
                for row in reader:
                    if (row[dic["func_par"]["value"]] not in values) and (row[dic["func_par"]["value"]] is not ''):
                        value = "<" + execute_function(row,dic) + ">"
                        line = []
                        for attr in dic["inputs"]:
                            if attr[1] is not "constant":
                                line.append(row[attr[0]])
                        line.append(value)
                        writer.writerow(line)
                        values[row[dic["func_par"]["value"]]] = value


def create_dictionary(triple_map):
    dic = {}
    inputs = []
    for tp in triple_map.predicate_object_maps_list:
        if "#" in tp.predicate_map.value:
            key = tp.predicate_map.value.split("#")[1]
            tp_type = tp.predicate_map.mapping_type
        elif "/" in tp.predicate_map.value:
            key = tp.predicate_map.value.split("/")[len(tp.predicate_map.value.split("/"))-1]
            tp_type = tp.predicate_map.mapping_type
        if "#" in tp.object_map.value:
            value = tp.object_map.value.split("#")[1]
            tp_type = tp.object_map.mapping_type
        elif "/" in tp.object_map.value:
            value = tp.object_map.value.split("/")[len(tp.object_map.value.split("/"))-1]
            tp_type = tp.object_map.mapping_type
        else:
            value = tp.object_map.value
            tp_type = tp.object_map.mapping_type

        dic.update({key : value})
        if (key != "executes") and ([value,tp_type] not in inputs):
            inputs.append([value,tp_type])
    dic["inputs"] = inputs
    return dic