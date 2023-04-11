from bs4 import BeautifulSoup
import requests


# Specifying the url of the webpage I want to scrape
url = "https://open.spotify.com/playlist/5ojUdiXpR0sRIivD9NnunT"


try:
    # Makes the script not translate the scraped value
    headers = {"Accept-Language": "en-US,en;q=0.5"}

    source = requests.get(url, headers=headers)
    
    # Checks if the website url is valid
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text, "html.parser")
    
    songs = soup.find('div', class_="JUa6JJNj7R_Y3i4P8YUX").find_all('div')

    print(songs)
    
    '''
    for song in songs:

        name = song.find("td", class_="titleColumn").a.text
        
        rank = movie.find("td", class_="titleColumn").get_text(strip=True).split(".")[0]

        year = movie.find("td", class_="titleColumn").span.text.strip("()")

        rating = movie.find("td", class_="ratingColumn imdbRating").strong.text

        print(rank, name, year, rating)
    '''

except Exception as e:
    print(e)