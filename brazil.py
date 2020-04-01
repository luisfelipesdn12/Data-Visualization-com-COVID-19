# -*- coding: utf-8 -*-

####### Data Analyzation:
import pandas as pd

dataset_pd = pd.read_csv(r'./datasets/brazil_covid19.csv')

#define the columns
state_column = dataset_pd['state'].tolist()
cases_column = dataset_pd['cases'].tolist()
deaths_column = dataset_pd['deaths'].tolist()
date_column = dataset_pd['date'].tolist()

def returnDatesWithoutRepeat():
    '''
    Return a list() of the dates in the
    dataset with just one item for date.
    '''
    date_column = dataset_pd['date'].tolist()
    dates_without_repeat = list()

    for date in date_column:
        if date not in dates_without_repeat:
            dates_without_repeat.append(date)

    return(dates_without_repeat)

def returnAllCasesInASpecificDate(specificdate:str):
    '''
    Given a specific date, returns an
    int() number of all the cases in it.
    '''
    cases_column = dataset_pd['cases'].tolist()
    date_column = dataset_pd['date'].tolist()

    cases_in_this_date_list = list()

    for c in range(len(date_column)):
        if date_column[c] == specificdate:
            cases_in_this_date_list.append(cases_column[c])

    cases_added = 0
    for case in cases_in_this_date_list:
        cases_added += case

    return(cases_added)

def returnAllDeathsInASpecificDate(specificdate:str):
    '''
    Given a specific date, returns an
    int() number of all the deaths in it.
    '''
    deaths_column = dataset_pd['deaths'].tolist()
    date_column = dataset_pd['date'].tolist()

    deaths_in_this_date_list = list()

    for c in range(len(date_column)):
        if date_column[c] == specificdate:
            deaths_in_this_date_list.append(deaths_column[c])

    deaths_added = 0
    for death in deaths_in_this_date_list:
        deaths_added += death

    return(deaths_added)

def returnAllCasesForEachDate():
    '''
    Returns a dict(), the keys represents
    the dates, the values represents the cases in it.
    '''
    dates_without_repeat = returnDatesWithoutRepeat()
    dates_and_cases = dict()

    for date in dates_without_repeat:
        dates_and_cases[date] = returnAllCasesInASpecificDate(date)

    return(dates_and_cases)

def returnAllDeathsForEachDate():
    '''
    Returns a dict(), the keys represents
    the dates, the values represents the deaths in it.
    '''
    dates_without_repeat = returnDatesWithoutRepeat()
    dates_and_deaths = dict()

    for date in dates_without_repeat:
        dates_and_deaths[date] = returnAllDeathsInASpecificDate(date)

    return(dates_and_deaths)


def returnDictOfDateAndCasesInAMonth( month:str, some_dict = returnAllCasesForEachDate()):
    '''
    Returns a dict that contains just the
    dates and cases of a especific month.

    Ask for 2 arguments:
        1. one dict with dates being the keys and
    the cases being the values. (opitional,
    for default uses the dict returned in
    returnAllCasesForEachDate() function);
        2. A month in str() format, e.g.:'03'.
    (needed, has not a default value);
    '''
    new_dict = dict()
    some_dict_keys = list(some_dict.keys())
    some_dict_values = list(some_dict.values())


    for c in range(len(some_dict_keys)):
        if some_dict_keys[c][5:7] == month:
            new_dict[some_dict_keys[c]] = some_dict_values[c]

    return(new_dict)

def returnDictOfDateAndDeathsInAMonth( month:str, some_dict = returnAllDeathsForEachDate()):
    '''
    Returns a dict that contains just the
    dates and deaths of a especific month.

    Ask for 2 arguments:
        1. one dict with dates being the keys and
    the deaths being the values. (opitional,
    for default uses the dict returned in
    returnAllDeathsForEachDate() function);
        2. A month in str() format, e.g.:'03'.
    (needed, has not a default value);
    '''
    new_dict = dict()
    some_dict_keys = list(some_dict.keys())
    some_dict_values = list(some_dict.values())


    for c in range(len(some_dict_keys)):
        if some_dict_keys[c][5:7] == month:
            new_dict[some_dict_keys[c]] = some_dict_values[c]

    return(new_dict)

