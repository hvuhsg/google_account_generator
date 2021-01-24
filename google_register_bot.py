from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import warnings

warnings.filterwarnings("ignore")

PHON_NUMBER = ""
FISRT_NAME = ""
LAST_NAME = ""
USERNAME = ""
PASSWORD = ""
GENDER = 1 # 0 for female and 1 for male 



class GoogleAccountGenerator:
    def __init__(self, first_name, last_name, account_name, password, gender):
        self.driver = webdriver.Firefox()
        self.first_name = first_name
        self.last_name = last_name
        self.account_name = account_name
        self.gender = gender
        self.password = password

    def first_form(self):
        first_name_box = self.driver.find_element_by_id("firstName")
        first_name_box.send_keys(self.first_name)

        last_name_box = self.driver.find_element_by_id("lastName")
        last_name_box.send_keys(self.last_name)

        account_name_box = self.driver.find_element_by_id("username")
        account_name_box.send_keys(self.account_name)

        password_box = self.driver.find_element_by_name("Passwd")
        password_box.send_keys(self.password)

        confirm_box = self.driver.find_element_by_name("ConfirmPasswd")
        confirm_box.send_keys(self.password)

        password_box.send_keys(Keys.ENTER)

    def second_form(self):
        phone_number_box = self.driver.find_element_by_xpath('//*[@id="phoneNumberId"]')
        phone_number_box.send_keys(PHON_NUMBER)

        phone_number_box.send_keys(Keys.ENTER)

    def third_form(self):
        code_box = self.driver.find_element_by_xpath('//*[@id="code"]')
        code_box.send_keys(input("G-"))
        code_box.send_keys(Keys.ENTER)

    def forth_form(self):
        month = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/select/option[3]").click()

        day_box = self.driver.find_element_by_id("day")
        day_box.send_keys("14")

        year = self.driver.find_element_by_id("year")
        year.send_keys("1978")

        gender = self.driver.find_element_by_xpath("//select[@id='gender']/option[value=2]").click()

        # year.send_keys(Keys.ENTER)

    def fifth_form(self):
        skip = self.driver.find_element_by_xpath("//*[contains(text(), 'Skip')]").click()
        i_agree = self.driver.find_element_by_xpath("//*[contains(text(), 'I agree')]").click()

    def run(self):
        self.driver.get(
            "https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp"
        )
        print("login...")
        self.first_form()
        time.sleep(1)
        self.second_form()
        time.sleep(2)
        self.third_form()
        time.sleep(1)
        self.forth_form()
        time.sleep(1)
        self.fifth_form()
        time.sleep(1)

    def close(self):
        self.driver.quit()


def main():
    bot = GoogleAccountGenerator(FISRT_NAME, LAST_NAME, USERNAME, PASSWORD, GENDER)
    try:
        bot.run()
    except Exception as ex:
        print(type(ex), str(ex))

    input("press enter or ctrl+c to exit...")

if __name__ == "__main__":
    main()
