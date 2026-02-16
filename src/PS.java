import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;

public class PS {
////////////////////////// commit changes 1
	@BeforeClass
	public void beforeRunr() {
		System.out.println("Before Class");
	}
	@AfterClass
	public void beforreRunr() {
		System.out.println("After Class");
	}	
	
	@BeforeMethod
	public void beforeRun() {
		System.out.println("run me first before method");
	}

	@AfterMethod
	public void befforeRun() {
		System.out.println("AFTER method");
	}	
	public void doThis() {
		System.out.println("ian here doThis()");
	}
	@AfterSuite
	public void kbeforeRun() {
		System.out.println("After suit");
	}
}