def returnDictOfDateAndCases(city:str, month:str):
    '''
    Returns a dict that contains the dates
    and cases given a specific month and a
    especific city, both in str() format.
    '''
    city_cases = list()
    date_of_cases = list()
    just_the_day = list()

    for c in range(len(cases_column)):
        if date_column[c][5:7] == str(month) and state_column[c] == str(city):
            city_cases.append(int(cases_column[c]))
            date_of_cases.append(date_column[c])
            just_the_day.append(int(date_column[c][8:]))

    date_and_cases = dict()
    date_and_cases['date'] = date_of_cases
    date_and_cases['date_days'] = just_the_day
    date_and_cases['cases'] = city_cases

    return(date_and_cases)

def returnDictOfDateAndDeaths(city:str, month:str):
    '''
    Returns a dict that contains the dates
    and deaths given a specific month and a
    especific city, both in str() format.
    '''
    city_deaths = list()
    date_of_deaths = list()
    just_the_day = list()

    for c in range(len(deaths_column)):
        if date_column[c][5:7] == str(month) and state_column[c] == str(city):
            city_deaths.append(int(deaths_column[c]))
            date_of_deaths.append(date_column[c])
            just_the_day.append(int(date_column[c][8:]))

    date_and_deaths = dict()
    date_and_deaths['date'] = date_of_deaths
    date_and_deaths['date_days'] = just_the_day
    date_and_deaths['deaths'] = city_deaths

    return(date_and_deaths)

def returnJustDays(some_list:list):
    '''
    Returns a list() with just the days
    given a list with complete dates in
    the format '2020-03-30'.
    e.g.: Given '1990-12-14', returns '14'.
    '''
    just_days = list()

    for date in some_list:
        just_the_day = int(date[8:])
        just_days.append(just_the_day)

    return(just_days)

####### Data visualization:

dates_and_cases_in_mar = returnDictOfDateAndCasesInAMonth(month='03')
dates_and_deaths_in_mar = returnDictOfDateAndDeathsInAMonth(month='03')

import matplotlib.pyplot as plt
import matplotlib.axes as maxes

def plotABoxplot():
    fig, axs = plt.subplots(1, 2, figsize=(8,5))
    fig.suptitle('BOXPLOT - Comparação da média de casos de COVID-19\n reportados por dia em São Paulo em Fevereiro e Março')
    fonte = 'Dados: Ministério da Saúde - 28/03/2020 às 17:00'

    bplot0 = axs[0].boxplot(returnDictOfDateAndCases('São Paulo', '02')['cases'], patch_artist=True, labels=[''])
    bplot1 = axs[1].boxplot(returnDictOfDateAndCases('São Paulo', '03')['cases'], patch_artist=True, labels=[''])

    bplot1['boxes'][0].set_facecolor('lightblue')
    axs[0].set_ylabel('Número de casos')
    axs[0].set_xlabel('Fevereiro')
    axs[0].grid(True, axis='y', linestyle='--')
    axs[1].set_xlabel('Março')
    axs[1].grid(True, axis='y', linestyle='--')

    plt.savefig('BOXPLOT Comparação da média de casos de COVID-19 reportados por dia em São Paulo em Fevereiro e Março.png'.replace(' ', '-'), dpi=400)
    plt.show()

