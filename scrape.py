import pandas as pd
import spotipy
import spotipy.util as util
token = util.prompt_for_user_token("test",client_id='5a04b9f52b5142dfa5df57ea2d3d4980',client_secret='99c37e47707349b7bbd16ee79b6f663f',redirect_uri='http://localhost/')

sp = spotipy.Spotify(auth=token)
sp.trace=False
playlist = sp.user_playlist("12715792", "spotify:user:12715792:playlist:73tOKF141FcxCXCwfCBiIu")
songs = playlist["tracks"]["items"]
ids = []
for i in range(len(songs)):
    ids.append(songs[i]["track"]["id"])

features = sp.audio_features(ids)
for i in range(len(songs)):
    features[i]["artists"] = (songs[i]["track"]["artists"][0]["name"])
    features[i]["name"] = (songs[i]["track"]["name"])
print (features[1])
cols_to_keep =['artists','name','acousticness','danceability','energy','instrumentalness','liveness','loudness','mode','speechiness','tempo','valence','track_href']
df = pd.DataFrame(features)
df[cols_to_keep].to_csv('tlop.csv',sep=';')
