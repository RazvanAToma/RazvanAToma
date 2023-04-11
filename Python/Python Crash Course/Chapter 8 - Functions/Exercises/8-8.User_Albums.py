
def make_album(artist_name, album_name, tracks=""):
    album = {"Artist Name": artist_name.title(), "Album Name": album_name}
    if tracks:
        album = {"Artist Name": artist_name.title(), "Album Name": album_name, "Tracks": tracks}
    return album

while True:
    print("If you want to quit, input 'quit' at any time.")
    
    artist_name = input("Input artist name:")
    if artist_name == "quit":
        break

    album_name = input("Input album name:")
    if album_name == "quit":
        break

    tracks = input("Input amount of tracks in album:")
    if tracks == "quit":
        break

    print(make_album(artist_name=artist_name, album_name=album_name, tracks=tracks))
