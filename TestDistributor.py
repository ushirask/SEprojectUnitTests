import unittest
from selenium import webdriver
from time import sleep


class SignUpUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testDisplaysHeadings(self):
        driver=self.driver
        driver.get("http://agrichain.ml/views/distributor.php")
        source=driver.page_source
        assert "Product Name" in source
        assert "Quantity" in source
        assert "Farmer" in source
        assert "Address" in source
        
    def testDisplaysData(self):
        driver=self.driver
        driver.get("http://agrichain.ml/views/distributor.php")
        source=driver.page_source
        assert "Beans" in source
        assert "100" in source
        assert "lahiru" in source
        assert "298" in source
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
