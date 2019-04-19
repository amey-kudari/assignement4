import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class RandomValueSelectionInDropdown {

	public static void main(String[] args) throws InterruptedException {

		// Setting chrome driver path
		System.setProperty("webdriver.chrome.driver", "./exefiles/chromedriver.exe");

		// Launching browser
		WebDriver driver = new ChromeDriver();

		// Maximize window
		driver.manage().window().maximize();

		// Load the URL
		driver.get("./templates/Quizzes.html");

		// Locating Options & Buttons
		WebElement quizQ = driver.findElement(By.className("quizQ"));
		WebElement nextButton = driver.findElement(By.className("btn btn-success"));
		

		// Putting in a loop to select different values every time
		for (int i = 0; i < 10; i++) {

			// Getting list of options
			List<WebElement> itemsInOptions = driver.findElements(By.className("option"));

			// Size of options available
			int size = 3;

			// Generate a random number with in range
			int randomOption = ThreadLocalRandom.current().nextInt(0, size);

			// Selecting random value
			itemsInOptions.get(randomOption).click();

			// Clicking next question
			nextButton.click();

			// Waiting for 1 second
			Thread.sleep(1000);

		}

		// Clicking Evaluate
		nextButton.click();

		// Creating View Report Element
		WebElement viewReport = driver.findElement(By.className("ansLink"));

		// Clicking View Report
		viewReport.click();

	}
}