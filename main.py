import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

'''
*** INSTRUÇÕES - PORTUGUÊS-BR ***

0. Atualize seus dados aqui no código. Verifique se o caminho do Chromedriver é o mesmo no seu computador
e coloque seu login / email e sua senha do IG nas constantes IG_LOGIN e IG_PASSWORD respectivamente.

1. Escolha o perfil de seu interesse no Instagram. Este programa irá seguir o máximo de seguidores 
possíveis deste perfil.
Isso é útil caso seja um perfil do seu nicho e você quer que os seguidores dele te sigam também.
Obviamente, não é garantido que te sigam de volta. Mas é prática comum no Instagram seguir 
de volta alguém que te seguiu.

2. Após escolher o perfil, cole o link dele na constante TARGET_PROFILE_FOLLOWERS.
Alternativamente, você pode simplesmente copiar apenas o nome do perfil no link e colar na mesma constante,
onde está escrito "TARGET_PROFILE".

3. Pronto! Você já pode usar o Follower Bot.  

_______________________________________________________________________________________________________________

*** INSTRUCTIONS - ENGLISH ***

0. Update your data here in the code. Check if the Chromedriver path is the same on your computer
and paste your IG login/email and password in the constants IG_LOGIN and IG_PASSWORD, respectively.

1. Choose the Instagram profile of your interest. This program will follow as many followers as possible
from this profile. 
This is useful if it's a profile within your niche and you want their followers to follow you too.
Obviously, there's no guarantee they'll follow you back. But it's a common practice on Instagram to follow back
someone who followed you.

2. After choosing the profile, paste its link in the constant TARGET_PROFILE_FOLLOWERS.
Alternatively, you can simply copy the profile name from the link and paste it in the same constant,
where it says "TARGET_PROFILE".

3. There! You can now use the Follower Bot.
'''


CHROME_PATH = "C:/chromedriver-win64/chromedriver.exe"  # Modifique o caminho do chromedriver de acordo / Modify the chromedriver path accordingly
IG_URL = "https://www.instagram.com/"
IG_LOGIN = "SEU_EMAIL / YOUR_EMAIL"
IG_PASSWORD = "SUA_SENHA / YOUR_PASSWORD"
TARGET_PROFILE_FOLLOWERS = "https://www.instagram.com/TARGET_PROFILE/followers/"

class InstagramFollowerBot():
    def __init__(self):
        self.service = Service(executable_path=CHROME_PATH, log_path="NUL")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def instagram_login(self, login, password):
        self.driver.get(IG_URL)
        time.sleep(2)

        # Ações - teclas pressionadas / Actions - key presses
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

        # Salvar informações - clicar em "Agora não" / Save info - click in "Not now"
        time.sleep(3)
        element_present = ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div"))
        WebDriverWait(self.driver, 10).until(element_present)
        save_login_prompt_no = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
        save_login_prompt_no.click()

        # Ativar notificações - clicar em "Agora não" / Save info - click in "Not now"
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
                if follow_button.text == "Seguir" or follow_button.text == "Follow":  # Mude o texto do botão de acordo com sua linguagem / Change the Follow button text according to your language
                    follow_button.click()
                    print("Seguindo o perfil de IG alvo / Following the target IG profile")
                    time.sleep(1)  # Necessário para que o IG não bloqueie a atividade / Necessary so IG doesn't block the activity
                else:
                    pass

ig_bot = InstagramFollowerBot()
ig_bot.instagram_login(IG_LOGIN, IG_PASSWORD)
ig_bot.seguir(TARGET_PROFILE_FOLLOWERS)
