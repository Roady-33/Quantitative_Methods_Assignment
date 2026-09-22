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

#Code:

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
text=("Incrematal Dental Dataset")
def banner(text, ch='=', length=45):
    print(ch * length)
    print (text.center(length))
    print(ch * length)
banner(text)




# -----------------------------------------------------------------------------
# 3.1 READ THE DATASET (Task 1)
# -----------------------------------------------------------------------------

import pandas as pd
df = pd.read_csv(r"C:\Anaconda\Dental dataset\Incremental_DentalClean.csv", 
                 sep=";")


# -----------------------------------------------------------------------------
# 3.2 VISUALISATIONS (Task 2)
# -----------------------------------------------------------------------------

# --- FIGURE 3.1 ---
# Print caption:
print("Figure 1: This bar chart shows the number of tooth samples that are",
      "examined during this research.","These teeth were found in different",
      "countries around the world. Green shows the amount of teeth from",
      "individuals with a low status, and red shows the higher status.")

# Code:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#reading the database
Figure1 = pd.read_csv(r"C:\Anaconda\Dental dataset\Incremental_DentalClean_Data.csv",
                      sep=";")
Figure1.columns = Figure1.columns.str.strip()

#Bar Chart with the countries and the amount of founded teeth
sns.barplot(x='Modern Country',
            y='Nr. of Analysed Tooth Samples', 
            data=Figure1, 
            hue='Social Status',
           palette=["#5BC0BE", "#C9184A"])



#setting the X (Modern Countries) and the Y (Nr. Tooth) labels
plt.title("Tooth Samples from diffrent countries")
plt.xlabel("Modern Country")
plt.ylabel("Nr. analysed tooth samples")

plt.xticks(rotation=45)


# Adding the legends
plt.show()

# --- FIGURE 3.2 ---
# Print caption:

print("Figure 2: This figure shows the difference within the maximum age of different",
      "individuals based on their culture. The blue color shows the max. age",
      "of men, and the pink shows the age of women in those cultures. The ages from",
      "English, Japanese, and Nubian/Meroitic cultures were the highest.")


# Code:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#reading the database
Figure2 = pd.read_csv(r"C:\Anaconda\Dental dataset\Incremental_DentalClean_Data.csv", sep=";")
plt.title("Max years per individuel based on culture")

Figure2.columns = Figure2.columns.str.strip()
sns.scatterplot(x='Culture', 
                y='Max. Age Individual (Years)', 
                data=Figure2,
                hue='Sex',
    palette=["#003F88", "#F72585"])

plt.xticks(rotation=45)

# Adding the legends
plt.show()


# --- FIGURE 3.3 ---
# Print caption:

print("Figure 3: This boxplot shows the difference within the social status",
      "of the individuals based on the age. The purple boxplot shows the age",
      "of low-status individuals. Their age was between 30 and 40 years old.",
      "The individuals with a high status (green) had an age between 30 and 75.")   

# Code:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#reading the database
Figure3 = pd.read_csv(r"C:\Anaconda\Dental dataset\Incremental_DentalClean_Data.csv", sep=";")
Figure3.columns = Figure3.columns.str.strip()

Figure3["Age"]=(
    Figure3["Min. Age Individual (Years)"]+
    Figure3["Max. Age Individual (Years)"])/2

sns.boxplot(
    x="Social Status",
    y="Age",
    data=Figure3,
    hue="Social Status",
    palette=["#7B2CBF", "#3CDBD3"])

plt.xlabel("Social Status")
plt.ylabel("Age")
plt.title("Age of individuals based on social status")

# Adding the legends

plt.show()


# --- FIGURE 3.4 ---
# Print caption:

print("Figure 4: This figure shows the δ13C collagen values spread over different",
      "time periods. This collagen shows the dietary protein people consumed.",
      "Most of the collagen was found around in 1750. The blue color shows",
      "the amount of man consumed, and the pink of women.") 

# Code:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading the database

Figure4 = pd.read_csv(r"C:\Anaconda\Dental dataset\Incremental_DentalClean_Data.csv", sep=";")
Figure4.columns = Figure4.columns.str.strip()

#To show the whole timeline i blended both Min and Mix Dates of the individuals
Figure4["Date"] = (
    Figure4["Min. Date (CE) (95%)"] +
    Figure4["Max. Date (CE) (95%)"])/2


#Code for making the scatterplot with the collagen diveded by Sex during history
sns.scatterplot(
    data=Figure4,
    x="δ13C Collagen",
    y="Date",
    hue="Sex", 
    palette=["#F72585", "#003F88"])

#Giving the labels names
plt.xlabel("δ13C Collagen")
plt.ylabel("Date")
plt.title("δ13C Collagen values during differents times divided by sex")

#Dividing x by fewer numbers to make it readable.
plt.xticks([-22, -20, -18, -16, -14, -12, -10, -8, -6])



plt.show()




# -----------------------------------------------------------------------------
# 3.3 DESCRIPTIVE STATISTICS (Task 3)
# -----------------------------------------------------------------------------

# --- TABLE 3 ---
# Print caption:
print("Table 1: This table present the descriptive statistics of the dataset.",
      "The numeric variables in the Dental incremental dataset include the number",
      "of observations, mean, standard, minimum, median, and maximum. The object variables",
      "are left out of this table.")
    
# Code:

import pandas as pd

#reading the database
Table = pd.read_csv(r"C:\Anaconda\Dental dataset\Incremental_DentalClean_Data.csv", sep=";")

#Printing the Descriptive statistics of the table.

print("Table 1: Descriptive statistics of the numeric values")
Table1 = Table.describe(exclude=[str])
Table1 = Table1.drop(index=['25%', '75%'])
print(Table1)

#Printing the Descriptive statistics of the table.
print("Table 2: This table shows the descriptive statistics of the dataset.",
      "The categorical variables in the Dental Incremental dataset include count",
      "unique, top, and frequency. The object numeric are left out of this table.")

Table2=Table.describe(include=[str])

print(Table2)


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
