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
#   1 - Jenna Hart
#   2 - Ersin Cilek
#   3 - Elin Zandstra
#   4 - Koen Vogelzang
# =============================================================================



# =============================================================================
# IMPORT PACKAGES
# All imports go here, once. No repeated or unused imports anywhere below.
# Focus on the packages we have covered in the lab. Use other packages ...
# ... only when it is absolutely necessary. You will need to justify the use. 
# =============================================================================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# DATASET 1
# Dataset name / identifier: DOI:https://doi.org/10.1002/9781118628430.ch3
# Dataset 1 carries the full instructions and the rest follow the same pattern.
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


# -----------------------------------------------------------------------------
# 1.0 PRINT THE DATASET BANNER
# -----------------------------------------------------------------------------
text = "Ruff (2018) Osteological Data from Europe - DOI: https://doi.org/10.1002/9781118628430.ch3"
def banner(text, ch="=", length=70):
    print(ch * length)
    print(text.center(length))
    print(ch * length)
banner(text)
# -----------------------------------------------------------------------------
# 1.1 READ THE DATASET (Task 1)
# Read your analysis-ready CSV.
# -----------------------------------------------------------------------------
osteo = pd.read_csv("Ruff_Data_Clean.csv")
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
print("Figure 1.1: Box plot comparing estimated anatomical stature (cm)",
      " between rural and urban individuals, separated by sex, in the Ruff",
      " et al. (2018) European osteoarchaeological dataset. Boxes represent",
      " interquartile ranges, horizontal lines indicate medians, and whiskers",
      " show stature distributions.")
# Code:

# Defining four groups    
urban_male = osteo[(osteo["RURAL/URBAN"] == 2) & (osteo["SEX"] == 1)]
urban_female = osteo[(osteo["RURAL/URBAN"] == 2) & (osteo["SEX"] == 2)]
rural_male = osteo[(osteo["RURAL/URBAN"] == 1) & (osteo["SEX"] == 1)]
rural_female = osteo[(osteo["RURAL/URBAN"] == 1) & (osteo["SEX"] == 2)]

# Pulling stature from each group
groups = [
    urban_male["STATURE"],
    rural_male["STATURE"],
    urban_female["STATURE"],
    rural_female["STATURE"]
    ]

# Create a boxplot
plt.boxplot(groups)

# Adding scattered individual points w/ jitter
plt.scatter(
    1 + np.random.normal(0, 0.04, len(urban_male)),
    urban_male["STATURE"],
    s=3,
   alpha=0.25
)

plt.scatter(
    2 + np.random.normal(0, 0.04, len(rural_male)),
    rural_male["STATURE"],
    s=3,
    alpha=0.25
)

plt.scatter(
    3 + np.random.normal(0, 0.04, len(urban_female)),
    urban_female["STATURE"],
    s=3,
   alpha=0.25
)

plt.scatter(
    4 + np.random.normal(0, 0.04, len(rural_female)),
    rural_female["STATURE"],
    s=3,
   alpha=0.25
)

# Labelling boxes
plt.xticks(
    [1, 2, 3, 4],
    ["Urban Male", "Rural Male", "Urban Female", "Rural Female"]
)
# Labelling y-axis
plt.ylabel("Stature (cm)")
# Title
plt.title("Figure 1.1: Stature by Urban/Rural Status & Sex")

# Show boxplot
plt.show()












# --- FIGURE 1.2 ---
# Print caption:
print("Figure 1.2: Mean age at death across North and Central European from",
      " the Neolithic through Late Medieval periods in the Ruff et al. (2018)",
      " European osteoarchaeological dataset. Points represent mean age at",
      " death for each chronological period.")
# Code:


# pull only North/Central Europe from data
north_central = osteo[osteo["REGION"] == "N.-Cen. Europe"]

# Calculate mean age of death by time period
mean_age = north_central.groupby("PERIOD")["AGE MEAN"].mean()

#Define Period Order
period_order = [
    "Neolithic",
    "Bronze",
    "Iron/Roman",
    
    "Early Medieval",
    "Late Medieval"
]

# put in chronological order
mean_age = mean_age.reindex(period_order)

# Make plot
sns.barplot(
    x=mean_age.index,
    y=mean_age.values,
    
  )

# Labelling x and y axis
plt.xlabel("Time Period")
plt.ylabel("Mean Age at Death (years)")

