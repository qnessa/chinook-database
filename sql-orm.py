from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "artist" table
class artist(base):
    __tablename__ = "artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class-based model for the "Album" table
class album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))

# create a class-based model for the "track" table
class track(base):
    __tablename__ = "track"
    trackId = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.album_id"))
    mediaType_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unitPrice = Column(Float)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()
# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the "Artist" table
artists = session.query(artist)
for artist in artists:
    print(artist.artist_id, artist.name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
artists = session.query(artist)
for artist in artists:
    print(artist.name)

# Query 3 - select only "Queen" from the "artist" table
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "artist_id" #51 from the "Artist" table
artist = session.query(Artist).filter_by(artist_id=51).first()
print(artist.ArtistId, artist.name, sep=" | ")

# Query 5 - select only the albums with "artist_id" #51 on the "album" table
albums = session.query(album).filter_by(artistId=51)
for album in albums:
    print(album.album_id, album.title, album.artist_id, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "track" table
tracks = session.query(track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.Track_id,
        track.Name,
        track.Album_id,
        track.MediaType_id,
        track.Genre_id,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
