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

class UploadTolls(unittest.TestCase):
    def setUp(self):
        # Set Chrome options for headless mode
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")  # Required for headless on Windows
        chrome_options.add_argument("--window-size=1920x1080")  # Optional: Set window size

        # Path to ChromeDriver, if needed
        # self.driver = webdriver.Chrome(executable_path=r'', options=chrome_options)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        print(webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options))
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_upload_tolls(self):
        # List of different locations for each iteration
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
            driver.find_element(By.ID, "todt").send_keys("23/09/2024")
            time.sleep(2)
            driver.find_element(By.ID, "location").click()
            Select(driver.find_element(By.ID, "location")).select_by_visible_text(location)
            # driver.find_element(By.ID, "location").click()
            # Select(driver.find_element(By.ID, "location")).select_by_visible_text("Sydney Airport")
            # driver.find_element(By.ID, "tollsFile").click()
            # driver.find_element(By.ID, "tollsFile").clear()

            # Find the latest file in the download directory
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

            downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
            # file_name = "Trips_8284934309_20240918215132.xls"  # Replace with the actual file name
            file_name = latest_file;
            file_path = os.path.join(downloads_folder, file_name)

            print(file_path);

            driver.find_element(By.ID, "tollsFile").send_keys(file_path)
            time.sleep(2)
            driver.find_element(By.XPATH, "//form[@id='upload-form']/button").click()
            time.sleep(20)
            # driver.find_element_by_xpath("//form[@id='upload-form']/button").click()
            driver.find_element(By.ID, "confirmBtn").click()
            time.sleep(5)
            self.assertEqual("Error: starting the job. Wait for progress bar to finish before going to any other page. Check few contract numbers from the new file to ensure it was uploaded.", self.close_alert_and_get_its_text())
            time.sleep(125)
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
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
