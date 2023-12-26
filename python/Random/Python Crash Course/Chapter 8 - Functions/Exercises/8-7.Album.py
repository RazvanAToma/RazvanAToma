
def make_album(artist_name, album_name, tracks=""):
    album = {"Artist Name": artist_name.title(), "Album Name": album_name}
    if tracks:
        album = {"Artist Name": artist_name.title(), "Album Name": album_name, "Tracks": tracks}
    return album
    
print(make_album("drake", 21))
print(make_album("drake", 21, 70))
