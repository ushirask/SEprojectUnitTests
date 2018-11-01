import unittest
from selenium import webdriver
from time import sleep


class SignUpUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testDoubleSignup(self):
        driver=self.driver
        driver.get("http://127.0.0.1/AgriChain/views/signup.php")
        email=driver.find_element_by_name("email")
        name=driver.find_element_by_name("name")
        address=driver.find_element_by_name("address")
        mobile=driver.find_element_by_name("mobile")
        password=driver.find_element_by_name("password")
        email.send_keys("nadun@gmail.com")
        name.send_keys("Nadun")
        address.send_keys("Nugegoda")
        mobile.send_keys("67548")
        password.send_keys("nadun")
        signinbutton=driver.find_element_by_name("register")
        signinbutton.click()
        sleep(2)
        alert = driver.switch_to_alert()
        assert "Sign Up Failed!" in alert.text
        
    def testFieldsRequired(self):
        driver=self.driver
        driver.get("http://127.0.0.1/AgriChain/views/signup.php")
        email=driver.find_element_by_name("email")
        name=driver.find_element_by_name("name")
        address=driver.find_element_by_name("address")
        mobile=driver.find_element_by_name("mobile")
        password=driver.find_element_by_name("password")
        self.assertTrue(email.get_attribute("required"))
        self.assertTrue(name.get_attribute("required"))
        self.assertTrue(address.get_attribute("required"))
        self.assertTrue(mobile.get_attribute("required"))
        self.assertTrue(password.get_attribute("required"))

    def testPasswordHidden(self):
        driver=self.driver
        driver.get("http://127.0.0.1/AgriChain/views/signup.php")
        password_type=driver.find_element_by_name("password").get_attribute("type")
        self.assertEqual(password_type,"password")
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