# Title
plt.title("Figure 1.2: Mean Age at Death Through Time in North-Central Europe")

# Rotating time period names so they are legible
plt.xticks(rotation=45)

# Show graph
plt.show()


# --- FIGURE 1.3 ---
# Print caption:
print("Box plots showing maximum tibia length across five European regions",
      " in the Ruff et al. (2018) osteoarchaeological dataset, separated by",
      " sex. Boxes represent interquartile ranges, horizontal lines indicate",
      " medians, and whiskers show the distribution of maximum tibia length",
      " within each regional-sex group.")
# code

# Defining regional groups by sex
balkans_male = osteo[(osteo["REGION"] == "Balkans") & (osteo["SEX"] == 1)]
balkans_female = osteo[(osteo["REGION"] == "Balkans") & (osteo["SEX"] == 2)]

britain_male = osteo[(osteo["REGION"] == "Britain") & (osteo["SEX"] == 1)]
britain_female = osteo[(osteo["REGION"] == "Britain") & (osteo["SEX"] == 2)]

iberia_male = osteo[(osteo["REGION"] == "Iberia") & (osteo["SEX"] == 1)]
iberia_female = osteo[(osteo["REGION"] == "Iberia") & (osteo["SEX"] == 2)]

ncenteuro_male = osteo[(osteo["REGION"] == "N.-Cen. Europe") & (osteo["SEX"] == 1)]
ncenteuro_female = osteo[(osteo["REGION"] == "N.-Cen. Europe") & (osteo["SEX"] == 2)]

scandfin_male = osteo[(osteo["REGION"] == "Scand./Finland") & (osteo["SEX"] == 1)]
scandfin_female = osteo[(osteo["REGION"] == "Scand./Finland") & (osteo["SEX"] == 2)]

# Pulling tibia length from each group
regiongroups = [
    balkans_male["TMAXLN"],
    balkans_female["TMAXLN"],
    
    britain_male["TMAXLN"],
    britain_female["TMAXLN"],
    
    iberia_male["TMAXLN"],
    iberia_female["TMAXLN"],
    
    ncenteuro_male["TMAXLN"],
    ncenteuro_female["TMAXLN"],
    
    scandfin_male["TMAXLN"],
    scandfin_female["TMAXLN"]
]

# Create a boxplot
boxplot = plt.boxplot(
    regiongroups,
    patch_artist=True
)

# X-ticks
plt.xticks(
    [1.5, 3.5, 5.5, 7.5, 9.5],
    [
        "Balkans",
        "Britain",
        "Iberia",
        "N.-Cen. Europe",
        "Scand./Finland"
    ]
)
# rotating x-ticks for legibility
plt.xticks(rotation=45)
# Labelling y-axis
plt.ylabel("Max Tibia Length (mm)")
# Title
plt.title("Figure 1.3: Max Tibia Length by Region & Sex")

# Color male boxes blue
for box in boxplot["boxes"][::2]:
    box.set_facecolor("lightblue")

# Color female boxes pink
for box in boxplot["boxes"][1::2]:
    box.set_facecolor("pink")
    
# Legend
plt.plot([], [], color="lightblue", marker="s", label="Male")
plt.plot([], [], color="pink", marker="s", label="Female")

plt.legend(title="Sex", bbox_to_anchor=(1.05, 1), loc="upper left")


# Show boxplot
plt.show()

# --- FIGURE 1.4 ---
# Print caption:
print("Figure 1.4: Histograms showing bilateral asymmetry in humeral",
      " anteroposterior (AP; front-to-back) and mediolateral",
      " (ML; side-to-side) diameters at 50% shaft length among rural and",
      " urban individuals in the Ruff et al. (2018) European",
      " osteoarchaeological dataset. Asymmetry is expressed as absolute",
      " percentage difference between right and left measurements.")
# code

# LEFT HUMERUS
left_ap = osteo["HL50AP"]       # Left humerus AP diameter
left_ml = osteo["HL50ML"]       # Left humerus ML diameter

# RIGHT HUMERUS
right_ap = osteo["HR50AP"]      # Right humerus AP diameter
right_ml = osteo["HR50ML"]      # Right humerus ML diameter

# Calculate directional asymmetry
# Positive = right side larger
# Negative = left side larger
AP_difference = right_ap - left_ap
ML_difference = right_ml - left_ml

