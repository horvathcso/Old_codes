/**
 *@author author_name
 *@since 1.0
 *@version 1.0
 */

import java.io.*;
import utils.*;

public class Main {
	
    /**
     *  The starting point of the Java application
     * @param args commandline arguments
     */	
	     /**
     * <p>Try to read from file. If fail</p>
     * @throws IllegalArgumentException 
     * @throws IOException if there is problem while reading the file
     * @since 1.0
     */
    public static void main(String[] args) {

try(
BufferedReader in = new BufferedReader(new FileReader("input.txt"))
)
{
	

	String read = null;
	int i=0;
	Auto[] lista=new Auto[0];
	Auto[] newlista;
    while ((read = in.readLine()) != null) {
		newlista=new Auto[i+1];
		for(int j=0; j<i;j++){newlista[j]=lista[j];}
        String[] splited = read.split(",");
        newlista[i]=new Auto(splited[0],Color.parseColor((String)splited[1]),Integer.parseInt(splited[2]));
		lista=newlista;
}
}

catch( IOException | IllegalArgumentException e ){
System.err.println(e);
}
}
}
