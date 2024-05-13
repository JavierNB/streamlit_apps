import streamlit as st
import pandas as pd
import altair as alt

st.title("Palmer's Penguins")
# import the data
df = pd.read_csv('penguins.csv')
st.write(df.sample(6))
st.markdown("Let's use this Streamlit app to explore data from penguins")
selected_species = st.selectbox('What species would you like to visualize?', df.species.unique())
selected_x_var = st.selectbox('What do you want the x variable to be?', df.select_dtypes(include=['int64', 'float64']).columns)
selected_y_var = st.selectbox('What do you want the y variable to be?', df.select_dtypes(include=['int64', 'float64']).columns)

penguins_df = df[df['species'] == selected_species]
alt_chart = (alt.Chart(penguins_df, title=f'Scatterplot of {selected_species} Penguins')
             .mark_circle()
             .encode(
                 x=selected_x_var,
                 y=selected_y_var,
             ).interactive())
st.altair_chart(alt_chart, use_container_width=True)