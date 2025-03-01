from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Connect to the "chinook" database
db = create_engine("postgresql:///chinook")

meta = MetaData()

# Reflect existing tables (ONLY if tables already exist)
meta.reflect(bind=db)

# If tables do NOT exist and you need to define them, use:
artist_table = Table(
    "artist", meta,   
    Column("artist_id", Integer, primary_key=True),
    Column("name", String),  
    extend_existing=True  # Allow redefining existing tables
)

album_table = Table(
    "album", meta,
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist.artist_id")),
    extend_existing=True
)

track_table = Table(
    "track", meta,
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album.album_id")),
    Column("media_type_id", Integer),
    Column("genre_id", Integer),
    Column("composer", String),
    Column("milliseconds", Integer),  # Removed "|"
    Column("bytes", Integer),  # Removed "|"
    Column("unit_price", Float),
    extend_existing=True
)

# Make the connection
with db.connect() as connection:
    
    # Query 1 - Select all records from the "artist" table
    select_query = artist_table.select()
    
    results = connection.execute(select_query)
    
    for result in results:
        print(result)  # Should print artist records
