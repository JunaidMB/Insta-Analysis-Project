import streamlit as st
import requests
import numpy as np
import pandas as pd
import os
import json
import pandas as pd
import numpy as np
import re
from datetime import datetime
import string
import json
import io

st.title('Raghads Attempt at Instagram Dashboard')


username = 'raghad.artistry'

js = json.load(open('C:/Users/ragha/raghad.artistry/raghad.artistry.json', encoding='utf-8'))
js.keys()

js['GraphProfileInfo']

df=pd.DataFrame(js['GraphImages'])
df

st.write(f"Full Name: {js['GraphProfileInfo']['info']['full_name']}")
#get the profile_pic_url from json
prof_pic=js['GraphProfileInfo']['info']['profile_pic_url']
#download the image in a folder called static I created
response = requests.get(prof_pic)
filename="C:/Users/ragha/raghad.artistry/image.jpg"
with open(filename, "wb") as f:
    f.write(response.content)

col1, col2 = st.beta_columns(2)
col1.image(filename)
col2.write(f"Biography: {js['GraphProfileInfo']['info']['biography']}")
col2.write(f"Is Business Account: {js['GraphProfileInfo']['info']['is_business_account']}")
col2.write(f"Number Of Posts: {js['GraphProfileInfo']['info']['posts_count']}")
         
for n in js['GraphProfileInfo']["info"]["followers_count"]:
    print(n)