# Calculate absolute asymmetry
AP_absolute_asymmetry = np.abs(AP_difference)
ML_absolute_asymmetry = np.abs(ML_difference)

# Calculate percentage asymmetry
AP_percent_asymmetry = (
    AP_absolute_asymmetry /
    ((right_ap + left_ap) / 2)
) * 100

ML_percent_asymmetry = (
    ML_absolute_asymmetry /
    ((right_ml + left_ml) / 2)
) * 100

# Separate Rural and Urban individuals
rural_ap = AP_percent_asymmetry[
    osteo["RURAL/URBAN"] == 1
]

urban_ap = AP_percent_asymmetry[
    osteo["RURAL/URBAN"] == 2
]

rural_ml = ML_percent_asymmetry[
    osteo["RURAL/URBAN"] == 1
]

urban_ml = ML_percent_asymmetry[
    osteo["RURAL/URBAN"] == 2
]

# Plot figure
plt.figure


# AP asymmetry subplot

plt.subplot(1, 2, 1)

plt.hist(
    rural_ap,
    alpha=0.6,
    label="Rural"
)

plt.hist(
    urban_ap,
    alpha=0.6,
    label="Urban"
)

plt.xlabel("AP Percent Asymmetry")
plt.ylabel("Frequency")
plt.title("Humeral AP Asymmetry")
plt.legend()

# ML asymmetry subplot


plt.subplot(1, 2, 2)

plt.hist(
    rural_ml,
    alpha=0.6,
    label="Rural"
)

plt.hist(
    urban_ml,
    alpha=0.6,
    label="Urban"
)

plt.xlabel("ML Percent Asymmetry")
plt.ylabel("Frequency")
plt.title("Humeral ML Asymmetry")
plt.legend()


# Display plot
plt.show()
# -----------------------------------------------------------------------------
# 1.3 DESCRIPTIVE STATISTICS (Task 3)
# Print the caption first, then the statistics, in a clean readable layout.
# -----------------------------------------------------------------------------

# --- TABLE 1 ---
#What is the total number of finds per Parish?
# Print caption:

# code

    # Figure 1.1 - Stature
# Boxplot shows median and quartiles

# Urban Male
urban_male_n = urban_male["STATURE"].count()
urban_male_median = urban_male["STATURE"].median()
urban_male_q1 = urban_male["STATURE"].quantile(0.25)
urban_male_q3 = urban_male["STATURE"].quantile(0.75)

# Rural Male
rural_male_n = rural_male["STATURE"].count()
rural_male_median = rural_male["STATURE"].median()
rural_male_q1 = rural_male["STATURE"].quantile(0.25)
rural_male_q3 = rural_male["STATURE"].quantile(0.75)

# Urban Female
urban_female_n = urban_female["STATURE"].count()
urban_female_median = urban_female["STATURE"].median()
urban_female_q1 = urban_female["STATURE"].quantile(0.25)
urban_female_q3 = urban_female["STATURE"].quantile(0.75)

# Rural Female
rural_female_n = rural_female["STATURE"].count()
rural_female_median = rural_female["STATURE"].median()
rural_female_q1 = rural_female["STATURE"].quantile(0.25)
rural_female_q3 = rural_female["STATURE"].quantile(0.75)


# Figure 1.2 - Age at death
# Line graph shows mean age

# Neolithic
neolithic = north_central[
    north_central["PERIOD"] == "Neolithic"
]["AGE MEAN"]

neolithic_n = neolithic.count()
neolithic_mean = neolithic.mean()

# Bronze
bronze = north_central[
    north_central["PERIOD"] == "Bronze"
]["AGE MEAN"]

bronze_n = bronze.count()
bronze_mean = bronze.mean()

# Iron/Roman
iron_roman = north_central[
    north_central["PERIOD"] == "Iron/Roman"
]["AGE MEAN"]

iron_roman_n = iron_roman.count()
iron_roman_mean = iron_roman.mean()

# Early Medieval
early_medieval = north_central[
    north_central["PERIOD"] == "Early Medieval"
]["AGE MEAN"]

early_medieval_n = early_medieval.count()
early_medieval_mean = early_medieval.mean()

# Late Medieval
late_medieval = north_central[
    north_central["PERIOD"] == "Late Medieval"
]["AGE MEAN"]

late_medieval_n = late_medieval.count()
late_medieval_mean = late_medieval.mean()


