
from hashlib import new
from urllib import response
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from ipywidgets import widgets
import json # library to handle JSON files
import requests 
import folium # map rendering library
from streamlit_folium import folium_static
from folium.features import GeoJsonPopup, GeoJsonTooltip
import geopandas as gpd
import branca.colormap as cm
import tweepy
import time
from datetime import date, datetime
from pandas_profiling import ProfileReport
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
import urllib.request,sys,time
from newspaper import Article
from textblob import TextBlob
import nltk
nltk.download('punkt')
import csv
import requests
import sys
import jsonpickle
import os
import snscrape.modules.twitter as twitterScraper
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import re  
import json
import snscrape.modules.twitter as sntwitter

import streamlit as st
st.set_page_config(
        page_title="TCA Data Lab",
        page_icon=":running:",

    )

st.write("# TCA News Analysis")

progress_bar = st.sidebar.progress(0)
# We clear elements by calling empty on them.
progress_bar.empty()

#IMPORTING DATASET
#French
url="https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/countries/france_news.json"
s=requests.get(url).content
france_news=pd.read_json(io.StringIO(s.decode('utf-8')))
#German
url="https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/countries/germany_news.json"
s=requests.get(url).content
germany_news=pd.read_json(io.StringIO(s.decode('utf-8')))
#German
url="https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/countries/italy_news.json"
s=requests.get(url).content
italy_news=pd.read_json(io.StringIO(s.decode('utf-8')))
    
#IMPORTING DATASET

global_news = pd.concat([france_news, germany_news, italy_news], keys=['France', 'Germany', 'Italy']).reset_index()

global_news_daily=pd.concat([france_news, germany_news, italy_news], keys=['France', 'Germany', 'Italy']).reset_index()
global_news_daily['date'] = pd.to_datetime(global_news['date']).dt.normalize()



#global_news.columns = global_news.columns.str.replace(' ', '')

global_news_grouped = global_news_daily.groupby(['level_0', 'date']).size().to_frame('Count').reset_index()



#OLD#


hover = alt.selection_single(
    fields=["date"],
    nearest=True,
    on="mouseover",
    empty="none",
)

#Example of data#
highlight = alt.selection(type='single', on='mouseover', 
                        fields=['Username'], nearest=True)

selection = alt.selection_multi(on='click', fields=['level_0'], bind='legend', empty='all')
tooltips2 = (
alt.Chart(global_news_grouped)
.mark_circle(size=60)
.encode(
x="yearmonthdate(date)",
y="Count",
color="level_0", 
opacity=alt.condition(hover, alt.value(0.5), alt.value(0)),
tooltip=[
    alt.Tooltip("date", title="Date"),
    alt.Tooltip("Count", title="Tweets"),
    alt.Tooltip("level_0", title="Country"),

],
)
.add_selection(hover)
)

st.write(" Data below shows mentions of Ukraine in the foreign media.")

expander = st.expander("How it's done")
expander.write("""
    TCA selects the biggest news sources on Twitter from a number of countries and then extracts all tweets that
    mention Ukraine in their repsective languages. The text is then pre-processed and the aggregated content is visualized below.""")

chart = (
    alt.Chart(global_news_grouped, width=750,
    height=350)
    .mark_area(opacity=0.2)
    .encode(
        x=alt.X("yearmonthdate(date)", title="Date"),
        y=alt.Y("Count:Q", stack=None),
        color="level_0:N",
        opacity=alt.condition(selection, alt.value(0.5), alt.value(0.1))
    ).add_selection(
selection
)
).interactive()
st.altair_chart(chart +tooltips2, use_container_width=True)
st.button("Reset")




#INSERTINGTABLE AND SELECTIONS



counted_global = global_news.groupby(['date', 'level_0', 'Username', 'Followers', 'content', 'Likes', 'Retweets']).size().to_frame('Count').reset_index()
global_news = counted_global.set_index('level_0', drop=False)
global_news.content = global_news.content.str.wrap(60)
global_news.content = global_news.content.apply(lambda x: x.replace('\n', '<br>'))



def showtable():
    return global_news.set_index("level_0")

try:
    df = showtable()
    media2 = st.multiselect(
            "View by country", list(global_news.index.unique())
    )        
    if not media2:
        st.write()
    else:
        global_news = global_news.loc[media2]
        global_news_short = global_news.drop(columns = [ 'Count', 'level_0'])
        st.write("####  ", global_news_short) #this creates the table
        fig=px.scatter(global_news, x="Likes", y="Retweets", 
        size="Likes", color="Username", color_discrete_sequence=px.colors.qualitative.Bold, 
        custom_data=["Username", 'Likes', 'date', 'content'],
            log_x=False, size_max=30)
        fig.update_traces(
        hovertemplate="<br>".join([
        "Name: %{customdata[0]}",
        "Likes: %{customdata[1]}",
        "Date: %{customdata[2]}",
        "Content: %{customdata[3]}",
        
    ])
)
        fig.update_layout(width = 900, height = 550,
        title = "Ukraine in the news <br><sup>Based on latest tweets from each outlet</sup>",         xaxis_title="Likes",
        yaxis_title="Retweets",
        legend_title="Media Source",)
        today = date.today()
        fig.add_annotation(
            text = (f"USAID-TCA | {today}<br>Source: TCA")
            , showarrow=False
            , x = 0
            , y = -0.15
            , xref='paper'
            , yref='paper' 
            , xanchor='left'
            , yanchor='bottom'
            , xshift=-1
            , yshift=-5
            , font=dict(size=10, color="lightgrey")
            , align="left"
            ,)

        st.plotly_chart(fig, use_container_width=False)

        #st.altair_chart(b, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )

