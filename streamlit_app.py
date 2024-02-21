import altair as alt
import numpy as np
import pandas as pd
import streamlit as st



# generation a randum number between 1 and 4 for each user secction
if "rn" not in st.session_state:
    st.session_state["rn"] = random.randint(1,4)

st.write('st.session_state.rn') 


#top text
"""
# Welcome to my eksperiment!

## Do you want cookies?
"""

col1, col2, col3, col4, col5 = st.columns([3,2,1,2,3])

with col2:
    button1 = st.button("Accepter alle", type="primary")
    st.write(button1)

with col4:
    button2 = st.button("  Afvis alle  ", type="secondary")
    st.write(button2)







############################ the old pre-build stuff
num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
