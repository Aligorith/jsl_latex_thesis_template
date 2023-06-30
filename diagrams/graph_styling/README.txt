graph_styling/
==============

Python module (and supporting datafile) for use from Python scripts used to
generate graphs / charts using Matplotlib. 

They are intended to be used on top of the "seaborn" package (using the "whitegrid" style),
white sets up most of the basic styling.


## Files

Part of the style-files:
* **`my_rc.py`** - The file that should be imported into the current plotting-script.
                   It applies the stylesheet + provides functions for applying common styling tweaks

* **`excel_thesis_style.mplstyle`** - The styling file that `my_rc.py` imports


Example Files:
* **`example_plots.py`** - Generate some sample plots using these templates


## Dependencies / Requirements

Mandatory:
* Matplotlib
* Seaborn

Recommended:
* NumPy
* Pandas
