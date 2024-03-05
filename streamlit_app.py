import pandas as pd
import streamlit as st
import random
import gspread
import gspread_dataframe as gd
import base64

#------------------------ Saving the data --------------
gc = gspread.service_account(filename='~/.config/gspread/service_account.json')   #cornnects to API

#-------------------------- this should be added after the button press code wiht "4acc" being changes to a value set by the buttons (i think)
#olddata = gc.open("MasterThesisDataLog").worksheet("ark") # spesifies the sheet
#pdolddata = gd.get_as_dataframe(olddata)  #imports it as a pd dataframe 
###making a dataframe wiht appnded old data
#new_row = pd.DataFrame([['4acc']], columns=['button']) !!!! has been moved below the buttons #Adding 4acc (condition 4 accsept button) to the coulum named button
#newdata = pd.concat([pdolddata, new_row])    # adding the new row from above at the end of the data

#gd.set_with_dataframe(olddata, newdata)    #this should ad the new data to the gsheet

#--------------------------------


import streamlit_antd_components as sac

sac.buttons([
    sac.ButtonsItem(label='button'),
    sac.ButtonsItem(label='button1', color='#F1F1F1'),
], label='label', align='center', gap='xl', color='green')


# function that add a bacgournd picture 
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
set_background('generic_website.png')

# initializing secction with a random number, used for picking a condition
if "condition" not in st.session_state:
    st.session_state["condition"] = random.randint(1,4)

# making the cookie banner apir
col1, col2, col3 = st.columns([1,4,1])
with col2: st.image('basic_cookie.png')

#defining the placment of the coloums (used for placing buttons). The st.coloum part defines how big each colum is so 2 is dubble as big as 1
col1, col2, col4, col5 = st.columns([3,2,2,3])

### condition number meaning:
# 1 = Left, same   
# 2 = Left, diffrent
# 3 = Right, same
# 4 = Rigth, diffrent 


# Show different content based on the user session number.
if st.session_state.condition == 1:  # con 1
    with col2:
        if st.button("Accepter alle", type="primary"):
            st.session_state["click"] = "accepter1"
    with col4:
        if st.button("  Afvis alle  ", type="primary"):
            st.session_state["click"] = "afvis1"
elif st.session_state.condition == 2:  # con 2
    with col2:
        if st.button("Accepter alle", type="primary"):
            st.session_state["click"] = "accepter2"
    with col4:
        if st.button("  Afvis alle  ", type="secondary"):
            st.session_state["click"] = "afvis2"
elif st.session_state.condition == 3:  # con 3
    with col4:
        if st.button("Accepter alle", type="primary"):
            st.session_state["click"] = "accepter3"
    with col2:
        if st.button("  Afvis alle  ", type="primary"):
            st.session_state["click"] = "afvis3"
elif st.session_state.condition == 4:  # con 4
    with col4:
        if st.button("Accepter alle", type="primary"):
            st.session_state["click"] = "accepter4"
    with col2:
        if st.button("  Afvis alle  ", type="secondary"):
            st.session_state["click"] = "afvis4"
else:
    st.write("An error has occurred, please reload the page!")
    

if 'click' not in st.session_state:
    st.session_state['click'] = 'button not cliked'
## take the button input and puts it in the new row dataframe
new_row = pd.DataFrame([[st.session_state.click]], columns=['button']) 
st.dataframe(new_row)   #!!! remove this before experiment launch


#show button with link to surevery only after a button has been cliked 
if st.session_state.click != 'button not cliked':
    st.link_button("Go to survey", "https://survey.au.dk/LinkCollector?key=VC8ZRNUQUN16")




