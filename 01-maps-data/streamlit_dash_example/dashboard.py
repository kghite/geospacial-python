import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('A Simple Dashboard')
st.write('This dashboard displays a chart for the selected region.')


@st.cache_data
def load_data():
    data_url = 'https://storage.googleapis.com/spatialthoughts-public-data/python-dataviz/osm/'
    csv_file = 'highway_lengths_by_district.csv'

    url = data_url + csv_file
    dataframe = pd.read_csv(url)

    return dataframe


df = load_data()

districts = df.DISTRICT.values
district = st.selectbox('Select a district', districts)
filtered = df[df['DISTRICT'] == district]

color_1, color_2, unit = st.columns(3)

nh_color = color_1.color_picker('Pick NH Color', '#0000FF', key='nh')
sh_color = color_2.color_picker('Pick SH Color', '#FF0000', key='sh')
data_units = unit.radio('Units', options=['Kilometers', 'Miles'], index=0, key='unit')

if data_units is 'Miles':
    filtered = filtered[['NH', 'SH']]*0.621371

fig, ax = plt.subplots(1, 1)

filtered.plot(kind='bar', ax=ax, color=[nh_color, sh_color],
              ylabel=data_units, xlabel='Category')
ax.set_title('Length of Highways')
ax.set_ylim(0, 2500)
ax.set_xticklabels([])
stats = st.pyplot(fig)
