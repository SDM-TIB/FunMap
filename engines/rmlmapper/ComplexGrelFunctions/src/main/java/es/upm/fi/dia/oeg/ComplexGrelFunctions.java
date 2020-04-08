package es.upm.fi.dia.oeg;

/**
 * Hello world!
 *
 */
public class ComplexGrelFunctions
{
    public static String string_replace(String value, String find, String replace){
        return value.replace(find,replace);
    }

    public static String variantIdentifier(String c1, String c2, String prefix){
        String value="";
        if (c1 != null && !c1.isEmpty() && !c1.contains("?")){
            value = c2.replaceAll("_.*","") +"_"+c1.replaceAll("c\\.","").replaceAll(">","~");
            value = prefix+"/"+value;
        }
        return value;

    }
}
