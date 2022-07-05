
import enum
import re
from collections import Counter
import string
import spacy.attrs
from dframcy import DframCy
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop
import fr_core_news_sm
import en_core_web_sm
import spacy
from datetime import date
import winsound
import snscrape.modules.twitter as sntwitter
import json
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk import sent_tokenize, word_tokenize
import snscrape.modules.twitter as twitterScraper
import os
import jsonpickle
import sys
import requests
import csv
from hashlib import new
from urllib import response
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from ipywidgets import widgets
import json  # library to handle JSON files
from geopy.geocoders import Nominatim
import requests
import folium  # map rendering library
from streamlit_folium import folium_static
from folium.features import GeoJsonPopup, GeoJsonTooltip
import geopandas as gpd
import branca.colormap as cm
import tweepy
import time
from datetime import date, datetime
from ipywidgets import interactive, HBox, VBox
import inspect
import textwrap
from collections import OrderedDict
import io
from IPython.display import display
from streamlit.logger import get_logger
import panel as pn
from urllib.error import URLError
from bs4 import BeautifulSoup
import urllib.request
import sys
import time
from newspaper import Article
from textblob import TextBlob
import nltk
from plotly import graph_objects
nltk.download('punkt')
nltk.download('punkt')
nltk.download('wordnet')
duration = 1000  # milliseconds
freq = 440  # Hz



st.set_page_config(
        page_title="TCA Data Lab",
        page_icon=":sunflower:",

    )

st.write("# Eurointegration")

progress_bar = st.sidebar.progress(0)
# We clear elements by calling empty on them.
progress_bar.empty()



url="https://raw.githubusercontent.com/dmytro-buhanevyc/app/main/eurointegration/eu_deputies.csv"
s=requests.get(url).content
eu_deputies=pd.read_csv(io.StringIO(s.decode('utf-8')))

### Full Votes ###
#eu_deputies = pd.read_csv(r"C:\Users\dbukhanevych\Downloads\eu_deputies.csv")


######## SPLITTING TO FULL NAME #########

#eu_deputies['fullName'] = eu_deputies['fullName'].str.split(n=1).str[1]
#eu_deputies = eu_deputies.rename(columns={"fullName": "Name"})

eu_deputies['Name'] = eu_deputies['Name'].str.title()
eu_deputies['Name'] = eu_deputies['Name'].str.replace('[#,@,&,-]', ' ')
eu_deputies['Name'] = eu_deputies['Name'].str.normalize(
    'NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
eu_deputies['nationalPoliticalGroup'] = eu_deputies['nationalPoliticalGroup'].str.title()
eu_deputies['nationalPoliticalGroup'] = eu_deputies['nationalPoliticalGroup'].str.replace(
    '[#,@,&,-]', ' ')
eu_deputies['nationalPoliticalGroup'] = eu_deputies['nationalPoliticalGroup'].str.normalize(
    'NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

########### TO CSV##########

#eu_deputies.to_csv("eu_deputies.csv")



###################


url="https://raw.githubusercontent.com/dmytro-buhanevyc/app/main/eurointegration/FullVotes_Ukraine.csv"
s=requests.get(url).content
eu_votes=pd.read_csv(io.StringIO(s.decode('utf-8')))

#eu_votes = pd.read_csv(
#    r"C:\Users\dbukhanevych\Anaconda3\envs\TCA\hello\Academic\FullVotes_Ukraine.csv")

eu_votes["Name"] = eu_votes["Name"].str.split(",")
eu_votes = eu_votes.explode("Name")
eu_votes["Name"] = eu_votes["Name"].str.replace(
    '^(\w+)\s+(\w+)(|.+|)', r'\1\g<3>')
eu_votes['Name'] = eu_votes['Name'].str.replace('[#,@,&,-]', ' ')
eu_votes['Name'] = eu_votes['Name'].str.normalize(
    'NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
eu_votes['Name'] = eu_votes['Name'].str.strip()


df3 = eu_deputies.merge(eu_votes, left_on='Name', right_on='Name')[
    ['country', 'Name', 'politicalGroup', 'nationalPoliticalGroup', 'Vote_y']]

# eu_votes.to_csv("eu_votes.csv")
# df3['country'].value_counts()

df4 = df3.groupby(['Vote_y', 'country', 'politicalGroup', 'nationalPoliticalGroup', 'Name'])[
    "Name"].count().reset_index(name="votes")


# FRANCE ###########3
df_eu_no = df4.drop(df4[df4.Vote_y == 'Yes'].index)


#france_eu_votes = pd.read_csv(
#    r"C:\Users\dbukhanevych\Anaconda3\envs\TCA\hello\Academic\france_eu_votes.csv")


#france_eu_votes['Vote'].value_counts()


# df4 = france_eu_votes.groupby(['politicalGroup', 'nationalPoliticalGroup', 'Name', 'Vote'])[
#    "Name"].count().reset_index(name="votes")


color_discrete_map = {'Yes': '#44878F', 'No': '#FF8591',
                      'Abstained': '#EFAAA3', 'No Vote': '#b784a3', '(?)': '#2e4962'}


fig = px.sunburst(df4, path=['country', 'politicalGroup', 'nationalPoliticalGroup',  'Name'], values='votes',
                  color='Vote_y',  color_discrete_map=color_discrete_map)
fig.update_layout(width=1200, height=800,
                  title="Ukraine & Moldova EU Candidate status <br> <sup>Votes in the EU Parliament by French MPs</sup>",
                  )
today = date.today()
fig.update_traces(textinfo='label')
fig.add_annotation(
    text=(f"USAID-TCA | {today}<br>Source: TCA"), showarrow=False, x=0, y=-0.15,
    xref='paper', yref='paper', xanchor='left', yanchor='bottom',
    xshift=-1, yshift=-5, font=dict(size=10, color="lightgrey"), align="left",)
fig
fig.show()
