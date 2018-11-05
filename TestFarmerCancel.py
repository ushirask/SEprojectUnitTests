import unittest
from selenium import webdriver
from time import sleep


class FarmerCancelRequestUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def testCancelDeletingData(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        driver.find_element_by_name("email").send_keys("nadun@gmail.com")
        driver.find_element_by_name("password").send_keys("nadun")
        driver.find_element_by_name("signin").click()
        sleep(2)
        driver.find_element_by_name("delete").click()
        sleep(1)
        driver.find_element_by_xpath('//button[contains(text(), "No")]').click()
        source=driver.page_source
        assert "banana" in source
        
    def testDeleteData(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        driver.find_element_by_name("email").send_keys("nadun@gmail.com")
        driver.find_element_by_name("password").send_keys("nadun")
        driver.find_element_by_name("signin").click()
        sleep(2)
        driver.find_element_by_name("delete").click()
        sleep(1)
        driver.find_element_by_xpath('//button[contains(text(), "Yes")]').click()
        source=driver.page_source
        assert "banana" not in source
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
