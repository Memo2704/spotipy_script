import os
import sys
import json
import spotipy
from spotipy import util

# main.py imports
from main import show_tracks, get_artist

# Getting the username from terminal
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python %s [username]" % (sys.argv[0]))
    sys.exit()
# user id = '9ta1ql0tgpzhg5cwbz58z2yr9'

# Erase the cache and prompt for user permissions.
try:
    scope = 'user-top-read'
    token = util.prompt_for_user_token(username, scope)
except:
    scope = 'user-top-read'
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

# Create the spotify object
sp = spotipy.Spotify(auth=token)
user = sp.current_user()
display_name = user['display_name']
followers = user['followers']['total']


while True:
    print()
    print(">>> Welcome to Spotipy by Tony Arteaga, " + display_name + "!")
    print(">>> You have " + str(followers) + " followers.")
    # print(">>> You have x_number of liked songs!") This can be another feature
    print()
    print("0 - See how many songs you have in your playlists?")
    print("1 - See your top tracks!")
    print("2 - See your top artists!")
    print("3 - See top tracks of any artist you want!")
    print("4 - Exit")

    choice = input("Your choice: ")
    if choice == "0":
        if token:
            sp = spotipy.Spotify(auth=token)
            playlists = sp.user_playlists(username)
            for playlist in playlists['items']:
                if playlist['owner']['id'] == username:
                    print()
                    print(playlist['name'])
                    print('  total tracks', playlist['tracks']['total'])
                    results = sp.playlist(playlist['id'],
                                          fields="tracks,next")
                    tracks = results['tracks']
                    show_tracks(tracks)
                    while tracks['next']:
                        tracks = sp.next(tracks)
                        show_tracks(tracks)
        else:
            print("Can't get token for", username)

    elif choice == "1":
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            ranges = ['short_term', 'medium_term', 'long_term']
            for range in ranges:
                print("range:", range)
                results = sp.current_user_top_tracks(time_range=range, limit=50)
                for i, item in enumerate(results['items']):
                    print(i, item['name'], '//', item['artists'][0]['name'])
                print()

        else:
            print("Can't get token for", username)

    elif choice == "2":
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            ranges = ['short_term', 'medium_term', 'long_term']
            for range in ranges:
                print("range:", range)
                results = sp.current_user_top_artists(time_range=range, limit=50)
                for i, item in enumerate(results['items']):
                    print(i, item['name'])
                print()
        else:
            print("Can't get token for", username)

    elif choice == "3":
        prompt = input("Enter the name of an artist: ")
        artist = get_artist(prompt, sp=sp)
        artist_id = artist['id']
        urn = 'spotify:artist:{}'.format(artist_id)
        response = sp.artist_top_tracks(urn)
        print(">>> Top songs for {}".format(artist['name']))
        for track in response['tracks']:
            print(track['name'])

    elif choice == "4":
        print("Run this script again if you want to interact with me!")
        print("Bye.")

    else:
        print("Please insert a correct option.")