# Figure 1.3 - Maximum tibia length
# Boxplot shows median and quartiles

# Balkans Male
balkans_male_n = balkans_male["TMAXLN"].count()
balkans_male_median = balkans_male["TMAXLN"].median()
balkans_male_q1 = balkans_male["TMAXLN"].quantile(0.25)
balkans_male_q3 = balkans_male["TMAXLN"].quantile(0.75)

# Balkans Female
balkans_female_n = balkans_female["TMAXLN"].count()
balkans_female_median = balkans_female["TMAXLN"].median()
balkans_female_q1 = balkans_female["TMAXLN"].quantile(0.25)
balkans_female_q3 = balkans_female["TMAXLN"].quantile(0.75)

# Britain Male
britain_male_n = britain_male["TMAXLN"].count()
britain_male_median = britain_male["TMAXLN"].median()
britain_male_q1 = britain_male["TMAXLN"].quantile(0.25)
britain_male_q3 = britain_male["TMAXLN"].quantile(0.75)

# Britain Female
britain_female_n = britain_female["TMAXLN"].count()
britain_female_median = britain_female["TMAXLN"].median()
britain_female_q1 = britain_female["TMAXLN"].quantile(0.25)
britain_female_q3 = britain_female["TMAXLN"].quantile(0.75)

# Iberia Male
iberia_male_n = iberia_male["TMAXLN"].count()
iberia_male_median = iberia_male["TMAXLN"].median()
iberia_male_q1 = iberia_male["TMAXLN"].quantile(0.25)
iberia_male_q3 = iberia_male["TMAXLN"].quantile(0.75)

# Iberia Female
iberia_female_n = iberia_female["TMAXLN"].count()
iberia_female_median = iberia_female["TMAXLN"].median()
iberia_female_q1 = iberia_female["TMAXLN"].quantile(0.25)
iberia_female_q3 = iberia_female["TMAXLN"].quantile(0.75)

# N.-Cen. Europe Male
ncenteuro_male_n = ncenteuro_male["TMAXLN"].count()
ncenteuro_male_median = ncenteuro_male["TMAXLN"].median()
ncenteuro_male_q1 = ncenteuro_male["TMAXLN"].quantile(0.25)
ncenteuro_male_q3 = ncenteuro_male["TMAXLN"].quantile(0.75)

# N.-Cen. Europe Female
ncenteuro_female_n = ncenteuro_female["TMAXLN"].count()
ncenteuro_female_median = ncenteuro_female["TMAXLN"].median()
ncenteuro_female_q1 = ncenteuro_female["TMAXLN"].quantile(0.25)
ncenteuro_female_q3 = ncenteuro_female["TMAXLN"].quantile(0.75)

# Scand./Finland Male
scandfin_male_n = scandfin_male["TMAXLN"].count()
scandfin_male_median = scandfin_male["TMAXLN"].median()
scandfin_male_q1 = scandfin_male["TMAXLN"].quantile(0.25)
scandfin_male_q3 = scandfin_male["TMAXLN"].quantile(0.75)

# Scand./Finland Female
scandfin_female_n = scandfin_female["TMAXLN"].count()
scandfin_female_median = scandfin_female["TMAXLN"].median()
scandfin_female_q1 = scandfin_female["TMAXLN"].quantile(0.25)
scandfin_female_q3 = scandfin_female["TMAXLN"].quantile(0.75)


# Figure 1.4 - Humeral asymmetry
# Histogram shows the distributions

# AP Rural
rural_ap_n = rural_ap.count()
rural_ap_mean = rural_ap.mean()
rural_ap_sd = rural_ap.std()

# AP Urban
urban_ap_n = urban_ap.count()
urban_ap_mean = urban_ap.mean()
urban_ap_sd = urban_ap.std()

# ML Rural
rural_ml_n = rural_ml.count()
rural_ml_mean = rural_ml.mean()
rural_ml_sd = rural_ml.std()

# ML Urban
urban_ml_n = urban_ml.count()
urban_ml_mean = urban_ml.mean()
urban_ml_sd = urban_ml.std()


# Put all descriptive statistics into one table

