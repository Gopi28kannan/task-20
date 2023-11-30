from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import wget
import os

class webhandle:
    def __init__(self, url):
        self.web_url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def win_switch(self):
        self.driver.get(self.web_url)
        sleep(2)
        self.driver.maximize_window()
        sleep(2)
        #FIRST close default opened window
        self.driver.find_element(By.XPATH, "//*[@id='popup']/div[2]/button").click()
        sleep(2)
        #download a monthly progress report 
        print("DOWNLOAD monthly progress report")
        print('-------------------------------------------------------')
        try:
            #and next select document in menu bar
            doc=self.driver.find_element(By.LINK_TEXT,"Documents")
            a = ActionChains(self.driver)
            a.move_to_element(doc).perform()
            sleep(2)
            #click monthly progress report
            self.driver.find_element(By.LINK_TEXT,'Monthly Progress Report').click()
            sleep(2)
            #create pdf folder from current saved program file
            try:
                path = "pdf_file"
                os.mkdir(path)
                print(path," folder created")
            except:
                print(path," already created")
            #i have just download first three monthy progress report pdf files, not all. Your download all please remove the if condiction
            pdfs=self.driver.find_elements(By.CSS_SELECTOR,"a[role='link'][title*='Download'][href]")
            count=0
            for i in pdfs:
                #your download all pdf files, please remove if count < 3: and else: break, don't remove center coding 
                if count < 3:
                    # get <a> tag attribute
                    link = i.get_attribute("href")
                    #use wget and download pdf file
                    wget.download(link, out=path)
                    print('pdf ',count+1,' is downloading')
                    i.click()
                    sleep(1)
                    #alert pop message accept(click okay)
                    alert = Alert(self.driver)
                    alert.accept()
                    #switch to control in sub window
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    sleep(3)
                    self.driver.close()
                else:
                    break
                #switch to control in primary window
                self.driver.switch_to.window(self.driver.window_handles[0])
                sleep(1)
                count +=1
        except:
            print("error")
        finally:
            print("pdf file successfully downloaded\n\n")
        sleep(4)
        #download ten images
        print("Download Images from photo gallery")
        print('------------------------------------------------------')
        try:
            #select media in menu bar
            imgd=self.driver.find_element(By.LINK_TEXT, "Media")
            a1 = ActionChains(self.driver)
            a1.move_to_element(imgd).perform()
            sleep(2)
            #click photo gallery
            self.driver.find_element(By.LINK_TEXT,'Photo Gallery').click()
            sleep(2)
            #use css selector and get required images in the window
            imgs=self.driver.find_elements(By.CSS_SELECTOR,"div.field-content>img")
            #create images folder
            try:
                path = "images"
                os.mkdir(path)
                print(path,' folder created')
            except:
                print(path,' folder already created')
            #use wget and download images
            count = 0
            for i in imgs:
                if count < 10:
                    link = i.get_attribute('src')
                    wget.download(link, out=path)
                    print("image ",count+1," is downloading")
                else:
                    break
                sleep(1)
                count += 1
        except:
            print(selenium_error)
        finally:
            print("10 images successfully downloaded and save the images folder")
    #close the chrome window
    def sh_win(self):
        sleep(5)
        self.driver.quit()
url ="https://labour.gov.in/"
wh = webhandle(url)
wh.win_switch()
wh.sh_win()
