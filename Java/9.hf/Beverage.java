public class Beverage{
	private String name;
	private int legalAge;
	
	public Beverage(String name, int legalAge){
		if(name !=null && legalAge>0){this.name=name; this.legalAge=legalAge; }
		throw new IllegalArgumentException();
	}
	
	public String getName(){return name;}
	public int getlegalAge(){return legalAge;}
}