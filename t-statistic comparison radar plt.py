# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 18:16:53 2021

@author: sanakhan
"""

import plotly.graph_objects as go
import plotly.offline as pyo


categories = ['Ac', 'slope', 'confinement', 'RUSLE']
categories = [*categories, categories[0]]

w = [24.947, 13.541, -1.206, 1.214]
d = [9.767, 31.693, 0.91, 0.554]

w = [*w, w[0]]
d = [*d, d[0]]


fig = go.Figure(
    data=[
        go.Scatterpolar(r=w, theta=categories, fill='toself', name='w'),
        go.Scatterpolar(r=d, theta=categories, fill='toself', name='d'),
    ],
    layout=go.Layout(
        title=go.layout.Title(text='t-statistic comparison'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

pyo.plot(fig)