# =============================================================================
#           Quantitative Methods in Archaeology
#                   ASSIGNMENT - CODE
#                   
# =============================================================================
#
# Marks for this section (see the Prospectus for the full breakdown):
#   Task 1 - Read the analysis-ready CSV datasets ................  5 points
#   Task 2 - Four visualisations per dataset ..................... 10 points
#   Task 3 - Descriptive statistics per dataset .................. 10 points
#   Reproducibility, Layout and Code Coherence ................... 10 points
#
# All four are assessed on the script as a whole, not block by block.
# You receive a single group grade.
#
# =============================================================================
### BEFORE YOU START ###
# =============================================================================
#
# ONE SCRIPT, FOUR DATASETS.
#   Each group member writes the block for the dataset they sourced in
#   Section A. Do not record who wrote which block. The group is jointly
#   answerable for the whole file, and every member should be able to
#   explain any part of it, including the parts they did not write.
#
# WHAT GOES HERE, AND WHAT GOES IN THE WORD DOCUMENT.
#   This script holds the code and short captions only. A caption states
#   what a figure or table shows - the variables, the units, the number of
#   cases. It does not argue anything.
#   The interpretation - what the pattern means, whether the statistics
#   support or complicate the visualisations, what alternative explanations
#   exist - belongs in Section C of the Word document. Do not write it twice.
#
# REPRODUCIBILITY.
#   The script must run top to bottom in one pass on a machine that is not
#   yours. Restart your environment and run the whole file before submitting.
#   The only inputs the script may assume are the cleaned
#   CSVs you upload alongside it. It should throw no error messages after
#   <Run>; warnings are acceptable.
#
# NO AI.
#   Do not use any kind of AI while coding here. 
#   
# =============================================================================
### CONSOLE OUTPUT: READ THIS BEFORE YOU WRITE ANY print() ###
# =============================================================================
#
# Captions are not comments. Every caption in this script must be PRINTED to
# the console when the file runs. 
#
# The layout of what you print is assessed under Reproducibility, Layout and
# Code Coherence. 
#
# REQUIRED FORMAT.
#   Print a banner at the start of each dataset block:
#
#       ============================================================
#       DATASET 1 - <dataset name; DOI if applicable>
#       ============================================================
#
#   Print each caption under a label of its own, immediately before the
#   object it describes:
#
#       FIGURE 1.1
#       <caption, around 40 words>
#
#       TABLE 1
#       <caption, around 40 words>
#       <the statistics themselves>
#
#
# PRINT NOTHING YOU WILL NOT USE.
#   Do not dump a whole dataframe, and do not print statistics that appear
#   nowhere in Section C. Every printed number should be one you discuss.
#
# =============================================================================
#           Quantitative Methods in Archaeology
#                   ASSIGNMENT - CODE
#                   
# =============================================================================


### OFF WE GO!!! 

# =============================================================================
# Group Name:
# Group Members:
#   1 -
#   2 -
#   3 -
#   4 -
# =============================================================================



# =============================================================================
# IMPORT PACKAGES
# All imports go here, once. No repeated or unused imports anywhere below.
# Focus on the packages we have covered in the lab. Use other packages ...
# ... only when it is absolutely necessary. You will need to justify the use. 
# =============================================================================


# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# DATASET 1
# Dataset name / identifier:
# Dataset 1 carries the full instructions and the rest follow the same pattern.
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


# -----------------------------------------------------------------------------
# 1.0 PRINT THE DATASET BANNER
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# 1.1 READ THE DATASET (Task 1)
# Read your analysis-ready CSV.
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# 1.2 VISUALISATIONS (Task 2)
# Four visualisations for this dataset. Fonts, points and axis labels must be
# readable, and figures must not draw on top of one another.
# Each figure's title carries its number. Each caption is PRINTED to the
# console under its own label, around 40 words, describing what is shown rather
# than what it means.
# -----------------------------------------------------------------------------

# --- FIGURE 1.1 ---
# Print caption:

# Code:


# --- FIGURE 1.2 ---
# Print caption:

# Code:


# --- FIGURE 1.3 ---
# Print caption:

# Code:


# --- FIGURE 1.4 ---
# Print caption:

# Code:


# -----------------------------------------------------------------------------
# 1.3 DESCRIPTIVE STATISTICS (Task 3)
# Print the caption first, then the statistics, in a clean readable layout.
# -----------------------------------------------------------------------------

# --- TABLE 1 ---
# Print caption:

# Code:


# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# DATASET 2
# Dataset name / identifier:
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


# -----------------------------------------------------------------------------
# 2.0 PRINT THE DATASET BANNER
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# 2.1 READ THE DATASET (Task 1)
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# 2.2 VISUALISATIONS (Task 2)
# -----------------------------------------------------------------------------

