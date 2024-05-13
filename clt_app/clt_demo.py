import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Illustrating the Central Limit Theorem using Streamlit')
st.subheader('Based on Chapter 1 of Streamlit for DS by Tyler Richards')
st.write('This app simulates a thousand coin flips using the chance of heads input below, and then samples with replacement from that population and plots the histogram of the means of the samples in order to illustrate the central limit theorem!')

# There are freeform text inputs with st.text_input()
# radio buttons, st.radio()
# numeric inputs with st.number_input()
perc_heads = st.number_input(label='Chance of coins landing on heads', min_value=0.0, max_value=1.0, value=0.5)
graph_title = st.text_input(label='Graph Title')

desc_txt = '''
    Samples are drawn from a binomial distribution with specified parameters,
    $n$ trials and $p$ probability of success where $n \ge 0$ and $p \in [0,1]$
'''

binom_dist = np.random.binomial(1, perc_heads, 1000)
list_of_means = []

# lets sample 100 times with replacement
for i in range(0, 1000):
    # append the mean of the 100 samples
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())
fig, ax = plt.subplots()
ax.hist(list_of_means, range=[0,1], bins=20)
ax.set_title(graph_title)
ax.axvline(np.mean(list_of_means), color='red')

st.pyplot(fig)
st.markdown(desc_txt)