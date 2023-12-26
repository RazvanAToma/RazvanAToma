from bs4 import BeautifulSoup
import requests, openpyxl



# Specifying the url of the webpage I want to scrape
url = "https://music.youtube.com/playlist?list=PLKHiCA-1l2AICuuzKizEFDId2agTBvu8-"


try:
    # Makes the script not translate the scraped value
    headers = {"Accept-Language": "en-US,en;q=0.5"}

    source = requests.get(url, headers=headers)
    
    # Checks if the website url is valid
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text, "html.parser")
    
    songs = soup.find('ytmusic-responsive-list-item-renderer', class_="style-scope ytmusic-playlist-shelf-renderer")
#soup.find('tbody', class_="lister-list").find_all("tr")

    print(songs)

except Exception as e:
    print(e)