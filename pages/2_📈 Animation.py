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

st.write("# TCA Animation Demo")


df = px.data.gapminder()
fig=px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
       size="pop", color="continent", hover_name="country",
       log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
st.plotly_chart(fig)

progress_bar = st.sidebar.progress(0)
# We clear elements by calling empty on them.
progress_bar.empty()
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
