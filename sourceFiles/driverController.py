from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


class DriverController:    
    @staticmethod
    def send_prompt(driver: WebDriver, prompt: str) -> None:
        msg_xpath = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div'
        try:
            driver.find_element(By.XPATH, msg_xpath).send_keys(prompt)
            try:
                driver.find_element(By.XPATH, msg_xpath).send_keys(webdriver.Keys.ENTER)
            except Exception as ex:
                print(f'cannot find path: {ex}')
        except Exception as ex:
            print(ex)
            return 'Cant send this prompt'
        return driver
    
    @staticmethod
    def driver_waiter(driver, WebDriver, prompt: str) -> None:
        pass
    
    @staticmethod
    def save_image(driver: WebDriver, prompt: str):
        pass
