from sqlite3 import Date
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from ipywidgets import widgets
import json # library to handle JSON files
from geopy.geocoders import Nominatim 
# convert an address into latitude and longitude values
import requests # library to handle requests
import folium # map rendering library
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
import matplotlib.pyplot as plt
import requests
from typing import Any
from urllib.request import urlopen
import streamlit as st
import numpy as np
import streamlit as st
st.set_page_config(
        page_title="TCA Data Lab",
        page_icon=":running:",

    )
progress_bar = st.sidebar.progress(0)
# We clear elements by calling empty on them.
progress_bar.empty()

st.write("# TCA Mapping Demo")

st.write("Currently, one data layer is present in the project, which represents the preliminary number (as of 25.03.2022) of internally displaced persons in Ukraine")
url="https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/IDP/IDP_data.csv"
s=requests.get(url).content
data_all=pd.read_csv(io.StringIO(s.decode('utf-8')))

with urlopen(r'https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/IDP/stanford-gg870xt4706-geojson.json') as f:
    data_geo = json.load(f)

#with urlopen('https://raw.githubusercontent.com/org-scn-design-studio-community/sdkcommunitymaps/master/geojson/Europe/Ukraine-regions.json') as response:
#    data_geo = json.load(response)

#data_geo = json.load(open('Kecamatan_Surabaya.geojson'))
#data_all["IDPs"] = pd.to_numeric(data_all['IDPs'], errors='coerce')
#data_all["IDPs"]  = data_all["IDPs"] .astype(int)

data_all["IDPs"] = data_all["IDPs"].apply(pd.to_numeric)


#data_all['IDPs'] = data_all['IDPs'].astype('Int64')


def center():
    address = 'Ukraine'
    geolocator = Nominatim(user_agent="id_explorer")
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    return latitude, longitude

def threshold(data):

    threshold_scale = np.linspace(data_all[dicts[data]].min(),
                            data_all[dicts[data]].max(),
                            5, dtype=float)
    threshold_scale = threshold_scale.tolist() # change the numpy array to a list
    threshold_scale[-1] = threshold_scale[-1]
    return threshold_scale


def show_maps(data, threshold_scale):
    maps= folium.Choropleth(
        geo_data = data_geo,
        data = data_all,
        columns=['Region', dicts[data]],
        key_on='feature.properties.name_1',
        #threshold_scale=threshold_scale,
        fill_color='YlGnBu', 
        fill_opacity=0.7, 
        line_opacity=0.2,
        legend_name=dicts[data],
        highlight=True,
        smooth_factor=0,
        overlay=True,
        nan_fill_color='black', nan_fill_opacity=None, 
        bins = [0, 20000, 50000, 100000, 200000, 300000],
        reset=True).add_to(map_sby)


    folium.LayerControl().add_to(map_sby)
    maps.geojson.add_child(folium.features.GeoJsonTooltip(fields=['name_1',data],
                                                        aliases=['name_1: ', dicts[data]],
                                                        labels=True))                                                       
    folium_static(map_sby)

centers = center()


select_maps = st.sidebar.selectbox(
    "What data do you want to see?",
    ("cartodbpositron","OpenStreetMap", "Stamen Toner")
)
select_data = st.sidebar.radio(
    "What data do you want to see?",
    ("Total_IDPs", "LastUpdated")
)

map_sby = folium.Map(tiles=select_maps,  location=[centers[0], centers[1]], zoom_start=5)

data_all['Region'] = data_all['Region'].str.title()
#data_all = data_all.replace({'Region':'Pabean Cantikan'},'Pabean Cantian')
#data_all = data_all.replace({'Region':'Karangpilang'},'Karang Pilang')

dicts = {"Total_IDPs":'IDPs',
"LastUpdated": 'LastUpdated',  
        }

for idx in range(27):
    data_geo['features'][idx]['properties']['Total_IDPs'] = int(data_all['IDPs'][idx])
    data_geo['features'][idx]['properties']['LastUpdated'] = int(data_all['LastUpdated'][idx])

show_maps(select_data, threshold(select_data))
