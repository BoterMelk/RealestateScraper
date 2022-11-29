from bs4 import BeautifulSoup
import requests


def itshousing():
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
        
    return(itshousingList)



print(itshousing()) 
allResults = []
allResults = allResults.append(itshousing())
print("test")
print(allResults)
