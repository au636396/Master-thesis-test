import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import random


# initializing secction with a random number, used for picking a condition
if "condition" not in st.session_state:
    st.session_state["condition"] = random.randint(1,4)
st.write(st.session_state.condition)

# condition number meaning:
# 1 = Left, same   # the noutral one
# 2 = Left, diffrent
# 3 = Right, same
# 4 = Rigth, diffrent   # the standart one 

#defining the placment of the coloums (used for placing buttons) 
col1, col2, col3, col4, col5 = st.columns([3,2,1,2,3])

#top text
"""
## Do you want cookies?
"""
#insert cookies test:
"""
"""



# Show different content based on the user session number.
if st.session_state.condition == 1:
    st.write("hello1")
elif st.session_state.condition == 2:
    st.write("hello2")
elif st.session_state.condition == 3:
    st.write("hello3")
elif st.session_state.condition == 4:
    st.write("hello4")
else:
    st.write("An error has occurred, please reload the page!")

with col2:
    accepter1 = st.button("Accepter alle", type="primary")
    st.write(ac1)
with col4:
    afvis1 = st.button("  Afvis alle  ", type="secondary")
    st.write(re1)


#trying to track the input of the user 
#df = pd.read_csv(path)

#st.write(https://survey.au.dk/LinkCollector?key=VC8ZRNUQUN16)
st.link_button("Go to survey", "https://survey.au.dk/LinkCollector?key=VC8ZRNUQUN16")



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
