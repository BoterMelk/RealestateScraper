from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



url="https://itshousing.nl/woningaanbod/huur"
page = requests.get(url)

pageContent = BeautifulSoup(page.content, 'html.parser')
listings = pageContent.find_all('article', class_='objectcontainer')
itshousingList = []

for list in listings:
    listingTitle = list.find('span', class_="street").text
    listingLocation = list.find('span', class_="location").text
    listingPrice = list.find('span', class_="obj_price").text
    listingPrice = listingPrice.replace("\t", "").replace("\r", "").replace("\n", "")
    listingPrice = listingPrice.strip()
    
    if listingLocation == "Utrecht":
        ListingInfo = [listingTitle, listingLocation, listingPrice]
        itshousingList.append(ListingInfo)

print(itshousingList)