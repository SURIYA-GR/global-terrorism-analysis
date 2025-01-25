import time 
import collections 
 
import pandas as pd 
import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings; warnings.simplefilter('ignore') 
 
from sklearn.preprocessing import scale 
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import precision_score 
from sklearn.metrics import recall_score 
from sklearn.metrics import f1_score 
# Display up to 150 rows and columns 
pd.set_option('display.max_rows', 220) 
pd.set_option('display.max_columns', 150) 
 
# Set the figure size for plots 
mpl.rcParams['figure.figsize'] = (14.6, 9.0) 
 
# Set the Seaborn default style for plots 
sns.set() 
 
# Set the color palette 
sns.set_palette(sns.color_palette("muted")) 
# Load the preprocessed GTD dataset 
gtd_df = pd.read_csv('/content/drive/MyDrive/data/gtdeda.csv', 
low_memory=False, index_col = 0, 
                      na_values=['']) 
# Display a summary of the data frame 
gtd_df.info(verbose = True)
# List of attributes that are categorical 
cat_attrs = ['extended_txt', 'country_txt', 'region_txt', 
'specificity', 'vicinity_txt', 
             'crit1_txt', 'crit2_txt', 'crit3_txt', 'doubtterr_txt', 
'multiple_txt', 
             'success_txt', 'suicide_txt', 'attacktype1_txt', 
'targtype1_txt', 
             'targsubtype1_txt', 'natlty1_txt', 'guncertain1_txt', 
'individual_txt', 
             'claimed_txt', 'weaptype1_txt', 'weapsubtype1_txt', 
'property_txt', 
             'ishostkid_txt', 'INT_LOG_txt', 
'INT_IDEO_txt','INT_MISC_txt', 'INT_ANY_txt'] 
 
for cat in cat_attrs: 
    gtd_df[cat] = gtd_df[cat].astype('category') 
 
# Data time feature added during EDA 
gtd_df['incident_date'] = pd.to_datetime(gtd_df['incident_date']) 
 
# Necessary for single data type 
gtd_df['gname'] = gtd_df['gname'].astype('str') 
 
gtd_df.info(verbose = True) 
gtd_df = gtd_df.drop(['provstate', 'city', 'summary', 'corp1', 
'target1', 
                                  'scite1', 'dbsource'], axis=1) 
 
gtd_df.info(verbose = True)
