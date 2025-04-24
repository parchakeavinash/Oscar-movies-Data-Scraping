from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import csv


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.scrapethissite.com/pages/ajax-javascript/")

time.sleep(5)

year_elements = driver.find_elements(By.XPATH, '//a[@class="year-link"]')

data = []

for each_year in year_elements:
    each_year.click()
    time.sleep(3)

    movie_names = driver.find_elements(By.XPATH, '//td[@class="film-title"]')
    nominations = driver.find_elements(By.XPATH, '//td[@class="film-nominations"]')
    film_awards = driver.find_elements(By.XPATH, '//td[@class="film-awards"]')

    for each_movie, nomination_num, award_num in zip(movie_names, nominations, film_awards):
        print(each_movie.text, nomination_num.text, award_num.text)
        data.append([each_movie.text, nomination_num.text, award_num.text])


driver.close()

with open("Oscar_movies_data.csv", 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Movie Name","Nominations","Awards"])
    writer.writerows(data)

print("Avinash You have completed scraping the website")