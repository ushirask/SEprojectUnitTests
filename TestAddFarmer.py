import unittest
from selenium import webdriver
from time import sleep


class SignUpUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testAddCorrect(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        driver.find_element_by_name("email").send_keys("nadun@gmail.com")
        driver.find_element_by_name("password").send_keys("nadun")
        driver.find_element_by_name("signin").click()
        sleep(2)
        driver.get("http://agrichain.ml/views/add_farmer_request.php")
        driver.find_element_by_name("product").send_keys("banana")
        driver.find_element_by_name("quantity").send_keys("30")
        driver.find_element_by_name("submit").click()
        sleep(2)
        source=driver.page_source
        assert "banana" in source
        assert "30" in source

    def testQuantityIsANumber(self):
        driver=self.driver
        driver.get("http://agrichain.ml/views/add_farmer_request.php")
        quantity_type=driver.find_element_by_name("quantity").get_attribute("type")
        self.assertEqual(quantity_type,"number")

    def testFieldsAreRequired(self):
        driver=self.driver
        driver.get("http://agrichain.ml/views/add_farmer_request.php")
        quantity_required=driver.find_element_by_name("quantity").get_attribute("required")
        product_required=driver.find_element_by_name("product").get_attribute("required")
        self.assertTrue(quantity_required)
        self.assertTrue(product_required)
            
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
