public class Bartender{
	public boolean order(Beverage b, Guest g){
		if(b.getlegalAge()==18 && g instanceof Adult){return false;}
		return true;
	}
}