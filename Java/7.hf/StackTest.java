import org.junit.*;
import java.util.*;
import static org.junit.Assert.*;

public class StackTest {
    @Test
    public void test_lastelement() {
		Stack st1 = new Stack();
		st1.push(1);
        assertEquals(1, st1.pop());
		st1.push(2020);
		assertEquals(2020, st1.pop());
		st1.push(0);
		st1.push(11);
		assertEquals(11,st1.pop());
    }
	
	@Test
	public void test_newisempty() {
		Stack st1 = new Stack();
		assertEquals(true,st1.empty());
	}
	
	@Test
	public void test_elementisnotempty() {
		Stack st1 = new Stack();
		st1.push(123);
		assertEquals(false,st1.empty());
	}
	
	 @Test(expected = NoSuchElementException.class)
	 public void test_throwexception() {
		Stack st1 = new Stack();
		st1.pop();
	}
	
	@Test
	public void test_size() {
		Stack st1 = new Stack();
		assertEquals(0, st1.size());
		st1.push(2);
		assertEquals(1,st1.size());
	}
	
	@Test
	public void test_pushpop() {
		Stack st1 = new Stack();
		st1.push(123);
		st1.push(st1.pop());
		assertEquals(123,st1.pop());
		
	}
	
	@Test
	public void test_poplastisempty() {
		Stack st1 = new Stack();
		st1.push(1);
		st1.pop();
		assertEquals(true,st1.empty());
		
	}
}