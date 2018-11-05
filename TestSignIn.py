import unittest
from selenium import webdriver
from time import sleep


class SignUpUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testNewSignIn(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        email=driver.find_element_by_name("email")
        password=driver.find_element_by_name("password")
        signinbutton=driver.find_element_by_name("signin")
        email.send_keys("ushirask@gmail.com")
        password.send_keys("ushira")
        signinbutton.click()
        sleep(2)
        self.assertEqual(driver.current_url,"https://agrichain.ml/views/distributor.php")

    def testEmailInputIsAnValidEmailValidation(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        email_type=driver.find_element_by_name("email").get_attribute("type")
        self.assertEqual(email_type,"email")

    def testUnregisteredEmailPrompt(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        email=driver.find_element_by_name("email")
        password=driver.find_element_by_name("password")
        signinbutton=driver.find_element_by_name("signin")
        email.send_keys("testemail@gmail.com")
        password.send_keys("ushira")
        signinbutton.click()
        sleep(2)
        alert = driver.switch_to_alert()
        assert "Sign In Failed!" in alert.text
        
    def testWrongPasswordPrompt(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        email=driver.find_element_by_name("email")
        password=driver.find_element_by_name("password")
        signinbutton=driver.find_element_by_name("signin")
        email.send_keys("ushirask@gmail.com")
        password.send_keys("wrongpassword")
        signinbutton.click()
        sleep(2)
        try:
            alert = driver.switch_to_alert()
        #if no alert is present
        except:
            assert False

    def testWrongPasswordDoNotLogin(self):
        driver=self.driver
        driver.get("https://agrichain.ml/views/signin.php")
        email=driver.find_element_by_name("email")
        password=driver.find_element_by_name("password")
        signinbutton=driver.find_element_by_name("signin")
        email.send_keys("ushirask@gmail.com")
        password.send_keys("wrongpassword")
        signinbutton.click()
        sleep(2)
        self.assertNotEqual(driver.current_url,"https://agrichain.ml/views/distributor.php")
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
