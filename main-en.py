# -*- coding: utf-8 -*-

import pandas as pd

dataset_pd = pd.read_csv(r'./COVID19_line_list_data.csv')

age_of_all_raw = dataset_pd['age'].tolist()
death_or_not_raw = dataset_pd['death'].tolist()

age_of_all = list()

for c in range(0, len(age_of_all_raw)):
  if age_of_all_raw[c] in range(0, 150):
    age_of_all.append(age_of_all_raw[c])

age_of_deaths = list()

for c in range(0, len(age_of_all_raw)):
  if age_of_all_raw[c] in range(0, 150) and death_or_not_raw[c] in (1, '1'):
    age_of_deaths.append(age_of_all_raw[c])

import matplotlib.pyplot as plt

plt.title('BOXPLOT - Age comparation between total cases \nand death cases in COVID-19 patients')
plt.ylabel('Age of patients')
plt.xlabel('Total number of analyzed patients: 1085')
plt.grid('True')
bplot = plt.boxplot([age_of_all, age_of_deaths], labels=['', ''], patch_artist=True)

bplot['boxes'][0].set_facecolor('lightblue')
bplot['boxes'][1].set_facecolor('pink')

import matplotlib.patches as mpatches

lightblue_patch = mpatches.Patch(color='lightblue', label='Total cases')
pink_patch = mpatches.Patch(color='pink', label='Death cases')
plt.legend(handles=[lightblue_patch, pink_patch], loc='lower center')

#plt.show()
plt.savefig(dpi=400, fname='BOXPLOT Age comparation between total cases and death cases in COVID-19 patients.png'.replace(' ', '-'))
