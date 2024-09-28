# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest, time
import datetime

class Sibacar3(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # Add any other options you need here

        # Create a new instance of Chrome
        # self.driver = webdriver.Chrome(service=Service(executable_path='/usr/local/bin/chromedriver'), options=chrome_options)
        # self.driver.implicitly_wait(30)

        # Update the path to your ChromeDriver executable
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        print(webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options))
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    
    def test_sibacar3(self):
        print("username enterd!!");
        driver = self.driver
        
        # driver.get("https://www.linkt.com.au/login")
        driver.get("https://manage.linkt.com.au/retailweb/login?username=bz%40simbacarhire.com.au")
        
        try:
            print("driver");
            # print(driver.get("https://manage.linkt.com.au/retailweb/login?username=bz%40simbacarhire.com.au"));
        
            # element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.ID, "loginForm-username-field"))
            # )
            # print("Page loaded and element found!")
            # # Wait for the username field and interact with it
            # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "loginForm-username-field"))).clear()
            # driver.find_element(By.ID, "loginForm-username-field").send_keys("bz@simbacarhire.com.au")
            
            # # Click the login button
            # driver.find_element(By.XPATH, "//div[@id='page-content']/div[6]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/form/div/div[3]/button/span").click()
            
            # # Wait for the next page element to be clickable and interact with it
            # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Taking you to your account'])[1]/following::span[1]"))).click()
            
            # driver.get("https://manage.linkt.com.au/retailweb/login?username=bz%40simbacarhire.com.au")
            driver.find_element(By.ID, "acc-pin").clear()
            driver.find_element(By.ID, "acc-pin").send_keys("Simbasydbrisbane89!")
            driver.find_element(By.ID, "submit-button").click()
            
            # driver.get("https://manage.linkt.com.au/retailweb/account/home/sydney")
            
            # time.sleep(20)  # Wait for 10 seconds
            # driver.find_element(By.LINK_TEXT, "Export trips").click()
            
            # driver.get("https://manage.linkt.com.au/retailweb/trips/triphistory/results/sydney")
            # driver.find_element(By.XPATH, "//div[@id='inner-wrap']/div[4]/div/div[2]/div/div[2]/a").click()
            
            driver.get("https://manage.linkt.com.au/retailweb/trips/triphistory/export/sydney")
            time.sleep(20)  # Wait for 10 seconds
            
            # driver.find_element(By.ID, "startDateId").click()
            # driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']/div/a[2]/span").click()
            # driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']/div/a[2]/span").click()
            # driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']/div/a[2]/span").click()
            # driver.find_element(By.LINK_TEXT, "8").click()

            # Get today's day (as a string)
            # today = str(datetime.date.today())
            today = datetime.date.today().strftime("%d/%m/%Y")

            print(today);

            # Set the current date in the startDateId field
            # Use JavaScript to set the value directly in the input field
            driver.execute_script(f"document.getElementById('startDateId').value = '{today}';")
            
            time.sleep(10)  # Wait for 10 seconds

            # Now try clicking the button after the overlay is gone
            driver.find_element(By.ID, "exportButton").click()
            driver.find_element(By.ID, "exportAndSave").click()
            time.sleep(30)  # Wait for 10 seconds

            # Wait until the overlay is invisible
            # WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "fancybox-overlay")))
            # time.sleep(30)  # Wait for 10 seconds

            # try:
            #     driver.find_element(By.ID, "exportButton").click()
            #     driver.find_element(By.ID, "exportAndSave").click()
            #     # Wait until the overlay is invisible
            #     WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "fancybox-overlay")))
            #     print("clickable");
            
            # except NoSuchElementException as e:
            #     print(f"Element not found: {e}")
            # except Exception as e:
            #     print(f"An error occurred: {e}")

        
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
