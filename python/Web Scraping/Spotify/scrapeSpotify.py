from bs4 import BeautifulSoup
import requests, openpyxl


# # Creating excel file
# excel = openpyxl.Workbook()
# sheet = excel.active
# sheet.title = "Top Rated Movies"
# print(excel.sheetnames)
# sheet.append(["Movie Rank", "Movie Name", "Year of Release", "IMDB Rating"])


# Specifying the url of the webpage I want to scrape
url = "https://open.spotify.com/collection/tracks?flow_id=6b2bfab3-b24f-4ff9-979e-07f1fea0d293%3A1684864752"


try:
    # Makes the script not translate the scraped value
    headers = {"Accept-Language": "en-US,en;q=0.5"}

    source = requests.get(url, headers=headers)
    
    # Checks if the website url is valid
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text, "html.parser")
    

    songs = soup.find("div", class_="JUa6JJNj7R_Y3i4P8YUX")

    print(songs)

except Exception as e:
    print(e)