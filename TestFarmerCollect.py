import unittest
from selenium import webdriver
from time import sleep


class FarmerUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        

    def testDisableCollectedButtonWhenCollected(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        driver.find_element_by_name("email").send_keys("nadun@gmail.com")
        driver.find_element_by_name("password").send_keys("nadun")
        driver.find_element_by_name("signin").click()
        sleep(2)
        driver.find_element_by_name("update").click()
        sleep(1)
        driver.find_element_by_xpath('//button[contains(text(), "Yes")]').click()
        collected_disabled=driver.find_element_by_name("update").get_attribute("disabled")
        self.assertTrue(collected_disabled)
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
