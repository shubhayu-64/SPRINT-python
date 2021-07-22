from lyrics_extractor import SongLyrics
import config

if __name__ == "__main__":
    print("Lyrics Finder for Clinify-Open-Sauce by Shubhayu Majumdar")

    client = SongLyrics(config.key, config.engine_id)

    song = input("Enter you song name: ")
    print("\n")

    data = client.get_lyrics(song)

    print(data['title'], "\n")
    print(data['lyrics'])
