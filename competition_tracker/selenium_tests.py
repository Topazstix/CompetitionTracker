from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class LoginTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_login(self):
        
        ## REGISTER USER FIRST
        self.browser.get(self.live_server_url + '/register/')
        username_input = self.browser.find_element(by=By.NAME, value='username')
        email_input = self.browser.find_element(by=By.NAME, value='email')
        password1_input = self.browser.find_element(by=By.NAME, value='password1')
        password2_input = self.browser.find_element(by=By.NAME, value='password2')
        submit_button = self.browser.find_element(by=By.NAME, value='submit')
        username_input.send_keys('test_account')
        email_input.send_keys('bunk@net.com')
        password1_input.send_keys('Bleach-Mollusk6-Municipal')
        password2_input.send_keys('Bleach-Mollusk6-Municipal')
        submit_button.click()
        
        ## VERIFY LOGIN
        username_input = self.browser.find_element(by=By.NAME, value='username')
        password_input = self.browser.find_element(by=By.NAME, value='password')
        submit_button = self.browser.find_element(by=By.NAME, value='submit')
        username_input.send_keys('test_account')
        password_input.send_keys('Bleach-Mollusk6-Municipal')
        submit_button.click()

        ## VALIDATE REDIRECTION
        expected_redirect_path = '/competitions/'
        current_url = self.browser.current_url
        assert current_url.endswith(expected_redirect_path), f"Expected redirect to {expected_redirect_path}, but got {current_url}"


class CompetitionCreationNavigationTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_navigation_to_competition_creation(self):

        ## REGISTER USER FIRST
        self.browser.get(self.live_server_url + '/register/')
        username_input = self.browser.find_element(by=By.NAME, value='username')
        email_input = self.browser.find_element(by=By.NAME, value='email')
        password1_input = self.browser.find_element(by=By.NAME, value='password1')
        password2_input = self.browser.find_element(by=By.NAME, value='password2')
        submit_button = self.browser.find_element(by=By.NAME, value='submit')
        username_input.send_keys('test_account')
        email_input.send_keys('bunk@net.com')
        password1_input.send_keys('Bleach-Mollusk6-Municipal')
        password2_input.send_keys('Bleach-Mollusk6-Municipal')
        submit_button.click()

        ## VALIDATE UN-AUTHENTICATED USER LOGIN REDIRECTION
        self.browser.get(self.live_server_url + '/competition/create')
        expected_redirect_path = '/login/?next=/competition/create/'
        current_url = self.browser.current_url
        assert current_url.endswith(expected_redirect_path), f"Expected redirect to {expected_redirect_path}, but got {current_url}"

        ## LOGIN
        username_input = self.browser.find_element(by=By.NAME, value='username')
        password_input = self.browser.find_element(by=By.NAME, value='password')
        submit_button = self.browser.find_element(by=By.NAME, value='submit')
        username_input.send_keys('test_account')
        password_input.send_keys('Bleach-Mollusk6-Municipal')
        submit_button.click()

        ## VALIDATE AUTHENTICATED USER LOGIN REDIRECTION        
        expected_redirect_path = '/competition/create/'
        current_url = self.browser.current_url
        assert current_url.endswith(expected_redirect_path), f"Expected redirect to {expected_redirect_path}, but got {current_url}"
