from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import time
import pickle
import undetected_chromedriver as uc
import csv
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import os
from pathlib import Path

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

BASE_PATH = Path(__file__).resolve().absolute().parent
print(BASE_PATH)

driver = webdriver.Chrome()


class WebscrapeJson:

    def __init__(self, email, pwd, keyword):
        self.email = email
        self.pwd = pwd
        self.keyword = keyword
        self.cookies_file_path = BASE_PATH / "cookies.pkl"

    def logIn(self):
        driver.get(
            f"https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&trk=login_reg_redirect"
        )
        driver.maximize_window()
        if os.path.exists(self.cookies_file_path):
            # load cookies
            cookies = pickle.load(open(self.cookies_file_path, "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.get("https://www.linkedin.com/feed/")
            time.sleep(10)
        else:
            sign_in = driver.find_element(
                By.CLASS_NAME, "main__sign-in-link"
            ).get_attribute("href")
            driver.get(sign_in)
            email_input = driver.find_element(By.ID, "username")
            email_input.send_keys(self.email)
            pwd_input = driver.find_element(By.ID, "password")
            pwd_input.send_keys(self.pwd)
            btn = driver.find_element(By.CLASS_NAME, "btn__primary--large")
            btn.click()
            # driver.get("https://www.linkedin.com/feed/")
            pickle.dump(driver.get_cookies(), open(self.cookies_file_path, "wb"))

    # get all the links of the profiles
    def get_all_profiles(self, class_name):
        links = driver.find_elements(By.CLASS_NAME, class_name)
        profiles_links = []
        for i in range(7, len(links), 2):
            profiles_links.append(links[i].get_attribute("href"))
        return profiles_links

    # convert to json file
    def convert_to_json_file(self, all_details):
        json_object = json.dumps(all_details)
        with open("profiles.json", "a+") as profiles:
            profiles.write(json_object)

    def collect_information(self):
        all_details = []
        infomation = {}
        # cookies = pickle.load(open(self.cookies_file_path, "rb"))
        # for cookie in cookies:
        #     driver.add_cookie(cookie)
        time.sleep(10)
        driver.get(
            f"https://www.linkedin.com/search/results/people/?origin=TALKS_ABOUT_CLUSTER_SEE_MORE_CANNED_SEARCH&sid=9B%40&talksAbout=%5B%22{self.keyword}%22%5D"
        )
        time.sleep(5)
        page = 2
        while True:
            profiles_links = self.get_all_profiles("app-aware-link ")
            for profile in profiles_links:
                print("the link", profile)
                self.convert_to_json_file(infomation)
            try:
                driver.get(
                    f"https://www.linkedin.com/search/results/people/?keywords={self.keyword}&origin=GLOBAL_SEARCH_HEADER&page={page}"
                )
                page += 1
            except:
                break



keyword = input("Put the keyword : ")
webscrape=WebscrapeJson("saidishadow@gmail.com","aziz1234",keyword)
webscrape.logIn()
webscrape.collect_information()
