# import logging
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import datetime
import time

class GoogleSearchWorkflow:
    '''Testing basic user workflow'''
    def __init__(self):
        PATH = 'c:/dev/automation/prauto/browsers/chromedriver.exe'
        self.browser = webdriver.Chrome(executable_path=PATH)
        self.wait = WebDriverWait(self.browser, timeout=30)
        self.bre_ui = self.browser.window_handles[0]
        self.today = datetime.datetime.today()
    def choose_browser(self):
        pass

    def start_browser(self):
        '''Start browser and call URL'''
        browser = self.browser
        browser.get('https://google.de')
        assert 'Google' in browser.title
        browser.maximize_window()
        print('Website started successfully!')

    def close_alert(self): 
        # browser = self.browser
        wait = self.wait
        wait.until(EC.presence_of_element_located((By.ID, 'CXQnmb')))
        btn_deny = wait.until(EC.presence_of_element_located((By.ID, 'W0wltc')))
        btn_deny.click()
        print('Dismissed alert successfully!')
    
    def do_search(self):
        # browser = self.browser
        wait = self.wait
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))
        print('Found google search form successfully!')
        _input = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
        #_input.clear()
        _input.send_keys('hello world')
        _input.submit()
        wait.until(EC.title_contains('hello world'))
        print('Search done successfully!')
        
    def close_browser(self):
        browser = self.browser
        browser.close()
        print('Browser closed successfully!')



if __name__ == '__main__':
    test = GoogleSearchWorkflow()
    test.start_browser()
    test.close_alert()
    test.do_search()
    test.close_browser()




