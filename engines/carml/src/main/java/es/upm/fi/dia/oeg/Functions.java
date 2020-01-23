package es.upm.fi.dia.oeg;

import com.taxonic.carml.engine.function.FnoFunction;
import com.taxonic.carml.engine.function.FnoParam;

public class Functions {



    @FnoFunction("http://users.ugent.be/~bjdmeest/function/grel.ttl#toUpperCase")
    public String toUpperCase(@FnoParam("http://users.ugent.be/~bjdmeest/function/grel.ttl#valueParameter") String s) {
        return s.toUpperCase();
    }
}
