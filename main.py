import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))


def get_artist(name, sp):
    """
    This will obtain some data of the searched artist.
    :param name:
    :param sp:
    :return: name of the artist
    """
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


def show_artist_albums(artist):
    """
    This will look for the albums release by the previously defined artist.
    :param artist:
    :return: names of the albums
    """
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    seen = []  # to avoid dups
    albums.sort(key=lambda album: album['name'].lower())
    for album in albums:
        name = album['name']
        if name not in seen:
            print((' ' + name))
            seen.append(name)
    return seen


def get_top_tracks(album_id):
    urn = 'spotify:artist:' + str(album_id)
    response = sp.artist_top_tracks(urn)
    for track in response['tracks']:
        print(track['name'])


def get_album_tracks(album_name):
    # Tengo que hacer que el album name coincida con el album que quiera buscar, por ejemplo si es
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.search(q="album:" + album_name, type="album")

    # get the first album uri
    album_id = results['albums']['items'][0]['uri']

    # get album tracks
    tracks = sp.album_tracks(album_id)
    for track in tracks['items']:
        print(track['name'])


# def show_album_tracks(album):
#     tracks = []
#     results = sp.album_tracks(album['id'])
#     tracks.extend(results['items'])
#     while results['next']:
#         results = sp.next(results)
#         tracks.extend(results['items'])
#     for track in tracks:
#         print('  ', track['name'])
#         print()
#         print(track)

