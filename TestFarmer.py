import unittest
from selenium import webdriver
from time import sleep


class FarmerUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testDisplaysHeadings(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        driver.find_element_by_name("email").send_keys("nadun@gmail.com")
        driver.find_element_by_name("password").send_keys("nadun")
        driver.find_element_by_name("signin").click()
        sleep(2)
        source=driver.page_source
        assert "Product Name" in source
        assert "Quantity" in source
        assert "Collected" in source
        assert "Cancel" in source

    def testDisplaysData(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        driver.find_element_by_name("email").send_keys("nadun@gmail.com")
        driver.find_element_by_name("password").send_keys("nadun")
        driver.find_element_by_name("signin").click()
        sleep(2)
        source=driver.page_source
        assert "banana" in source
        assert "30" in source

        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
