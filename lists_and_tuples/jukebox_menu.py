from nested_data import albums

# Constants for indexing
SONGS_LIST = 3
SONG_TITLE = 1
while True:
    # User input for choosing an album
    # Displays possible album choices
    print("Please choose your album (Invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    # Check if choice is valid
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST]
        print(songs_list)
    else:
        break

    # User input for choosing a song
    # Print out possible song choices
    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    # Check if song choice is valid, print out song title
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE]
    else:
        break
    print("Playing {}".format(title))
    print("=" * 40)

