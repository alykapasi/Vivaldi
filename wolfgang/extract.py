## (E)xtract from spotify REST api
# import relevant libraries

## NEED TO FIX : UNABLE TO EXTRACT RECENT DATA


import datetime
import json
import pandas
import requests
import creds

song_name_list = []
artist_name_list = []
played_at_list = []

if __name__ == "__main__":

    hdrs = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {creds.AUTH_TOKEN}"
    }

    yday = datetime.datetime.now() - datetime.timedelta(days=1)
    yday_unix = int(yday.timestamp()) * 1000

    r = requests.get(f"https://api.spotify.com/v1/me/player/recently-played?before={yday_unix}", headers=hdrs)


    data = r.json()
    data_pretty = json.dumps(data, sort_keys = True, indent = 4)
    print(data_pretty)
    

    for song in data['items']:
        song_name_list.append(song['track']['name'])
        artist_name_list.append(song['track']['album']['artists'][0]['name'])
        played_at_list.append(song['played_at'])

    track_dict = {
        'title' : song_name_list,
        'artist' : artist_name_list,
        'played_at' : played_at_list,
    }

    df = pandas.DataFrame(track_dict, columns=['title' ,'artist' ,'played_at' ,'timestamp'])

    print(df)