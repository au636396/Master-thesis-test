import pandas as pd
import streamlit as st
import random
import gspread
import gspread_dataframe as gd
import base64
from st_btn_group import st_btn_group
import time

#--------------------------------- DEFINING THE GENERAL WAY THE PAGE LOOKS---------------------------------------------
#stat with sidebar corlapsed
st.set_page_config(initial_sidebar_state="collapsed")

## setting the page wiht to be smaller (makes the white box smalller), removing the top menu bar and the sideabr button
css='''
<style>
    section.main > div {max-width:38rem}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)

# initializing secction with a random number, used for picking a condition
if "condition" not in st.session_state:
    st.session_state["condition"] = random.randint(1,4)

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
set_background('Background.png')

#----------------------------------------------SET UP TIMER---------------------------------------------------------------
# making the start timer with secction state so that it stayes consistent
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = time.time()

#----------------------------------------- SETUP FOR SAVING DATA  --------------------------------------------------------
gc = gspread.service_account(filename='~/.config/gspread/service_account.json')   #cornnects to API
olddata = gc.open("MasterThesisDataLog").worksheet("ark") # spesifies the sheet
pdolddata = gd.get_as_dataframe(olddata)  #imports it as a pd dataframe 

#------------------------- DEFINING THE WAY THE BUTTONS LOOK AND THE OUTPUT TEXT THEY GIVE --------------------------------
## SAME SIZE
#con1
buttons1 = [
    {"label": "Accepter alle", "value": "accepter1", "style": {"backgroundColor": "lightgreen",  "color": "black", },},
    {"label": "  Afvis alle  ",  "value": "afvis1", "style": {"backgroundColor": "lightgreen",  "color": "black", },},
]
#con 2
buttons2 = [
    {"label": "Accepter alle", "value": "accepter2", "style": {"backgroundColor": "lightgreen", "color": "black", },},
    {"label": "  Afvis alle  ",  "value": "afvis2", "style": { "color": "black", },},
]
#con 3
buttons3 = [
    {"label": "  Afvis alle  ",  "value": "afvis3", "style": { "backgroundColor": "lightgreen", "color": "black", },},
    {"label": "Accepter alle", "value": "accepter3", "style": {"backgroundColor": "lightgreen", "color": "black", },},
]
#con 4
buttons4 = [
    {"label": "  Afvis alle  ",  "value": "afvis4", "style": { "color": "black", },},
    {"label": "Accepter alle", "value": "accepter4", "style": {"backgroundColor": "lightgreen", "color": "black", },},
]

#making the container baggruound white
css_body_container = f'''
<style>
    [data-testid="stVerticalBlock"] {{
    background-color: #FFFFFF;
    }}
</style>
'''
st.markdown(css_body_container,unsafe_allow_html=True)

#-----------------------------------------  MAKING THE TEXT AND BUTTONS APPEAR  ---------------------------------------------
#text to apir in banner
text1 = "Vi og vores samarbejdspartnere bruger teknologier, herunder cookies, til at indsamle oplysninger om dig til forskellige formål, herunder:"
text2 = "Ved at trykke på 'Accepter alle' giver du samtykke til alle disse formål. Du kan også vælge at tilkendegive, hvilke formål du vil give samtykke til ved at klike <u>her</u> . Du kan til enhver tid trække dit samtykke tilbage."

# defining the colums the buttons and text will appear in
col1, col2, col3 = st.columns([1,12,1])

#text
with col2: 
    st.write("### "+"Denne hjemmeside bruger cookies.")
    st.write(text1)
    st.write("- Funktionalitet")
    st.write("- Statistik")
    st.write("- Marketing")
    st.write(text2, unsafe_allow_html=True)
    st.write("---")

# makeing the buttons show up depending on condition
if st.session_state.condition == 1:  # con 1
    with col2:
            button_cliked = st_btn_group(buttons=buttons1, gap_between_buttons = 45, size='default', align ='center')
elif st.session_state.condition == 2:  # con 2
    with col2:
            button_cliked = st_btn_group(buttons=buttons2, gap_between_buttons = 45, size='default', align ='center')
elif st.session_state.condition == 3:  # con 3
    with col2:
            button_cliked = st_btn_group(buttons=buttons3, gap_between_buttons = 45, size='default', align ='center')
elif st.session_state.condition == 4:  # con 4
    with col2:
            button_cliked = st_btn_group(buttons=buttons4, gap_between_buttons = 45, size='default', align ='center')
else:
    st.write("An error has occurred, please reload the page!")

with col2: 
    st.markdown('##')
#------------------------------------------------------ TIMER END -------------------------------------------------------------------
if button_cliked == 'afvis1' or button_cliked == 'accepter1' or button_cliked == 'afvis2' or button_cliked == 'accepter2' or button_cliked == 'afvis3' or button_cliked == 'accepter3' or button_cliked == 'afvis4' or button_cliked == 'accepter4':
    end_time = time.time()
    elapsed_time = end_time - st.session_state.start_time 
#---------------------------------------------- TRACKING THE BUTTON INPUT -----------------------------------------------------------
## take the button input and puts it in the new row dataframe, only after a buttons has been pressed
if button_cliked == 'afvis1' or button_cliked == 'accepter1' or button_cliked == 'afvis2' or button_cliked == 'accepter2' or button_cliked == 'afvis3' or button_cliked == 'accepter3' or button_cliked == 'afvis4' or button_cliked == 'accepter4':
    new_row = pd.DataFrame([button_cliked], columns = ['button'])   #making the new dataframe
    new_row['timer'] = elapsed_time   #adding time to the new dataframe
    newdata = pd.concat([pdolddata, new_row]) # adding the new row from above at the end of the data
    gd.set_with_dataframe(olddata, newdata)  #this should ad the new data to the gsheet

#-------------------------------------------------- SWITH TO NEW PAGE-----------------------------------------------------------------
#Goes to survey page once its has been cliked 
if button_cliked == 'afvis1' or button_cliked == 'accepter1' or button_cliked == 'afvis2' or button_cliked == 'accepter2' or button_cliked == 'afvis3' or button_cliked == 'accepter3' or button_cliked == 'afvis4' or button_cliked == 'accepter4':
    st.switch_page("pages/To_survey.py")
