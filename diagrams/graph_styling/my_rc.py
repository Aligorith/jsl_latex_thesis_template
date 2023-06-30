# Apply our own custom formatting style to all plot styling settings
# To be imported AFTER seaborn, so that we have the last word

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc

plt.style.use('./excel_thesis_style.mplstyle')

def stylize_axes(ax):
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)

	ax.xaxis.set_tick_params(top='off', direction='out', width=1)
	ax.yaxis.set_tick_params(right='off', direction='out', width=1)
	

def stylize_grid(ax, values_only=True):
	if values_only:
		ax.grid(False)
		ax.yaxis.grid(True)
	else:
		ax.grid(True)
		#ax.xaxis.grid(True)
		#ax.yaxis.grid(True)
