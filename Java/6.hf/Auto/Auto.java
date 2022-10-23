import utils.*;
/**
 *@author author_name
 *@since 1.0
 *@version 1.0
 */


/**
     *  The starting point of the Java application
     * @param rendszam (String) 
	 * @param color (Color) 
	 * @param maxSpeed (int)
	 * @param Counter (int)
     */
public class Auto{
private String rendszam;
private Color color;
private int maxSpeed;
private int Counter;


/**
     *  A public constructor with 3 parameter {@code String Color, int} set the vales.
     */
public Auto(String rendszam, Color color, int maxSpeed){
this.rendszam=rendszam;
this.maxSpeed=maxSpeed;
this.color=color;
Counter++;
}

/**
     *  A public constructor without parameters give default value.
     */
public Auto(){
this.rendszam="AAA-000";
this.maxSpeed=120;
this.color=Color.BLUE;
Counter++;
}

/**
     *  A getter for maxSpeed parameter.
     */
public int getSpeed(){return maxSpeed;}

/**
     *  A public function, whit two param. Returns treu if the firs is faster, false otherwise. 
     */
public static boolean Compare (Auto a1, Auto a2){
return a1.getSpeed()>a2.getSpeed();
}

}