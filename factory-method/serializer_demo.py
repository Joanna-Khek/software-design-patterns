import json
import xml.etree.ElementTree as et
import xml.dom.minidom

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        
class SongSerializer:
    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(song_info)
        
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            
            song_info_parsed = et.tostring(song_info, encoding='unicode')
            song_info_reparsed = xml.dom.minidom.parseString(song_info_parsed)
            return song_info_reparsed.toprettyxml(indent="  ")
        
        else:
            raise ValueError(format)
        
            