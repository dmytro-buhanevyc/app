from sqlite3 import Date
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from ipywidgets import widgets
import json # library to handle JSON files
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

import streamlit as st
from streamlit.logger import get_logger


import streamlit as st
st.set_page_config(
        page_title="TCA Data Lab",
        page_icon=":running:",

    )


st.write("# TCA Data Lab 🧪")
st.markdown(
    """
    TCA Data Lab is a lightweight web app, which provides a repository of research materials created by TCA.

    **👈 Select a project from the menu on the left**

    ### FAQ

    - This TCA Data Lab demo currently hosts two complete projects.
    - The complete projects are News Analysis and Mapping.
        - News Analysis visualizes Twitter data from official news sources in three select countries (France, Germany, Italy).
        - Mapping showcases geospatial data on the number of internally displaced persons in Ukraine.
        - Animation Demo is a placeholder for potential visualizations of TCA's research. 
    - Data (table contents, snapshots of graphs) can be extracted as images. 


    ### Contact
    - Please contact Dmytro Bukhanevych at dbukhanevych@transformua.com for more details
"""
)
