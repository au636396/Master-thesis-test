import pandas as pd
import streamlit as st
import random
import gspread
import gspread_dataframe as gd

#------------------------ Saving the data --------------
gc = gspread.service_account(filename='~/.config/gspread/service_account.json')   #cornnects to API

#-------------------------- this should be added after the button press code wiht "4acc" being changes to a value set by the buttons (i think)
#olddata = gc.open("MasterThesisDataLog").worksheet("ark") # spesifies the sheet
#pdolddata = gd.get_as_dataframe(olddata)  #imports it as a pd dataframe 
###making a dataframe wiht appnded old data
#new_row = pd.DataFrame([['4acc']], columns=['button']) #Adding 4acc (condition 4 accsept button) to the coulum named button
#newdata = pd.concat([pdolddata, new_row])    # adding the new row from above at the end of the data

#gd.set_with_dataframe(olddata, newdata)    #this should ad the new data to the gsheet

#--------------------------------



# initializing secction with a random number, used for picking a condition
if "condition" not in st.session_state:
    st.session_state["condition"] = random.randint(1,4)
st.write(st.session_state.condition)



 

#top text
"""
## Do you want cookies?
"""
#insert cookies test:
"""
"""
st.image('basic_cookie.png')



#defining the placment of the coloums (used for placing buttons) 
col1, col2, col3, col4, col5 = st.columns([3,2,1,2,3])
#make buttons, this should be con 4, change the col to make them move and change the type to make change colour 
with col2:
    accepter1 = st.button("Accepter alle", type="primary")
    st.write(accepter1)
with col4:
    afvis1 = st.button("  Afvis alle  ", type="secondary")
    st.write(afvis1)



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

#show button with link to surevery
st.link_button("Go to survey", "https://survey.au.dk/LinkCollector?key=VC8ZRNUQUN16")




