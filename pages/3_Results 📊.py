import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(layout="wide")

st.title("Results")
"""
A significant regression equation was found for novel UE hand movement patterns (F(1,9) = 37.61, p < 0.001), with an R2 of 0.84, but not found for novel UE arm movement patterns. CUE-T scores increased by 12.9 points for each 0.1 increase in mean novel UE hand movement score
"""
participantsfeatures = st.sidebar.radio("Novelty Detected Movement", ["Regression", "Participants", "Features"])
allptdata = pd.read_csv("D:/PHIRE/CPH/pages/allptdata.csv")
comb = pd.read_csv("D:/PHIRE/CPH/pages/comb.csv")
if participantsfeatures == 'Regression':
    hs = st.radio("hs", ['Hand', 'Arm'], horizontal = True, label_visibility='hidden')
    if hs == 'Hand':
        v = 'Hand'
    if hs == 'Arm':
        v = 'Side'
    fig = px.scatter(comb[comb['Class']==v], x= 'Novelty Score', y = 'CUET Score', trendline = 'ols', trendline_color_override='black')
    fig.update_layout(showlegend=False, font_size = 28)
    fig.update_traces(marker={'size': 24})
    fig.update_layout(paper_bgcolor=None, plot_bgcolor=None)
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.15,
        xanchor="right",
        x=0.8
    ))
    fig.update_xaxes(title = None)
    fig.update_yaxes(title = None)
    st.plotly_chart(fig, use_container_width=True)
if participantsfeatures == 'Participants':
    pt = st.selectbox("Select Example Participant", options = allptdata['PT'].unique())
    figdata = allptdata[allptdata['cuet']=='Cuet2']
    figdata = figdata[figdata['PT'] == pt]
    figdata['s'] = figdata.index
    figdata["Series"] = figdata.groupby("PT")['s'].apply(lambda x: x.groupby(x).ngroup() + 1)
    figdata['Cue-T'] = figdata['CUET All Score']
    figdata['Novel Movement'] = figdata['Novel Movement'].replace([0,1], ['Baseline Related Movement', 'Novel UE Movement'])
    fig = px.scatter(figdata, x='Series', y = 'Resultant (m/s^2)_mean', 
                color = 'Novel Movement',
                color_discrete_map={'Non-Novel UE Movement': 'red', 'Novel UE Movement': 'lightsteelblue'}, 
                category_orders={'Novel Movement': ['Non-Novel UE Movement', 'Novel UE Movement']}, 
                hover_data = ['class'])
    fig.update_layout(height=450, width=1300, showlegend=True, font_size = 28)
    fig.update_layout(paper_bgcolor=None, plot_bgcolor=None)

    #fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.update_traces(marker={'size': 5})
    fig.update_xaxes(showgrid=False, zeroline=True, title = "Time", showticklabels=False)
    fig.update_yaxes(showgrid=True, zeroline=True, title = 'Acceleration (sqrt(x + y + z) M/S^2)')

    st.plotly_chart(fig, use_container_width=True)
if participantsfeatures == 'Features':
    handarm = st.radio("Hand or Side", options = ["Hand", "Arm"], horizontal = True, label_visibility = 'hidden')
    feats = st.multiselect("Features", options = [feature for feature in allptdata.columns if feature.startswith('Resultant')], 
                           default = ['Resultant (m/s^2)_mean', 
                                 'Resultant (m/s^2)_std', 
                                 'Resultant (m/s^2)_energy'])
    features = [feat.split('_')[1].upper() for feat in feats]
    features = features + ['Score']
    feats = feats + ['Novelty Score']
    d = allptdata[allptdata['cuet'] == 'Cuet2']
    if handarm == "Hand":
        d = allptdata[allptdata['class'] == 'hand']
    if handarm == "Arm":
        d = allptdata[allptdata['class'] == 'side']
    featurefig = px.parallel_coordinates(d[feats], 
                                color="Novelty Score",
                                color_continuous_scale = 'rdbu', 
                                color_continuous_midpoint= 2,
                                range_color = [1, 4])
    featurefig.update_layout(showlegend=False, font_size = 24)
    featurefig.update_layout(paper_bgcolor=None, plot_bgcolor=None)
    st.plotly_chart(featurefig, use_container_width=True)

