package utils;
/**
    *  Mivel belső csomagaban van, így a megfelelő működéshez szükséges a csomag megadása
    */

/**
    *  A Color felsorolási objektum négy lehetséges értékkel rendelkezik
    */
public enum Color {
NODATA, RED,GREEN,BLUE;


/**
    *  Ahhoz, hogy a Main-ben a stringből létrehozhassak Color objektumokat, készült egy {@code parseColor} statikus függvény, ami stringet Colorrá alakít
    */
public static Color parseColor(String s)
{
if(s=="RED"){return Color.RED;}
else if(s=="GREEN"){return Color.GREEN;}
else if(s=="BLUE"){return Color.BLUE;}
return Color.NODATA;
}	
}