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
# Dataset name / identifier: doi
# Dataset 1 carries the full instructions and the rest follow the same pattern.
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


# -----------------------------------------------------------------------------
# 1.0 PRINT THE DATASET BANNER
# -----------------------------------------------------------------------------
text=("Norrbottens county lithic dataset - https://doi.org/10.7910/DVN/OCYM7I")
def banner(text, ch="=", length=70):
    print(ch * length)
    print(text.center(length))
    print(ch * length)
banner(text)


# -----------------------------------------------------------------------------
# 1.1 READ THE DATASET (Task 1)
# Read your analysis-ready CSV.
# -----------------------------------------------------------------------------
import pandas as pd
df = pd.read_csv("Norrbottens_county_lithic_dataset_1.csv", sep=";")


#subsetting the Type, Material, Blade length and Blade width from the Dataframe to make visualizations
Tools_Materials = df[["Type", "Material", "Blade_length_(mm)", "Blade_width_(mm)"]].copy()

# Convert str values to float 
Tools_Materials["Blade_length_(mm)"] = pd.to_numeric(Tools_Materials["Blade_length_(mm)"],errors = 'coerce')
Tools_Materials["Blade_width_(mm)"] = pd.to_numeric(Tools_Materials["Blade_width_(mm)"],errors = 'coerce')

# Remove NaN values from datafram
Tools_Materials_clean = Tools_Materials.dropna()

# Filtering Tool types to only show the Axes, keeping into account the capital letter
Filtered_TM = Tools_Materials_clean[Tools_Materials_clean["Type"].str.contains("axe", case=False)]

#Filtering the Material colum to only show the values containing Stone or Slate
Filtered_TM = Filtered_TM[Filtered_TM['Material'].isin(["Slate", "Stone"])]

#Filtering the dataframe to only show the weights and the types and materials
Chissels_df = df[["Type", "Material", "Weight_(g)"]].copy()

#Convert str to float in the Weights colum
Chissels_df["Weight_(g)"] = pd.to_numeric(Chissels_df["Weight_(g)"], errors="coerce")

#Filtering to only show the chissels with the material and weight
Filtered_Chissles = Chissels_df[Chissels_df["Type"].str.contains("chisel", case=False)]

#Filtering the length and blade length of the stone and slate axes
Axes= df[["Type", "Material", "Length_(mm)", "Blade_length_(mm)"]].copy()
Axes["Length_(mm)"] = pd.to_numeric(Axes["Length_(mm)"], errors="coerce")
Axes["Blade_length_(mm)"] = pd.to_numeric(Axes["Blade_length_(mm)"], errors="coerce")
Axes_clean = Axes.dropna()


Axe_filtered = Axes_clean[Axes_clean["Type"].str.contains("axe", case=False)]
Axe_filtered = Axe_filtered[Axe_filtered["Material"].isin(["Slate", "Stone"])]
# -----------------------------------------------------------------------------
# 1.2 VISUALISATIONS (Task 2)
# Four visualisations for this dataset. Fonts, points and axis labels must be
# readable, and figures must not draw on top of one another.
# Each figure's title carries its number. Each caption is PRINTED to the
# console under its own label, around 40 words, describing what is shown rather
# than what it means.
# -----------------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
# --- FIGURE 1.1 ---
# Print caption:
print ("Figure1.1: In this figure, the blade length and width of stone axes vs the blade length and width of slate axes are visualized. This is to visualize possible differences between these different material axes")
# Code:
plt.figure(1)
sns.scatterplot(
    data=Filtered_TM, 
    x='Blade_length_(mm)', 
    y="Blade_width_(mm)", 
    hue="Material"
    )

plt.title("Figure 1: Blade Dimensions: Slate vs Stone")
plt.xlabel("Blade length in mm")
plt.ylabel("Blade width in mm")
plt.show()

# --- FIGURE 1.2 ---
# Print caption:
print("Figure 1.2: This figure shows an overview of the total of finds found per Parish")
# Code:
plt.figure(2)
sns.histplot(
    data= df, 
    x= "Parish"
    )

plt.title("Figure 2: Total finds per Parish")
plt.xticks(rotation=90, ha="center")
plt.xlabel("Parish")
plt.ylabel("Finds")
plt.show()


# --- FIGURE 1.3 ---
# Print caption:
print("Figure 1.3: This figure shows the weight distribution in grams per chisel type found. this visualization is filtered by material to show the difference per material aswell")
# Code:
plt.figure(figsize=(10, 5))
sns.scatterplot(
    data=Filtered_Chissles, 
    x="Weight_(g)", 
    y="Type", 
    hue="Material"
    )

plt.title("Figure 3: Weight distribution of chisel type per material")
plt.legend(title="Material", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xlabel("Weight(g)")
plt.ylabel("Chisel Type")
plt.show()
# --- FIGURE 1.4 ---
# Print caption:
print("Figure 1.4: This figure shows the difference between blade length and length of slate and stone axes. Between these is a line drawn to show if there is a relationship between these values. ")
# Code:
sns.lmplot(
    data=Axe_filtered, 
    x="Length_(mm)", 
    y="Blade_length_(mm)", 
    hue="Material", 
    )

plt.title("Figure 1.4: Difference between the blade length and length of slate and stone axes")
plt.xlabel("Length (mm)")
plt.ylabel("Blade length (mm)")
plt.show()
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
# Dataset name / identifier:
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================

# -----------------------------------------------------------------------------
# 4.0 PRINT THE DATASET BANNER
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# 4.1 READ THE DATASET (Task 1)
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# 4.2 VISUALISATIONS (Task 2)
# -----------------------------------------------------------------------------

# --- FIGURE 4.1 ---
# Print caption:

# Code:


# --- FIGURE 4.2 ---
# Print caption:

# Code:


# --- FIGURE 4.3 ---
# Print caption:

# Code:


# --- FIGURE 4.4 ---
# Print caption:

# Code:


# -----------------------------------------------------------------------------
# 4.3 DESCRIPTIVE STATISTICS (Task 3)
# -----------------------------------------------------------------------------

# --- TABLE 4 ---
# Print caption:

# Code:



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
