from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
class webhandle:

    def __init__(self, url):
        self.web_url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def win_switch(self):
        try:
            #open the primary window
            self.driver.get(self.web_url)
            # maximize window
            self.driver.maximize_window()
            # switch to the FAQ window
            print('open FAQ window')
            self.driver.find_element(By.XPATH, "//a[@class='dropdwnbtn accessibility-plugin-ac newMenu' and @href='/faq']").click()
            sleep(4)
            # switch to the PARTNERS window
            print('open PARTNERS window')
            self.driver.find_element(By.XPATH, "//a[@class='dropdwnbtn accessibility-plugin-ac newMenu' and @href='/our-partner']").click()
            sleep(4)
            window = self.driver.window_handles
            #switch to controls in sub windows
            for w in window:
                self.driver.switch_to.window(w)
                if self.driver.current_url == "https://www.cowin.gov.in/faq":
                    # print the current page url in the console
                    print("FAQ url:" , self.driver.current_url)
                    self.driver.close()
                    sleep(4)
                elif self.driver.current_url == 'https://www.cowin.gov.in/our-partner':
                    #print the current page url in the console
                    print("PARTNER url : " , self.driver.current_url)
                    self.driver.close()
                    sleep(4)
            #finally return the primary window
            print("close FAQ and PARTNERS window")
            
        except:
            print("An exception occurred")
        
    def sh_win(self):
        sleep(5)
        self.driver.quit()
url = "https://www.cowin.gov.in/"
wh = webhandle(url)
wh.win_switch()
#and last close the primary window
print('finally close the primary window')
wh.sh_win()

