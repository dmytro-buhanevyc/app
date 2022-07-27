
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
import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
        page_title="TCA Data Lab",
        page_icon=":sunflower:",

    )

st.write("# Keyword search")



HtmlFile = open("https://raw.githubusercontent.com/dmytro-buhanevyc/app/main/various/german_keywords.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code)

progress_bar = st.sidebar.progress(0)
# We clear elements by calling empty on them.
progress_bar.empty()
