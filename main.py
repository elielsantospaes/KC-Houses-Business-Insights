import pandas as pd
import os
from pandas._config.config import set_option
import numpy as np
import plotly.express as px
import streamlit as st
from datetime import datetime
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import statsmodels
from math import sin, cos, sqrt, atan2, radians
st.set_page_config(layout = 'wide')


@st.cache(allow_output_mutation= True)
def get_data(path):
    data = pd.read_csv(path)
    return data


@st.cache(allow_output_mutation= True)
def select_data():
    samples = os.listdir('dataset')
    for sample in samples:
        if '.csv' not in sample or 'kc' in sample:
            samples.pop(samples.index(sample))
        
    return samples
    
@st.cache(allow_output_mutation= True)
def min_max(data, feature):
    min_ = data[feature].min()
    max_ = data[feature].max()
    return [min_, max_]


@st.cache(allow_output_mutation= True)
def show_map(data, estimate_profit):
    data['condition'] = data['condition'].astype(str)
    df = data.loc[data['estimate_profit%'] >  estimate_profit].reset_index()

    fig = px.scatter_mapbox(
                        df,
                        lat = 'lat',
                        lon = 'long',
                        color = 'condition',
                        size = 'estimate_profit%',
                        size_max = 30,
                        hover_name = 'estimate_profit%',
                        zoom = 10
                    )

    fig.update_layout(mapbox_style = 'open-street-map')
    fig.update_layout(width = 700, height = 500, margin={'r':0,'t':0,'l':0,'b':0})
    return fig    


if __name__ == '__main__':
    st.title('House Rocket Dashboard')
    st.write('Welcome to house rocket dashboard. Here you can select the sample of houses of your interest, according to the samples definition available in the report.')
    
    c1, c2 = st.beta_columns((1,3))
    with c1:
        sample = st.selectbox('Select the sample data', select_data())
        path = 'dataset/' + sample
        estimate_profit = st.slider('Select the desired profit',min_max(get_data(path), 'estimate_profit%')[0], min_max(get_data(path), 'estimate_profit%')[1])
    with c2:
        st.write(show_map(get_data(path), estimate_profit))
    
    