from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import By


class DriverFactory:
    def __init__(self):
        self._install_driver()

    def _install_driver(self):
        chromedriver_autoinstaller.install()

    def create_instance(self, login, password) -> WebDriver:
        self.driver = webdriver.Chrome()

        # Fix it.
        self.driver.get('https://discord.com/channels/1070053475829960724/1070053475829960727')
        sleep(10)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(login)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[2]/div/input').send_keys(password)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]').click()
        sleep(20)
        return self.driver
