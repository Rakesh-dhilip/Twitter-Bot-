from internet import InternetSpeedTwitterBot
SPEED=200
path='C:/Users/reshm/chromedriver'
Test=InternetSpeedTwitterBot(path)

Test.get_internet_speed()

if(SPEED>Test.upload and SPEED>Test.download):
    Test.complain()

