package util;

import java.util.Arrays;
import java.lang.StringBuilder;

public class Vector {
    double[] vec;

    public Vector(double[] numbers) {
        vec = new double[numbers.length];
        for(int i=0; i<numbers.length; i++) {
            vec[i] = numbers[i];
        }
    }
	
	public static double vectorSkalar(Vector elso, Vector masodik) {
	int hossz=Math.min(elso.vec.length, masodik.vec.length);
			double osszeg=0.0;
			for(int i=0; i<elso.vec.length && i<masodik.vec.length; i++){
			osszeg=osszeg+elso.vec[i]*masodik.vec[i];
			}
			return osszeg;
	}

	public Vector skalar(double s) {
	Vector eredmeny=new Vector(this.vec);
	for(int i=0; i<eredmeny.vec.length; i++){
		eredmeny.vec[i]=s*eredmeny.vec[i];
	}
	return eredmeny;
	}

    public static Vector add(Vector elso, Vector masodik) {
			int hossz=Math.max(elso.vec.length, masodik.vec.length);
			double[] osszeg=new double[hossz];
			for(int i=0; i<elso.vec.length || i<masodik.vec.length; i++){
				if(elso.vec[i]!=0)
				{
					if(masodik.vec[i]!=0){
						osszeg[i]=elso.vec[i]+masodik.vec[i];
					}
					else{osszeg[i]=elso.vec[i];}
				}
				else{osszeg[i]=masodik.vec[i];}
			}
			Vector ossz=new Vector(osszeg);
			return ossz;
		}
		
	    public static Vector minus(Vector elso, Vector masodik) {
			int hossz=Math.max(elso.vec.length, masodik.vec.length);
			double[] kul=new double[hossz];
			for(int i=0; i<elso.vec.length || i<masodik.vec.length; i++){
				if(elso.vec[i]!=0)
				{
					if(masodik.vec[i]!=0){
						kul[i]=elso.vec[i]-masodik.vec[i];
					}
					else{kul[i]=elso.vec[i];}
				}
				else{kul[i]=0-masodik.vec[i];}
			}
			Vector kivon=new Vector(kul);
			return kivon;
		}

	@Override
    public String toString() {
		StringBuilder str = new StringBuilder(); 
		str.append("(");
		for(int i=0; i<vec.length; i++) {
        if(i != 0){str.append(", ");}
		str.append(String.valueOf(vec[i]));		
		}
        return str.toString();
    }
}