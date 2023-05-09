from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InsiderHomePage:
    def __init__(self, driver):
        self.driver = driver

    more_button = (By.XPATH, "//a[@href='#' and text()='More']")
    careers_button = (By.XPATH, "//a[@href='/careers/' and text()='Careers']")
    xpath_selector_more = (By.XPATH, '//a[@class="nav-link dropdown-toggle" and @href="javascript:void(0);"]//span[contains(text(), "More")]')
    xpath_selector_careers = (By.XPATH, "//a[contains(@href, 'https://useinsider.com/careers/')]")

    def click_more(self):
        more_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.xpath_selector_more))
        more_element.click()

    def click_careers(self):
        careers_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.xpath_selector_careers))
        careers_element.click()
