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
col1.image('C:/Users/ragha/raghad.artistry/image.jpg')
col2.write(f"Biography: {js['GraphProfileInfo']['info']['biography']}")
col2.write(f"Is Business Account: {js['GraphProfileInfo']['info']['is_business_account']}")
col2.write(f"Number Of Posts: {js['GraphProfileInfo']['info']['posts_count']}")

      
#number of likes
df['likes']=df['edge_media_preview_like'].apply(lambda x: x['count'])
#number of comments
df['comments']=df['edge_media_to_comment'].apply(lambda x: x['count'])
#transform the timestamp to datetime object
df['date']=df['taken_at_timestamp'].apply(datetime.fromtimestamp)
#extract dayofweek, month, week, year, ym 
df['dayofweek']=df['date'].dt.dayofweek
df['month']=df['date'].dt.month
df['week']=df['date'].dt.week
df['year']=df['date'].dt.year
df['ym']=df['year'].astype(str)+df['month'].astype(str)
engagement_rate=(((df['likes'].sum()+df['comments'].sum())/len(df))/js['GraphProfileInfo']['info']['followers_count'])*100
col2.write(f"Average Posts Per Month: {round(df.groupby('ym').size().mean(),2)}")
col2.write(f"Engagement Rate: {round(engagement_rate,2)}%")

x=df.groupby('dayofweek').size()
st.subheader('Number Of Posts Per Week-Day')
st.bar_chart(pd.DataFrame(x).rename(columns={0: 'Number Of Posts'}))
x=df.groupby('month').size()
st.subheader('Number Of Posts Per Month')
st.bar_chart(pd.DataFrame(x).rename(columns={0: 'Number Of Posts'}))

#for n in js['GraphProfileInfo']["info"]["followers_count"]:
 #   print(n)
 #

df.shape

list(df)
df.head(3)