descriptive_stats = pd.DataFrame({

    "Figure": [
        "1.1", "1.1", "1.1", "1.1",
        "1.2", "1.2", "1.2", "1.2", "1.2",
        "1.3", "1.3", "1.3", "1.3", "1.3",
        "1.3", "1.3", "1.3", "1.3", "1.3",
        "1.4", "1.4", "1.4", "1.4"
    ],

    "Variable": [
        "Stature (cm)", "Stature (cm)", "Stature (cm)", "Stature (cm)",
        "Age at death (years)", "Age at death (years)",
        "Age at death (years)", "Age at death (years)", "Age at death (years)",
        "Max tibia length (mm)", "Max tibia length (mm)",
        "Max tibia length (mm)", "Max tibia length (mm)",
        "Max tibia length (mm)", "Max tibia length (mm)",
        "Max tibia length (mm)", "Max tibia length (mm)",
        "Max tibia length (mm)", "Max tibia length (mm)",
        "AP percent asymmetry", "AP percent asymmetry",
        "ML percent asymmetry", "ML percent asymmetry"
    ],

    "Group": [
        "Urban Male", "Rural Male", "Urban Female", "Rural Female",
        "Neolithic", "Bronze", "Iron/Roman",
        "Early Medieval", "Late Medieval",
        "Balkans Male", "Balkans Female",
        "Britain Male", "Britain Female",
        "Iberia Male", "Iberia Female",
        "N.-Cen. Europe Male", "N.-Cen. Europe Female",
        "Scand./Finland Male", "Scand./Finland Female",
        "Rural", "Urban", "Rural", "Urban"
    ],

    "N": [
        urban_male_n, rural_male_n, urban_female_n, rural_female_n,
        neolithic_n, bronze_n, iron_roman_n,
        early_medieval_n, late_medieval_n,
        balkans_male_n, balkans_female_n,
        britain_male_n, britain_female_n,
        iberia_male_n, iberia_female_n,
        ncenteuro_male_n, ncenteuro_female_n,
        scandfin_male_n, scandfin_female_n,
        rural_ap_n, urban_ap_n, rural_ml_n, urban_ml_n
    ],

    "Mean": [
        np.nan, np.nan, np.nan, np.nan,
        neolithic_mean, bronze_mean, iron_roman_mean,
        early_medieval_mean, late_medieval_mean,
        np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan,
        rural_ap_mean, urban_ap_mean, rural_ml_mean, urban_ml_mean
    ],

    "SD": [
        np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan,
        rural_ap_sd, urban_ap_sd, rural_ml_sd, urban_ml_sd
    ],

    "Median": [
        urban_male_median, rural_male_median,
        urban_female_median, rural_female_median,
        np.nan, np.nan, np.nan, np.nan, np.nan,
        balkans_male_median, balkans_female_median,
        britain_male_median, britain_female_median,
        iberia_male_median, iberia_female_median,
        ncenteuro_male_median, ncenteuro_female_median,
        scandfin_male_median, scandfin_female_median,
        np.nan, np.nan, np.nan, np.nan
    ],

    "Q1": [
        urban_male_q1, rural_male_q1,
        urban_female_q1, rural_female_q1,
        np.nan, np.nan, np.nan, np.nan, np.nan,
        balkans_male_q1, balkans_female_q1,
        britain_male_q1, britain_female_q1,
        iberia_male_q1, iberia_female_q1,
        ncenteuro_male_q1, ncenteuro_female_q1,
        scandfin_male_q1, scandfin_female_q1,
        np.nan, np.nan, np.nan, np.nan
    ],

    "Q3": [
        urban_male_q3, rural_male_q3,
        urban_female_q3, rural_female_q3,
        np.nan, np.nan, np.nan, np.nan, np.nan,
        balkans_male_q3, balkans_female_q3,
        britain_male_q3, britain_female_q3,
        iberia_male_q3, iberia_female_q3,
        ncenteuro_male_q3, ncenteuro_female_q3,
        scandfin_male_q3, scandfin_female_q3,
        np.nan, np.nan, np.nan, np.nan
    ]
})

# Round numerical values to two decimal places
descriptive_stats = descriptive_stats.round(2)

# Print the table
print(descriptive_stats.to_string(index=False))

# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# DATASET 2
# Dataset name / identifier: DOI:https://doi.org/10.7910/DVN/OCYM7I
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