def plotCases():
    fig, ax = plt.subplots(figsize=(8,4))
    sp_dates = returnDictOfDateAndCases('São Paulo', '03')['date_days']
    sp_cases = returnDictOfDateAndCases('São Paulo', '03')['cases']
    ax.plot(sp_dates, sp_cases)

    brazil_dates = returnJustDays(list(dates_and_cases_in_mar.keys()))
    brazil_cases = list(dates_and_cases_in_mar.values())

    def returnDatesAndCasesWithoutSP():
        dates_and_cases_without_sp = dict()

        for c in range(len(brazil_cases)):
            cases_without_sp = brazil_cases[c] - sp_cases[c]
            dates_and_cases_without_sp[brazil_dates[c]] = cases_without_sp

        return(dates_and_cases_without_sp)

    brazil_without_sp_cases = list(returnDatesAndCasesWithoutSP().values())

    ax.plot(brazil_dates,
            brazil_cases,
            color='red')
    ax.scatter(brazil_dates, brazil_cases, color='red')

    from pprint import pprint
    print('dates_and_cases_without_sp:')
    pprint(returnDatesAndCasesWithoutSP())
    ax.plot(brazil_dates,
            brazil_without_sp_cases,
            color='green')
    ax.scatter(brazil_dates, brazil_without_sp_cases, color='green')

    ax.scatter(sp_dates, sp_cases, color='C0')
    fig.suptitle('Comparação do número de casos de COVID-19 reportados por dia em São Paulo, \nBrasil sem São Paulo e Brasil no mês de Março')
    #fig.set_ylabel('somke')
    ax.set_ylabel('Número de casos')
    ax.set_xlabel('Dia do mês (Março)')
    plt.grid(True)
    plt.subplots_adjust(top=0.87, left=0.10, bottom=0.20, right=0.95)

    import matplotlib.patches as mpatches

    C0_patch = mpatches.Patch(color='C0', label='São Paulo')
    green_patch = mpatches.Patch(color='green', label='Brasil sem São Paulo')
    red_patch = mpatches.Patch(color='red', label='Brasil')
    plt.legend(handles=[C0_patch, red_patch, green_patch], loc='upper left')
    source = r'''Elaborado a partir dos dados do Ministério da Saúde sobre o COVID-19.
Disponível em: <kaggle.com/unanimad/corona-virus-brazil>. Acesso em: 31/03/2020 às 19:27.'''
    plt.annotate(source, (0,0), (-44,-37), fontsize=8,
             xycoords='axes fraction', textcoords='offset points', va='top')
    plt.savefig(dpi=400, fname=r'./img/Comparação do número de casos de COVID-19 reportados por dia em São Paulo Brasil sem São Paulo e Brasil no mês de Março-atl3003.png'.replace(' ', '-'))
    plt.show()

def plotDeaths():
    fig, ax = plt.subplots(figsize=(8,4))
    sp_dates = returnDictOfDateAndDeaths('São Paulo', '03')['date_days']
    sp_deaths = returnDictOfDateAndDeaths('São Paulo', '03')['deaths']
    ax.plot(sp_dates, sp_deaths)

    brazil_dates = returnJustDays(list(dates_and_deaths_in_mar.keys()))
    brazil_deaths = list(dates_and_deaths_in_mar.values())

    def returnDatesAndDeathsWithoutSP():
        dates_and_deaths_without_sp = dict()

        for c in range(len(brazil_deaths)):
            deaths_without_sp = brazil_deaths[c] - sp_deaths[c]
            dates_and_deaths_without_sp[brazil_dates[c]] = deaths_without_sp

        return(dates_and_deaths_without_sp)

    brazil_without_sp_deaths = list(returnDatesAndDeathsWithoutSP().values())

    ax.plot(brazil_dates,
            brazil_deaths,
            color='red')
    ax.scatter(brazil_dates, brazil_deaths, color='red')

    from pprint import pprint
    print('dates_and_deaths_without_sp:')
    pprint(returnDatesAndDeathsWithoutSP())
    ax.plot(brazil_dates,
            brazil_without_sp_deaths,
            color='green')
    ax.scatter(brazil_dates, brazil_without_sp_deaths, color='green')

    ax.scatter(sp_dates, sp_deaths, color='C0')
    fig.suptitle('Comparação do número de óbitos causados por COVID-19 por dia em São Paulo, \nBrasil sem São Paulo e Brasil no mês de Março')
    #fig.set_ylabel('somke')
    ax.set_ylabel('Número de óbitos')
    ax.set_xlabel('Dia do mês (Março)')
    plt.grid(True)
    plt.subplots_adjust(top=0.87, left=0.10, bottom=0.20, right=0.95)

    import matplotlib.patches as mpatches

    C0_patch = mpatches.Patch(color='C0', label='São Paulo')
    green_patch = mpatches.Patch(color='green', label='Brasil sem São Paulo')
    red_patch = mpatches.Patch(color='red', label='Brasil')
    plt.legend(handles=[C0_patch, red_patch, green_patch], loc='upper left')
    source = r'''Elaborado a partir dos dados do Ministério da Saúde sobre o COVID-19.
Disponível em: <kaggle.com/unanimad/corona-virus-brazil>. Acesso em: 31/03/2020 às 19:27.'''
    plt.annotate(source, (0,0), (-44,-37), fontsize=8,
             xycoords='axes fraction', textcoords='offset points', va='top')
    plt.savefig(dpi=400, fname=r'./img/Comparação do número de óbitos causados pr COVID-19 reportados por dia em São Paulo Brasil sem São Paulo e Brasil no mês de Março-atl3003.png'.replace(' ', '-'))
    plt.show()

#plotCases()
plotDeaths()
