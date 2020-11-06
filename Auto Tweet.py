from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome(executable_path="your chromedriver path here") # enter your chrome driver download path
driver.get("https://twitter.com/login")
sleep(3)
driver.find_element_by_name('session[username_or_email]').send_keys("your email or username") # your twitter accounts email or username
driver.find_element_by_name('session[password]').send_keys("password here") # twitter accounts password
driver.find_element_by_name('session[password]').send_keys(Keys.RETURN)
sleep(3)

f = open("SpamFile.txt", "r")

for word in f:
    if word == "\n":
        continue
    driver.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
    sleep(5)
    driver.find_element_by_class_name("notranslate").click()
    driver.find_element_by_class_name("notranslate").send_keys(word)
    driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
    sleep(70) # because of twitter spam tweet protection has to be 1 minute + per tweet sent

    f.close()
