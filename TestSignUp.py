import unittest
from selenium import webdriver
from time import sleep


class SignUpUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testNewSignup(self):
        driver=self.driver
        driver.get("http://127.0.0.1/AgriChain/views/signup.php")
        email=driver.find_element_by_name("email")
        name=driver.find_element_by_name("name")
        address=driver.find_element_by_name("address")
        mobile=driver.find_element_by_name("mobile")
        password=driver.find_element_by_name("password")
        email.send_keys("nadun1@gmail.com")
        name.send_keys("Nadun1")
        address.send_keys("Nugegoda")
        mobile.send_keys("0776061092")
        password.send_keys("nadun1")
        signinbutton=driver.find_element_by_name("register")
        signinbutton.click()
        sleep(2)
        self.assertEqual(driver.current_url,"http://127.0.0.1/AgriChain/views/signin.php")

    def testDoubleSignup(self):
        driver=self.driver
        driver.get("http://127.0.0.1/AgriChain/views/signup.php")
        email=driver.find_element_by_name("email")
        name=driver.find_element_by_name("name")
        address=driver.find_element_by_name("address")
        mobile=driver.find_element_by_name("mobile")
        password=driver.find_element_by_name("password")
        email.send_keys("nadunregistered@gmail.com")
        name.send_keys("NadunRegistered")
        address.send_keys("Nugegoda")
        mobile.send_keys("0713478360")
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

    def testWrongMobileNumber(self):
        driver=self.driver
        driver.get("http://127.0.0.1/AgriChain/views/signup.php")
        email=driver.find_element_by_name("email")
        name=driver.find_element_by_name("name")
        address=driver.find_element_by_name("address")
        mobile=driver.find_element_by_name("mobile")
        password=driver.find_element_by_name("password")
        email.send_keys("nadun2@gmail.com")
        name.send_keys("Nadun2")
        address.send_keys("Nugegoda")
        mobile.send_keys("111111111111111111111111111111111111111")
        password.send_keys("nadun2")
        signinbutton=driver.find_element_by_name("register")
        signinbutton.click()
        sleep(2)
        self.assertNotEqual(driver.current_url,"http://127.0.0.1/AgriChain/views/signin.php")

    def testMobileNumberIsANumberValidation(self):
        driver=self.driver
        driver.get("http://127.0.0.1/AgriChain/views/signup.php")
        mobile_type=driver.find_element_by_name("mobile").get_attribute("type")
        self.assertEqual(mobile_type,"number")       

    def testEmailInputIsAnEmailValidation(self):
        driver=self.driver
        driver.get("http://127.0.0.1/AgriChain/views/signup.php")
        email_type=driver.find_element_by_name("email").get_attribute("type")
        self.assertEqual(email_type,"email")
        
    def testPasswordHidden(self):
        driver=self.driver
        driver.get("http://127.0.0.1/AgriChain/views/signup.php")
        password_type=driver.find_element_by_name("password").get_attribute("type")
        self.assertEqual(password_type,"password")
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
