import org.junit.*;
import java.util.*;
import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;


@RunWith(Parameterized.class)
public class CaesarTest {
	 
    @Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][] {     
			{toChar("abc"),toChar("cde")},{toChar("a"),toChar("c")},{toChar("bcd"),toChar("def")},{toChar("abcdefgh"),toChar("cdefghij")},{toChar("defj"),toChar("fghl")}
//                 { "abc".toCharArray(), "cde".toCharArray() } ,{"abc".toCharArray(), "cde".toCharArray()} 
           });
    }

    private char[] fInput;

    private char[] fExpected;

private static char[] toChar (String str){
		 return str.toCharArray();
}
	public CaesarTest(char[] inp, char[] out){
		this.fInput=inp;
		this.fExpected=out;
	}
	
	
    @Test
	public void test_chipper() {
	Caesar cs=new Caesar(2);
	String st= new String(fExpected);
	String s2= new String(cs.chiper(fInput));
	assertEquals(st,s2);
	}
	
	@Test
	public void test_dechipper() {
		Caesar cs=new Caesar(2);
	String st= new String(fInput);
	String s2= new String(cs.dechiper(fExpected));
	assertEquals(st,s2);
	}
	
	
	@Test
	public void test_othern() {
	Caesar cs3=new Caesar(3);
	Caesar cs4=new Caesar(4);
	Caesar cs5=new Caesar(5);
	char[] arg={'a','b','c'};
	String st3= "def";
	String st4= "efg";
	String st5= "fgh";
	String s3= new String(cs3.chiper(arg));
	String s4= new String(cs4.chiper(arg));
	String s5= new String(cs5.chiper(arg));
	assertEquals(st3,s3);
	assertEquals(st4,s4);
	assertEquals(st5,s5);
	}
	
	@Test (expected =IllegalArgumentException.class) 	
	public void test_Error1() {
	Caesar cs=new Caesar(222);
	}
	
	@Test (expected =IllegalArgumentException.class) 	
	public void test_Error2() {
	Caesar cs=new Caesar(22);
	char[] err={'A'};
	cs.dechiper(err);
	}
	
	
}
	