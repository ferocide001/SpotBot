import spotipy
from spotipy.oauth2 import SpotifyOAuth

# variables
tracks = []
playlistTracks = []

# Authentication
username = 'ferocide001'
cid = ''
secret = ''
redirect_url = 'http://localhost:9000'
scope = "user-modify-playback-state user-read-private ugc-image-upload playlist-modify-private playlist-read-private playlist-modify-public playlist-read-collaborative user-read-private user-read-email user-read-playback-state user-modify-playback-state user-read-currently-playing user-library-modify user-library-read user-read-playback-position user-read-recently-played user-top-read app-remote-control streaming user-follow-modify user-follow-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=cid, client_secret=secret, redirect_uri=redirect_url))

# main code
recentTracks = sp.current_user_recently_played(limit=50)

# get tracks recently listened to
for _ in recentTracks['items']:
    tracks.append(_['track']['uri'])

# get tracks in playlist
playlist = sp.playlist_items("spotify:playlist:5pd2lMvyOBC0wi2jo4XgyY?si=c4200da5573746c2")
for _ in playlist['tracks']['items']:
    playlistTracks.append(_['track']['uri'])

# delete old tracks
for track in playlistTracks:
    if track not in tracks:
        trackid = track.split("track:", 1)[1]
        trackid = [trackid]
        print(track)
        result = sp.playlist_remove_all_occurrences_of_items('5pd2lMvyOBC0wi2jo4XgyY', trackid)
        print(f'deleted {track}')
    else:
        print(f'alerady listened to {track}')
