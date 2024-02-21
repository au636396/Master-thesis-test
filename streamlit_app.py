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

#make buttons, this should be con 4, change the col to make them move and change the type to make change colour 
with col2:
    accepter1 = st.button("Accepter alle", type="primary")
    st.write(accepter1)
with col4:
    afvis1 = st.button("  Afvis alle  ", type="secondary")
    st.write(afvis1)


#trying to track the input of the user 
df = pd.read_csv("data.csv")
st.dataframe(df)
#df.append(afvis1)

#st.write(https://survey.au.dk/LinkCollector?key=VC8ZRNUQUN16)
st.link_button("Go to survey", "https://survey.au.dk/LinkCollector?key=VC8ZRNUQUN16")




