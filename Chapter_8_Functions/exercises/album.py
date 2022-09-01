def make_album(artist, album, songs=None):
    if songs:
        return {artist: album, 'songs': songs, }
    else:
        return {artist: album, }


print(make_album("Metallica", "Master Of Puppets"))
print(make_album("Metallica", "Ride The Lightning"))
print(make_album("Frank Sinatra", "That's Life", "That's Life"))
