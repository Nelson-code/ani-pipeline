import pandas as pd
import os
from datetime import datetime
import requests

def extract(access_token):
    url = "https://api.spotify.com/v1/artists/4zCH9qm4R2DADamUHMCa6O/top-tracks?market=IN"

    # Headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

def transform(profile_data):
    song=[]
    pop_no=[]
    for ind in range(0,len(profile_data['tracks'])):
        song.append(profile_data['tracks'][ind]['name'])
        pop_no.append(profile_data['tracks'][ind]['popularity'])
    df=pd.DataFrame(data={"Name":song,"Popularity":pop_no})
    df.sort_values(by="Popularity",ascending=False,inplace=True)
    return df

def load(clean_data):
    directory='/home/skullcrusher/extract'
    os.makedirs(directory,exist_ok=True)
    file_name=f"load_output_{datetime.now()}
    path=os.path.join(directory,file_name)
    df.to_csv(path,index=False)

def etl():
    access_token = "access token"  # Replace with your actual access token
    raw_data = extract(access_token)
    clean_data=transform(raw_data)
    load(clean_data)

if __name__=="__main__":
    etl()