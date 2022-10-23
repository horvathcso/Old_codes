public class ColouredCircle extends Circle{
private ColouredPoint center;
public ColouredCircle(ColouredPoint center, double radius, String label) {
         super( radius,  label);
		this.center = new ColouredPoint(center);
       
    }
public ColouredPoint.Colour getColour(){return this.center.getSzin();}

}