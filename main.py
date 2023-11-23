import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

CHROME_PATH = "C:/chromedriver-win64/chromedriver.exe"
IG_URL = "https://www.instagram.com/"
IG_LOGIN = "jluizpyhon@gmail.com"
IG_PASSWORD = "Qwe_123!"
TARGET_PROFILE_FOLLOWERS = "https://www.instagram.com/pythoneiro/followers/"

class InstagramFollowerBot():
    def __init__(self):
        self.service = Service(executable_path=CHROME_PATH, log_path="NUL")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def instagram_login(self, login, password):
        self.driver.get(IG_URL)
        time.sleep(2)

        # Actions - key presses
        actions = ActionChains(self.driver)
        action_press_enter = actions.send_keys(Keys.ENTER)
        action_press_escape = actions.send_keys(Keys.ESCAPE)

        # IG Login
        input_fields = self.driver.find_elements(By.CSS_SELECTOR, "input")
        self.ig_login_input = input_fields[0]
        self.ig_password_input = input_fields[1]
        self.ig_login_input.send_keys(IG_LOGIN)
        self.ig_password_input.send_keys(IG_PASSWORD)
        action_press_enter.perform()

        # Salvar informações - clicar em "Agora não"
        time.sleep(3)
        element_present = ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div"))
        WebDriverWait(self.driver, 10).until(element_present)
        save_login_prompt_no = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
        save_login_prompt_no.click()

        # Ativar notificações - clicar em "Agora não"
        time.sleep(3)
        notifications_on_prompt_no = self.driver.find_element(By.CSS_SELECTOR, "button._a9--._a9_1")
        notifications_on_prompt_no.click()

    def seguir(self, target_profile_followers):
        time.sleep(2)
        self.driver.get(target_profile_followers)
        time.sleep(5)
        followers_popup = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        while True:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            time.sleep(0.5)
            follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
            for follow_button in follow_buttons[2:len(follow_buttons)]:
                if follow_button.text == "Seguir":
                    follow_button.click()
                    print("Followed")
                    time.sleep(1)  # Necessary so IG doesn't block the activity
                else:
                    pass

ig_bot = InstagramFollowerBot()
ig_bot.instagram_login(IG_LOGIN, IG_PASSWORD)
ig_bot.seguir(TARGET_PROFILE_FOLLOWERS)