# -----------------------------------------------------------------------------
# 2.0 PRINT THE DATASET BANNER
# -----------------------------------------------------------------------------
text=("Norrbottens county lithic dataset - DOI: https://doi.org/10.7910/DVN/OCYM7I")
def banner(text, ch="=", length=70):
    print(ch * length)
    print(text.center(length))
    print(ch * length)
banner(text)


# -----------------------------------------------------------------------------
# 2.1 READ THE DATASET (Task 1)
# -----------------------------------------------------------------------------
df = pd.read_csv("Norrbottens_county_lithic_dataset_1_copy.csv", sep=";")

# Filtering Tool types to only show the Axes, keeping into account the capital letter
Axe_dimensions = df[df["Type"].str.contains("axe", case=False)]

#Filtering the Material colum to only show the values containing Stone or Slate
Axe_dimensions = Axe_dimensions[Axe_dimensions['Material'].isin(["Slate", "Stone"])]

#Filtering to only show the chissels with the material and weight
Chissel = df[df["Type"].str.contains("chisel", case=False)]


# -----------------------------------------------------------------------------
# 2.2 VISUALISATIONS (Task 2)
# -----------------------------------------------------------------------------

# --- FIGURE 2.1 ---
# Print caption:
print ("Figure1.1: In this figure, the blade length and width of",
       " stone axes vs the blade length and width of slate axes are",
       " visualized. This is to visualize possible differences between",
       " these different material axes")
# Code:
plt.figure(1)
sns.scatterplot(
    data=Axe_dimensions, 
    x='Blade_length_(mm)', 
    y="Blade_width_(mm)", 
    hue="Material"
    )

plt.title("Figure 1: Blade Dimensions: Slate vs Stone")
plt.xlabel("Blade length in mm")
plt.ylabel("Blade width in mm")
plt.show()

# --- FIGURE 2.2 ---
# Print caption:
print("Figure 2.2: This figure shows an overview of the total of finds",
      " found per Parish")

# Code:
plt.figure(2)
sns.histplot(
    data= df, 
    x= "Parish"
    )

plt.title("Figure 2.2: Total finds per Parish")
plt.xticks(rotation=90, ha="center")
plt.xlabel("Parish")
plt.ylabel("Finds")
plt.show()

# --- FIGURE 2.3 ---
# Print caption:
print("Figure 2.3: This figure shows the weight distribution in grams per",
      " chisel type found. this visualization is filtered by material to show",
      " the difference per material aswell")

# Code:
plt.figure(figsize=(10, 5))
sns.scatterplot(
    data=Chissel, 
    x="Weight_(g)", 
    y="Type", 
    hue="Material"
    )

