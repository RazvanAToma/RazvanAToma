import webbrowser

user_input = input("What website do you want to open?\n").lower()

websites = {
    "youtube": "https://youtube.com"
    }

webbrowser.open(websites[user_input]) # Go to website
