# Import the necessary models
from app.models import Playlist, Song, db

# Create your playlists and songs
playlist1 = Playlist(title='Playlist 1')
playlist2 = Playlist(title='Playlist 2')

song1 = Song(title='Song 1')
song2 = Song(title='Song 2')
song3 = Song(title='Song 3')

# Add the playlists and songs to the session
db.session.add_all([playlist1, playlist2, song1, song2, song3])
db.session.commit()

# Associate the songs with the playlists
playlist1.songs.append(song1)
playlist1.songs.append(song2)
playlist2.songs.append(song2)
playlist2.songs.append(song3)

# Commit the changes to the session
db.session.commit()