plt.title("Figure 2.3: Weight distribution of chisel type per material")
plt.legend(title="Material", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xlabel("Weight(g)")
plt.ylabel("Chisel Type")
plt.show()


# --- FIGURE 2.4 ---
# Print caption:
print("Figure 2.4: This figure shows the difference between blade length and",
      " length of slate and stone axes. Between these is a line drawn to show",
      " if there is a relationship between these values.")

# Code:
sns.lmplot(
    data=Axe_dimensions, 
    x="Length_(mm)", 
    y="Blade_length_(mm)", 
    hue="Material", 
    )

plt.title("Figure 2.4: Difference between the blade length and length of slate and stone axes")
plt.xlabel("Length (mm)")
plt.ylabel("Blade length (mm)")
plt.show()


# -----------------------------------------------------------------------------
# 2.3 DESCRIPTIVE STATISTICS (Task 3)
# -----------------------------------------------------------------------------

# --- TABLE 2 ---
# Print caption:

print("This table shows the input data for figure 2," 
" allowing for the illustration of the total numnber of finds per Parish. ")

# Code:
summary = df.describe().drop(["25%", "50%", "75%"])
print(summary)


# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# DATASET 3
# Dataset name / identifier: DOI:https://www.doi.org/10.48493/sak5-9487
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


# -----------------------------------------------------------------------------
# 3.0 PRINT THE DATASET BANNER
# -----------------------------------------------------------------------------
text=("Incrematal Dental Dataset - DOI: https://www.doi.org/10.48493/sak5-9487")
def banner(text, ch='=', length=70):
    print(ch * length)
    print (text.center(length))
    print(ch * length)
banner(text)


# -----------------------------------------------------------------------------
# 3.1 READ THE DATASET (Task 1)
# -----------------------------------------------------------------------------
df = pd.read_csv("Incremental_DentalClean_Data.csv", 
                 sep=";")


# -----------------------------------------------------------------------------
# 3.2 VISUALISATIONS (Task 2)
# -----------------------------------------------------------------------------

# --- FIGURE 3.1 ---
# Print caption:
print("Figure 3.1: This bar chart shows the number of tooth samples that are",
      "examined during this research.","These teeth were found in different",
      "countries around the world. Green shows the amount of teeth from",
      "individuals with a low status, and red shows the higher status.")
# Code:

#reading the database
Figure1 = pd.read_csv("Incremental_DentalClean_Data.csv",
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
print("Figure 3.2: This figure shows the difference within the maximum age of different",
      "individuals based on their culture. The blue color shows the max. age",
      "of men, and the pink shows the age of women in those cultures. The ages from",
      "English, Japanese, and Nubian/Meroitic cultures were the highest.")
# Code:

#reading the database
Figure2 = pd.read_csv("Incremental_DentalClean_Data.csv", sep=";")
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
print("Figure 3.3: This boxplot shows the difference within the social status",
      "of the individuals based on the age. The purple boxplot shows the age",
      "of low-status individuals. Their age was between 30 and 40 years old.",
      "The individuals with a high status (green) had an age between 30 and 75.")   
# Code:

#reading the database
Figure3 = pd.read_csv("Incremental_DentalClean_Data.csv", sep=";")
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
print("Figure 3.4: This figure shows the δ13C collagen values spread over different",
      "time periods. This collagen shows the dietary protein people consumed.",
      "Most of the collagen was found around in 1750. The blue color shows",
      "the amount of man consumed, and the pink of women.")
# Code:

#reading the database

Figure4 = pd.read_csv("Incremental_DentalClean_Data.csv", sep=";")
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

#reading the database
Table = pd.read_csv("Incremental_DentalClean_Data.csv", sep=";")

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
text=("Coins from findscatalogue - DOI:")
def banner(text, ch='=', length=70):
    print(ch * length)
    print (text.center(length))
    print(ch * length)
banner(text)


# -----------------------------------------------------------------------------
# 4.1 READ THE DATASET (Task 1)
# -----------------------------------------------------------------------------
df = pd.read_csv ('muntjescompleet88888.csv', sep=";")

# removing the metal prefix from the "subcategorie" colum so it just states the type of metal now
df["subcategorie"] = df["subcategorie"].str.replace("metaal:", "")

# -----------------------------------------------------------------------------
# 4.2 VISUALISATIONS (Task 2)
# -----------------------------------------------------------------------------

# --- FIGURE 4.1 ---
# Print caption:
print("figure 4.1: A stacked graph of coins by enddate and material aka",
      " subcategorie grouped in 140 bins and specifyied for the timeframe",
      " of 1350ad to current day.")
# Code:
sns.displot(
    data=df, 
    x='eind_dat', 
    hue='subcategorie', 
    multiple="stack", 
    bins=140
    )

plt.xlim(1350,2026)
plt.title("Figure 4.1: A graph of coins subdevided by type of material")
plt.show ()

# --- FIGURE 4.2 ---
# Print caption:
print("figure 4.2: Same as figure 1 but not subdevided into subcategorie")
# Code:
sns.displot(
    data=df, 
    x='eind_dat', 
    bins=140
    )

plt.xlim(1350,2026)
plt.title("Figure 4.2: Count of total coins found per year ")
plt.show()

# --- FIGURE 4.3 ---
# Print caption:
print("figure 4.3: Counts grouped by subcategory aka metal type")
# Code:
sns.histplot(
    data=df, 
    y="subcategorie"
    )

plt.title("Figure 4.3: Counts grouped by subcategory metal type")
plt.show()

# --- FIGURE 4.4 ---
# Print caption:
print("figure 4.4: Material composition per site")
# Code:
sns.displot(
    data=df, 
    x='project_code', 
    hue='subcategorie', 
    multiple="stack"
    )

plt.title("Figure 4.4: Material composition per site")
plt.show()

# -----------------------------------------------------------------------------
# 4.3 DESCRIPTIVE STATISTICS (Task 3)
# -----------------------------------------------------------------------------

# --- TABLE 4 ---
# Print caption:
print("descriptive statistics")
# Code:
print(df[["eind_dat", "begin_dat", 'munt_lengte_diameter_in_mm','vlak_max']].describe())


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
