import java.util.*;

public class Stack{
private ArrayList<Integer> verem = new ArrayList<Integer>();

public void push(int p){
verem.add(p);	
}

public int pop(){
if(verem.isEmpty()){
	throw new NoSuchElementException();
}
else{
int vissza=verem.get(verem.size()-1);
verem.remove(verem.size()-1);
return vissza;
}
}

public boolean empty(){
return verem.isEmpty();
}

public int size(){
return verem.size();
}
}