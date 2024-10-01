# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import Select class
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest, time
import datetime
import os
import pandas as pd

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

        # Set the default download directory to /tmp
        chrome_prefs = {
            "download.default_directory": "Downloads",  # Heroku writable directory
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", chrome_prefs)

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

            # Get today's date
            todayDate = datetime.date.today()

            # Subtract 3 days from today's date
            three_days_back = todayDate - datetime.timedelta(days=3)

            # Format the date as dd/mm/yyyy
            three_days_back_formatted = three_days_back.strftime("%d/%m/%Y")

            print("Today's Date:", todayDate.strftime("%d/%m/%Y"))
            print("3 Days Back:", three_days_back_formatted)

            today = datetime.date.today().strftime("%d/%m/%Y")

            print(today);

            # Set the current date in the startDateId field
            # Use JavaScript to set the value directly in the input field
            driver.execute_script(f"document.getElementById('startDateId').value = '{three_days_back_formatted}';")
            
            time.sleep(10)  # Wait for 10 seconds

            # Now try clicking the button after the overlay is gone
            driver.find_element(By.ID, "exportButton").click()
            driver.find_element(By.ID, "exportAndSave").click()
            time.sleep(30)  # Wait for 10 seconds

            # Verify if the file is present in /tmp
            
            files = os.listdir('Downloads')
            print(f"Files in Downloads: {files}")

            # Check for any .xls file in the directory
            xls_files = [f for f in files if f.endswith('.xls')]
            if xls_files:
                print(f"XLS file found: {xls_files}")
            else:
                print("No XLS file found in /tmp.")

            # DATA uploading has started from next line!

            locations = ["Sydney Airport", "Adelaide Melrose Park", "Brisbane Airport", "Cairns Airport", "Adelaide Airport"]
            
            print("locations :{locations}");
            # Loop through each location (5 times)
            for location in locations:
                print(f"Processing location: {location}")

                driver = self.driver
                # driver.get("https://carcharter-automation-b28424ced80d.herokuapp.com/")
                # driver.find_element(By.ID, "username").click()
                # driver.get("https://manage.linkt.com.au/retailweb/trips/triphistory/export/sydney")
                driver.get("https://carcharter-automation-b28424ced80d.herokuapp.com/")

                
                driver.find_element(By.ID, "username").clear()
                driver.find_element(By.ID, "username").send_keys("bz@simbacarhire.com.au")
                
                driver.find_element(By.ID, "password").click()
                driver.find_element(By.ID, "password").clear()
                driver.find_element(By.ID, "password").send_keys("bzsimba1368?")
                driver.find_element(By.XPATH, "//form[@id='license-form']/button").click()
                time.sleep(10)  # Wait for 10 seconds
                # driver.find_element_by_xpath("//form[@id='license-form']/button").click()
                
                driver.find_element(By.ID, "fromDt").click()
                driver.find_element(By.ID, "fromDt").clear()
                driver.find_element(By.ID, "fromDt").send_keys("20/09/2024")
                time.sleep(2)
                driver.find_element(By.ID, "todt").click()
                driver.find_element(By.ID, "todt").clear()
                driver.find_element(By.ID, "todt").send_keys("30/09/2024")
                time.sleep(2)
                driver.find_element(By.ID, "location").click()
                Select(driver.find_element(By.ID, "location")).select_by_visible_text(location)
                # driver.find_element(By.ID, "location").click()
                # Select(driver.find_element(By.ID, "location")).select_by_visible_text("Sydney Airport")
                # driver.find_element(By.ID, "tollsFile").click()
                # driver.find_element(By.ID, "tollsFile").clear()

                # Find the latest file in the download directory

                # For localhost

                def get_latest_download_file(directory):
                    files = os.listdir(directory)
                    paths = [os.path.join(directory, filename) for filename in files if filename.endswith('.xls')]  # Assuming CSV file
                    return max(paths, key=os.path.getctime) if paths else None

                download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
                latest_file = get_latest_download_file(download_dir)

                if latest_file:
                    print(f"Latest downloaded file: {latest_file}")
                else:
                    print("No file downloaded.")

                # downloads_folder = os.path.join(os.path.expanduser("~"), "/tmp")
                # # file_name = "Trips_8284934309_20240918215132.xls"  # Replace with the actual file name
                # file_name = xls_files[0];
                # file_path = os.path.join(downloads_folder, file_name)

                # For Heroku
                # file_path = xls_files[0]

                print("FILE Name: ")
                print(latest_file);

                # Read the Excel file
                df = pd.read_excel("/app/Downloads/Trips_8284934309_20241001024530.xls", engine="xlrd")
                
                # Print the entire DataFrame
                print(df)
                
                # Or, if you want to print specific columns
                # print(df[['Column1', 'Column2']])  # Replace with actual column names
                

                driver.find_element(By.ID, "tollsFile").send_keys("/app/Downloads/Trips_8284934309_20241001024530.xls")
                time.sleep(5)
                driver.find_element(By.XPATH, "//form[@id='upload-form']/button").click()
                time.sleep(40)
                # driver.find_element_by_xpath("//form[@id='upload-form']/button").click()
                driver.execute_script("document.getElementById('confirmBtn').click();")
                # driver.find_element(By.ID, "confirmBtn").click()
                time.sleep(20)
                self.assertEqual("Error: starting the job. Wait for progress bar to finish before going to any other page. Check few contract numbers from the new file to ensure it was uploaded.", self.close_alert_and_get_its_text())
                time.sleep(125)

        
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
