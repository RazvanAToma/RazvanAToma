from bs4 import BeautifulSoup
import requests


# Specifying the url of the webpage I want to scrape
url = "https://www.gulesider.no/lier/personer"
 

try:
    # Makes the script not translate the scraped value
    headers = {"Accept-Language": "en-US,en;q=0.5"}

    source = requests.get(url, headers=headers)
    
    # Checks if the website url is valid
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text, "html.parser")
    
    people = soup.find('div', class_="MuiGrid-root MuiGrid-item css-1wxaqej").find_all("li")
    print(len(people))
    
    for person in people:
        
        name = person.find("h3", class_="MuiTypography-root MuiTypography-h6 css-j40wv6").a.text
        print(name)

        try:
            address = person.find("p", class_="MuiTypography-root MuiTypography-body1 css-1u09hd5\n").text
            print(address)



        except Exception as _:
            print("No address listed\n")

    
except Exception as e:
    print(e)