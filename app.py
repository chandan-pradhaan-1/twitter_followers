from audioop import add
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

address = "https://twitter.com/explore"
twitter_user_id = input("Enter user name of twitter user : ")
driver = webdriver.Chrome()

def findFollowers(id):
    driver.get(address)
    driver.implicitly_wait(10)
    search_box = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
    search_box.send_keys(twitter_user_id)
    search_box.send_keys(Keys.RETURN)
    people = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/span')
    people.click()
    person = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/div[2]/div')
    person.click()
    followers = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span')
    print(followers.text)
    


findFollowers(twitter_user_id)






