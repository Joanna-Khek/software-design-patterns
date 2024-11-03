class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        
    def serialize(self, serializer):
        serializer.start_object(object_name='song', object_id=self.song_id)
        serializer.add_property(name='title', value=self.title)
        serializer.add_property(name='artist', value=self.artist)
        