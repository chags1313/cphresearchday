import streamlit as st
from PIL import Image
import pandas as pd
data = pd.read_csv('D:/PHIRE/CPH/pages/allptdata.csv')

st.title('Methods')
topside1, topside2 = st.columns([4,1])
topside1.markdown(
"""
<span style='color:grey'>10</span> adults (M = <span style='color:grey'>62.0</span> years; SD = <span style='color:grey'>7.6</span>) 
with incomplete cervical SCI performed UE tasks from the CUE-T while wering a wrist-worn wearable device (ActiGraph GT9X Link) on their dominant UE.

The wearable device captured acceleration data in the x, y, and z planes at 100 hertz sampling frequency. Assessments were performed in an inpatient rehabilitation facility for individuals with acute injury (n = 5) and community settings for Veterans with chronic injury (n = 5) at baseline and follow-up, approximately four weeks later.

Acceleration features (e.g., mean, min, max) were extracted using a sliding window technique (1-second window, 0.5-second step). 
""", unsafe_allow_html=True)

topside2.video('https://www.youtube.com/watch?v=6VEuGwl6hnc')



acc = [feat for feat in data.columns if feat.startswith('Acc')]
res = [feat for feat in data.columns if feat.startswith('Res')]
with st.expander("Features Used for Model Training"):
    st.multiselect("Features Used for Model Training", 
                options = acc + res, 
                default = acc + res,
                label_visibility='hidden')

#topside2.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRySanzSa_A8VtpgIujOpP6WNUSG2hvLCEmLA&usqp=CAU')
"""
The novelty detection model (local outlier factor) [8] was trained with baseline CUE-T acceleration features for hand and arm movements. 

"""
image = Image.open('D:/PHIRE/CPH/pages/train.png')
with st.expander("Training Procedures"):
    st.image(image)

"""
The model was then applied to post-CUE-T acceleration features of hand and arm movements. A simple linear regression was used to assess the relationship between the mean novel UE movement pattern score in the post-test CUE-T to the overall post-test CUE-T score across participants for the hand and arm.
"""
image2 = Image.open('D:/PHIRE/CPH/pages/test.png')
with st.expander("Application Procedures"):
    st.image(image2, caption = 'xx')

