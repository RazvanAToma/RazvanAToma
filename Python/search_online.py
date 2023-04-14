import webbrowser
import sys

url = "https://www.google.com/search?q="

valid_websites = [
    "reddit.com",
    "stackoverflow.com",
    "stackexchange.com",
    "medium.com"
]

# Windows
brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'

def create_filter():
    filter = "("
    for index, website in enumerate(valid_websites):
        filter += "site:" + website
        if index == len(valid_websites) -1:
            filter += ")"
        else:
            filter += " OR "
    return filter

def create_query():
    query = sys.argv[1:]
    return " ".join(query)

def create_url():
    if len(sys.argv[1:]) == 0:
        print("Please inter a valid search query")
    else:
        final_url = url + create_query() + create_filter()
        webbrowser.get(brave_path).open(final_url)

create_url()