# --- FIGURE 2.1 ---
# Print caption:

# Code:


# --- FIGURE 2.2 ---
# Print caption:

# Code:


# --- FIGURE 2.3 ---
# Print caption:

# Code:


# --- FIGURE 2.4 ---
# Print caption:

# Code:


# -----------------------------------------------------------------------------
# 2.3 DESCRIPTIVE STATISTICS (Task 3)
# -----------------------------------------------------------------------------

# --- TABLE 2 ---
# Print caption:

# Code:


# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# DATASET 3
# Dataset name / identifier:
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


# -----------------------------------------------------------------------------
# 3.0 PRINT THE DATASET BANNER
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# 3.1 READ THE DATASET (Task 1)
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# 3.2 VISUALISATIONS (Task 2)
# -----------------------------------------------------------------------------

# --- FIGURE 3.1 ---
# Print caption:

# Code:


# --- FIGURE 3.2 ---
# Print caption:

# Code:


# --- FIGURE 3.3 ---
# Print caption:

# Code:


# --- FIGURE 3.4 ---
# Print caption:

# Code:


# -----------------------------------------------------------------------------
# 3.3 DESCRIPTIVE STATISTICS (Task 3)
# -----------------------------------------------------------------------------

# --- TABLE 3 ---
# Print caption:

# Code:


# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# DATASET 4
# Dataset name / identifier:muntjescompleet88888.csv
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================

# -----------------------------------------------------------------------------
# 4.0 PRINT THE DATASET BANNER
# -----------------------------------------------------------------------------
import pandas as pd
df = pd.read_csv ('muntjescompleet88888.csv')

print (df)


# -----------------------------------------------------------------------------
# 4.1 READ THE DATASET (Task 1)
import pandas as pd
df = pd.read_csv ('muntjescompleet88888.csv')




# -----------------------------------------------------------------------------
# 4.2 VISUALISATIONS (Task 2)
# -----------------------------------------------------------------------------

# --- FIGURE 4.1 ---
print("figure 1: a stacked graph of coins by enddate and material aka subcategorie grouped in 140 bins and specifyied for the timeframe of 1350ad to current day.")

# Code: 
#first import seaborn and mathplotlib
#furter read the csv and define it as df use seaborn to make a graph using the displot fuction make it stack and group by subcategorie aka metal type and define bins and x axis range for the bin groups.

import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv ('muntjescompleet88888.csv')
sns.displot(data=df, x='eind_dat', hue='subcategorie', multiple="stack", bins=140)
plt.xlim(1350,2026)
plt.title("1")
plt.figure (1)
# --- FIGURE 4.2 ---
print("figure 2: same as figure 1 but not subdevided into subcategorie")


# Code:
df = pd.read_csv ('muntjescompleet88888.csv')
sns.displot(data=df, x='eind_dat', bins=140)
plt.xlim(1350,2026)
plt.title("2")
plt.figure (2)


# --- FIGURE 4.3 ---
print("figure 3: counts grouped by subcategorie aka metal type")

# Code:
df = pd.read_csv ('muntjescompleet88888.csv')
sns.histplot(data=df, y="subcategorie",)
plt.title("3")
plt.figure (3)



# --- FIGURE 4.4 ---
# Print caption:
print("figure 4: material composition per site") 
df = pd.read_csv ('muntjescompleet88888.csv')
sns.histplot(data=df, y="subcategorie",)
# Code:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv ('muntjescompleet88888.csv')
sns.displot(data=df, x='project_code', hue='subcategorie', multiple="stack")
plt.title("4")
plt.figure (4)

# -----------------------------------------------------------------------------
# 4.3 DESCRIPTIVE STATISTICS (Task 3)
# -----------------------------------------------------------------------------

# --- TABLE 4 ---
print("descriptive statistics")


# Code:
df = pd.read_csv ('muntjescompleet88888.csv')
df[["eind_dat", "begin_dat", 'munt_lengte_diameter_in_mm','vlak_max']].describe()


# =============================================================================
# COHERENCE CHECK
#
# Do this together, once all four blocks work. Because four people wrote four
# blocks, the script will not be coherent by default. A reader should not be
# able to tell where one author stops and the next begins.
#
#   Console: is every figure and every table preceded by a printed
#       caption, and does every figure number match its plot title?
#   Console: is anything printed that you do not discuss in Section C?
#   Naming: one convention for variables, dataframes and figure objects,
#       applied across all four blocks.
#   Structure: the same sequence of steps in the same order for each
#       dataset, so the blocks are parallel and comparable.
#   Comments: a consistent level throughout. 
#   Imports: all at the top, once. Nothing repeated, nothing unused.
#   Restart the environment and run the whole file, on a machine that is
#       not the one it was written on.
#   Check that every figure and table the script produces is the one you
#       have reported in Section C.
# =============================================================================