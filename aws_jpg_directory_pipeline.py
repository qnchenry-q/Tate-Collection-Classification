import pandas as pd
import numpy as np
from PIL import Image
import urllib.request
import io
import requests
import validators
import os

if __name__ == '__main__':

  works_raw = pd.read_csv('data/collection/artwork_data.csv')

  works_raw['ByJMWT'] = works_raw['artist'] == 'Turner, Joseph Mallord William'

  JMWT = works_raw['ByJMWT'] == True
  Other_artists = works_raw['ByJMWT'] == False

  JMWT_works = works_raw[JMWT]
  Other_artist_works = works_raw[Other_artists]

  JMWT_art_urls = JMWT_works['thumbnailUrl'].to_numpy()
  Other_artist_urls = Other_artist_works['thumbnailUrl'].to_numpy()

  artists_raw = pd.read_csv('data/collection/artist_data.csv')

  name_gender = artists_raw.iloc[:,[1,2]]
  works_with_gender = works_raw.merge(name_gender, how = 'left', left_on = 'artist', right_on = 'name')

  male_bool = works_with_gender.gender == 'Male'
  female_bool = works_with_gender.gender == 'Female'


  F_set = works_with_gender[female_bool]
  F_art_urls = F_set['thumbnailUrl'].to_numpy()

  M_set = works_with_gender[male_bool]
  M_art_urls = M_set['thumbnailUrl'].to_numpy()

  os.mkdir('JMWT_vs_Other')
  os.mkdir('Male_vs_Female')

  def clean_url_array (array):
    res = []
    for url in array:
        if type(url)== str:
            valid = validators.url(url)
            if valid == True:
                res.append(url)
            else:
                continue
        else:
            continue
    return res

  import time
  def array_to_folder (array, parent_dir_name, dir_name):
    os.mkdir(dir_name)
    for i, url in enumerate(array):
        time.sleep(.5)
        img_id = str(i)
        try:
            urllib.request.urlretrieve(url, f"{parent_dir_name}/{dir_name}/{img_id}.jpg")
        except:
            continue

  JMWT_clean_urls = clean_url_array(JMWT_art_urls)
  Other_artist_clean_urls = clean_url_array(Other_artist_urls)
  F_art_clean_urls = clean_url_array(F_art_urls)
  M_art_clean_urls = clean_url_array(M_art_urls)

  array_to_folder(JMWT_clean_urls, 'JMWT_vs_Other','By JMWT')
  array_to_folder(Other_artist_clean_urls, 'JMWT_vs_Other','By another artist')
  array_to_folder(F_art_clean_urls, 'Male_vs_Female','By Female')
  array_to_folder(M_art_clean_urls, 'Male_vs_Female','By Male')

