import java.util.*;

public class Caesar{
private int tav;

public Caesar(int tav){
	if(tav <=25 && 1<= tav){this.tav=tav;}
	else {throw new IllegalArgumentException();}
}

public char[] chiper(char[] args){
	char[] szoveg = Arrays.copyOf(args,args.length);
	for (int i = 0; i < szoveg.length; i++) { 
	int unicode=(int)szoveg[i];
	//System.out.println(unicode);
	if(unicode>=97 && unicode<=122){
	if(unicode+tav<122){szoveg[i]=(char)(unicode+tav);}
	else{szoveg[i]=(char)(unicode+tav-25);}
	}	
	else{throw new IllegalArgumentException();}
	}
	return szoveg;
}
public char[] dechiper(char[] args){
	char[] szoveg = Arrays.copyOf(args,args.length);
	for (int i = 0; i < szoveg.length; i++) { 
	int unicode=(int)szoveg[i];
	if(unicode>=97 && unicode<=122){
	if(unicode-tav>=97){szoveg[i]=(char)(unicode-tav);}
	else{szoveg[i]=(char)(unicode-tav+25);}
	}	
	else{throw new IllegalArgumentException();}
	}
	return szoveg;
}
}