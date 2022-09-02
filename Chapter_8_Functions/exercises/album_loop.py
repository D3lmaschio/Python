def make_album(artist, album, songs=None):
    """
    Make an dictionary of album with given arguments
    and returns this dictionary.
    """
    if songs:
        return {artist: album, 'songs': songs, }
    else:
        return {artist: album, }


prompt_end = "\nEnter 'q' to quit."
prompt_artist = "Enter the artist:\n> "
prompt_album = "Enter the album:\n> "
prompt_songs = "Enter the number of songs in the album:\n> "

while True:
    print(prompt_end)
    inp_artist = input(prompt_artist)

    if inp_artist == 'q':
        break

    print(prompt_end)
    inp_album = input(prompt_album)

    if inp_album == 'q':
        break

    print(prompt_end)
    inp_songs = int(input(prompt_songs))

    if inp_songs == 'q':
        break

    print("Making your album...")
    print(make_album(inp_artist, inp_album, inp_songs))

    repeat = input("\nDo you want to make another album? (yes/no) \n> ")

    if repeat != 'yes':
        print("\nGoodbye!")
        break
        