package es.upm.fi.dia.oeg;

import com.taxonic.carml.engine.RmlMapper;
import com.taxonic.carml.logical_source_resolver.CsvResolver;

import com.taxonic.carml.model.TriplesMap;
import com.taxonic.carml.util.RmlMappingLoader;
import com.taxonic.carml.vocab.Rdf;
import org.eclipse.rdf4j.model.Model;
import org.eclipse.rdf4j.rio.RDFFormat;
import org.eclipse.rdf4j.rio.Rio;

import java.io.File;
import java.io.FileOutputStream;
import java.nio.file.Paths;
import java.text.Normalizer;
import java.util.Set;

/**
 * Hello world!
 *
 */
public class CarmlCli
{
    public static void main( String[] args )
    {

        try {
            FileOutputStream foutput = new FileOutputStream(new File("output.nt"));
            System.out.println("Llego");
            Set<TriplesMap> mapping = RmlMappingLoader.build().load(RDFFormat.TURTLE, Paths.get("mapping.rml.ttl"));
            System.out.println("y aqui");
            RmlMapper mapper = RmlMapper.newBuilder()
                    // Add the resolvers to suit your need
                    .setLogicalSourceResolver(Rdf.Ql.Csv, new CsvResolver())
                    .addFunctions(new Functions())
                    // optional:
                    // set file directory for sources in mapping
                    .fileResolver(Paths.get("."))
                    .build();
            System.out.println("y aqui 2");
            Model result = mapper.map(mapping);
            System.out.println("LLego");
            Rio.write(result, foutput, RDFFormat.NTRIPLES);
            foutput.flush();
            foutput.close();
        }catch (Exception e){
            System.out.println("Exception: "+e.getMessage());
        }
    }
}
