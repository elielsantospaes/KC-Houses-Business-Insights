import pandas as pd
import os
import numpy as np
import plotly
import plotly.express as px
import streamlit as st
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
    min_ = float(data[feature].min())
    max_ = float(data[feature].max())
    avg = data[feature].mean()
    return [min_, max_, avg]


@st.cache(allow_output_mutation= True)
def show_map(data, estimate_profit, top, bedrooms, bathrooms, Living_room_area):
    data['condition'] = data['condition'].astype(str)
    df = data.loc[
        (data['estimate_profit%'] >=  estimate_profit) &
        (data['bedrooms'] >= bedrooms) &      
        (data['bathrooms'] >= bathrooms) &
        (data['sqft_living'] >= Living_room_area)
        ].head(top)
    df.sort_values('estimate_profit%', inplace = True, ascending = False)
    fig = px.scatter_mapbox(
                        df,
                        lat = 'lat',
                        lon = 'long',
                        color = 'condition',
                        size = 'estimate_profit%',
                        size_max = 30,
                        zoom = 9
                    )

    fig.update_layout(mapbox_style = 'open-street-map')
    fig.update_layout(width = 1000, height = 700, margin={'r':0,'t':0,'l':0,'b':0})
    return fig    


if __name__ == '__main__':
    st.title('House Rocket Dashboard')
    st.write('Welcome to "house rocket" dashboard. Here you can select the sample of houses of your interest, according to the samples definition available in the report. See after the map the description of the filters.')
    
    c1, c2 = st.beta_columns((1,4))
    with c1:
        st.subheader('Sample of houses.')
        sample = st.selectbox('Select the sample data', select_data())
        path = 'dataset/' + sample
        data = get_data(path)
                
        estimate_profit = st.slider(
            'Select the desired profit (%)',
            min_max(data, 'estimate_profit%')[0],
            min_max(data, 'estimate_profit%')[1],
            min_max(data, 'estimate_profit%')[0],            
        )

        top = st.slider(
            'Select the top houses',
            10,
            int(data['id'].count()),
            int(data['id'].count()/2),
            10            
        )

        st.subheader('Houses featutes.')

        bedrooms = st.slider(
            'Number of bedrooms',
            min_max(data, 'bedrooms')[0],
            min_max(data, 'bedrooms')[1],
            min_max(data, 'bedrooms')[2],            
        )

        bathrooms = st.slider(
            'Number of bathrooms',
            min_max(data, 'bathrooms')[0],
            min_max(data, 'bathrooms')[1],
            min_max(data, 'bathrooms')[2],            
        )

        Living_room_area = st.slider(
            'Living room area (Sqft)',
            min_max(data, 'sqft_living')[0],
            min_max(data, 'sqft_living')[1],
            min_max(data, 'sqft_living')[2],            
        )
    
    with c2:
        st.write(show_map(data, estimate_profit, top, bedrooms, bathrooms, Living_room_area))
    
    st.subheader('See here how the filters works.')
    st.subheader('Sample selector:')
    st.write('In the sample selector you can select a sample of houses from the analysis made in the approaches presented in the repport. sample_general.csv select houses from the general approach, sample_h1 select houses from the hypothesis H1, and so on.')
    
    st.subheader('The top houses')
    st.write('The top houses filter allows to filter data to show only the top X profitable houses. If X = 10 the the map will show the top 10 profitable houses. The step of that filter is ten.')

    st.subheader('Number of bedrooms')
    st.write('Allows to filter data to show only houses with amount of bedrooms equal or higher the selected value.')

    st.subheader('Number of bathrooms')
    st.write('Allows to filter data to show only houses with amount of bathrooms equal or higher the selected value.')

    st.subheader('Living room arear')
    st.write('Allows to filter data to show only houses with living room area equal or higher the selected value.')
    st.write('')
    st.write('PS: The size of the circles represents the estimate profit, considering the evaluation method presented in the repport. The higher size, the higher estimated profit.')