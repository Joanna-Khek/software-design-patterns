import json
import xml.etree.ElementTree as et
import xml.dom.minidom

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        
class SongSerializer:
    # Client component of the pattern
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer(song)
    
# Creator component
def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)

# Product components
def _serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)

def _serialize_to_xml(song):
    song_info = et.Element('song', attrib={'id': song.song_id})
        
    title = et.SubElement(song_info, 'title')
    title.text = song.title
    
    artist = et.SubElement(song_info, 'artist')
    artist.text = song.artist
    
    song_info_parsed = et.tostring(song_info, encoding='unicode')
    song_info_reparsed = xml.dom.minidom.parseString(song_info_parsed)
    return song_info_reparsed.toprettyxml(indent="  ")