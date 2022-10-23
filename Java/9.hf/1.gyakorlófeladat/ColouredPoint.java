public class ColouredPoint extends Point{
private Colour szin;

public ColouredPoint(Point that) {
super(that.getX(),that.getY());}
public ColouredPoint(ColouredPoint that) {
        super(that.getX(),that.getY());
		this.szin=that.getSzin();
    }

public Colour getSzin(){return this.szin;}
public void setSzin(Colour szin){this.szin=szin;}
	
public enum Colour{
	RED, GREEN, BLUE;
}

}