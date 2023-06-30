# Example script for plotting some data using the custom styling code
# This does some standard barcharts of a number of conditions

import sys
import os
import re

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm

import seaborn as sns
sns.set_style("whitegrid")

from my_rc import *

##########################################
# Constants

# Source data folder
# NOTE: Assumes we're running from the folder this script lives in
BASEPATH = "../graph_data/"

# Output data folder
# NOTE: Assumes we're running from the folder this script lives in
OUTPATH  = "../example_plot_outputs/"

##########################################
# Data Processing

# Load dataset
def load_dataset():
	df = pd.read_csv(os.path.join(BASEPATH, "measure_1_raw.csv"), sep='\t').
	return df

##########################################
# Data Plotting
#
# < df: Pandas Dataframe
#
# < title: (str) Title for the graph
# < x_label: (str) X-Axis Label
# < y_label: (str) Y-Axis Label
#
# NOTE: Latex code (e.g. `$\Delta t$`) can be used in these labels for nicer formatting
# NOTE: The below code is just an example...
def plot_dataset_as_bargraph(df,
                             title: str = r"Dependent Measure ($\Delta t$) per Treatment Type",
                             x_label: str = r"Treatment Type",
                             y_label: str = r"Dependent Measure (px)",
                             fileN: str = "measure_1_plot.png"):
	# Compute average values + plot with error bars
	# NOTE: Custom color override is manually applied to these bars
	#       (Leaving these off should use the default Excel-style colours (?)
	v1_df = df.groupby("variable_1")[['measure_1']]
	ax = v1_df.mean().sort_values(by='measure_1').plot(kind="bar", yerr=v1_df.sem(), color="#A9D08E", legend=False)
	
	ax.set_title(title)
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)
	
	ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")
	stylize_grid(ax)
	
	plt.savefig(os.path.join(OUTPATH, fileN), bbox_inches='tight')


##########################################

# Ensure output directories exist
if not os.path.exists(OUTPATH):
	os.makedirs(OUTPATH)

# ----------------------------------------

df = load_dataset()

# ... do some processing

plot_dataset_as_bargraph(df)
