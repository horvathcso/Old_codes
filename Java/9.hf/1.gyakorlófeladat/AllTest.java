import org.junit.*;
import java.util.*;
import static org.junit.Assert.*;

public class AllTest {
    @Test
    public void test_ColouredPint() {
		ColouredPoint p= new ColouredPoint(new Point(1,1));
		p.setSzin(ColouredPoint.Colour.BLUE);
		assertEquals(ColouredPoint.Colour.BLUE,p.getSzin());
    }
	
	@Test
	public void test_ColouredCircle() {
		ColouredPoint p= new ColouredPoint(new Point(1,1));
		p.setSzin(ColouredPoint.Colour.BLUE);
		ColouredCircle c= new ColouredCircle(p,1.0,"test");
		assertEquals(ColouredPoint.Colour.BLUE,c.getColour());
    }
	}