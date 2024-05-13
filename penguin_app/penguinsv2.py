import streamlit as st
import pandas as pd
import altair as alt
import time

st.title("Palmer's Penguins")
st.markdown("Let's use this Streamlit app to explore data from penguins")

# Import the data
# The following code uses the st.file_uploader() function from within an if statement
# to provide a default file to use until the user interacts with the application
penguin_file = st.file_uploader('Select your local Penguins CSV file (default provided)', type=['csv'])

@st.cache_data() # Cache decorator to store the results of this function
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv('penguins.csv')   
    return df
# st.stop()
df = load_file(penguin_file)

selected_x_var = st.selectbox('What do you want the x variable to be?', df.select_dtypes(include=['int64', 'float64']).columns)
selected_y_var = st.selectbox('What do you want the y variable to be?', df.select_dtypes(include=['int64', 'float64']).columns)
selected_gender = st.selectbox('What gender do you wanto to filter for?',['all penguins', 'male penguins', 'female penguins'])

if selected_gender == 'male penguins':
    df = df[df['sex'] == 'male']
elif selected_gender == 'female penguins':
    df = df[df['sex'] == 'female']
else:
    pass

st.write(df.sample(5))

alt_chart = (alt.Chart(df, title=f"Scatterplot of Palmer's {selected_gender}")
             .mark_circle()
             .encode(
                 x=selected_x_var,
                 y=selected_y_var,
                 color='species'
             ).interactive())
st.altair_chart(alt_chart, use_container_width=True)