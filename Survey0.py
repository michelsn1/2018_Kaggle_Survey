#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 21:43:35 2018

@author: michel
"""

import pandas as pd
from plotly import tools
import plotly.graph_objs as go
import plotly.offline as py

py.init_notebook_mode(connected=True)


data_set_guia=pd.read_csv('SurveySchema.csv')
data_set_free=pd.read_csv('freeFormResponses.csv')
data_set_alt=pd.read_csv('multipleChoiceResponses.csv')


data_set_alt_2017=pd.read_csv('~///Kaggle//2018_Survey//2017//multipleChoiceResponses.csv',encoding='ISO-8859-1')

