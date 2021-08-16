import time

from selenium import webdriver
SPEED=200
USERNAME='SORRY ICANT GIVE MY ID'
PASSWORD='THEN HOW CAN I GIVE MY PASSWORD'
class InternetSpeedTwitterBot:
    def __init__(self,path):
        self.website=webdriver.Chrome(executable_path=path)
        self.download=0
        self.upload = 0

    def get_internet_speed(self):
        self.website.get('https://www.speedtest.net/')
        time.sleep(3)
        but=self.website.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        but.click()
        time.sleep(60)
        self.download=int(self.website.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.upload=int(self.website.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        self.website.quit()
    def complain(self):
        self.website.get('https://twitter.com/login')
        time.sleep(3)
        user=self.website.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        user.send_keys(USERNAME)

        Pass=self.website.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        Pass.send_keys(PASSWORD)

        submit=self.website.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        submit.click()

        time.sleep(3)

        tweet=self.website.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet.click()

        time.sleep(2)
        msgsend=self.website.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        message = f'Hi @ACTFibernet my internet speed is {self.download} ms down/{self.upload}ms  up instead of {SPEED}ms down/{SPEED}ms up'
        msgsend.send_keys(message)
        time.sleep(4)
        tweetsubmit=self.website.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweetsubmit.click()
        self.website.quit()