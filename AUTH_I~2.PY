
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# setup env vars from EnvVarMaster:
CLIENT_ID = os.environ.get('CLIENT_ID', 'Client ID does not exist')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET', 'Client Secret does not exist')
REDIRECT_URI = os.environ.get('REDIRECT_URI', 'Redirect URI does not exist')
USER_ID = os.environ.get('USER_ID', 'User ID does not exist')

# print the env vars to ensure they are correctly setup:
print(f"The CLIENT_ID is: {CLIENT_ID}")
print(f"The CLIENT_SECRET is: {CLIENT_SECRET}")
print(f"The REDIRECT_URI is: {REDIRECT_URI}")
print(f"The USER_ID is: {USER_ID}")

# Set your credentials and the required scope
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private"
))

# this is where you use the 'id' you got from the previous step
# now you can use this user_id to create a new playlist
playlist = sp.user_playlist_create(USER_ID, "New Playlist", public=False)
print(f"New Playlist ID: {playlist['id']}")
