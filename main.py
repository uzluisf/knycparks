"""
Name: Luis Filion
Subject: Data Science project
Professor: Katherine St. John
Date: December 10, 2021
Description: Code used to clean up the data and generates the graphs.
URL: https://uzluisf.github.io/knycparks/
Resources: NYC Parks Crime Statistics (https://www1.nyc.gov/site/nypd/stats/crime-statistics/park-crime-stats.page), Open Space NYC Parks (https://data.cityofnewyork.us/Recreation/Open-Space-Parks-/g84h-jbjm), Pandas (https://pandas.pydata.org/), Matplotlib (https://matplotlib.org/), seaborn (https://seaborn.pydata.org/)
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

SOURCE = "./nycps"
DEST = "./bxparks"

# Read each of the files from SOURCE which contains all the parks and filter
# BRONX parks whose total number of crimes is at least 1, remove and rename some
# columns, and save the resulting DF to DEST.

def getbxparks(df):
    # get parks in the bronx with more than zero crimes.
    df = df[(df['BOROUGH'] == 'BRONX') & (df['TOTAL'] > 0)]
    # drop and rename some columns
    df = df.drop(columns=['BOROUGH', 'SIZE (ACRES)', 'CATEGORY', 'YEAR', 'QUARTER'])
    df.rename(columns = 
        {   'MURDER':'M',
            'RAPE':'RP',
            'ROBBERY' : 'RB', 
            'FELONY ASSAULT' : 'FA',
            'BURGLARY' : 'BG', 
            'GRAND LARCENY' : 'GL',
            'GRAND LARCENY OF MOTOR VEHICLE' : 'GLM'
        },
        inplace = True
    )
    return df

for filename in os.listdir(SOURCE):
    csvfile = os.path.join(SOURCE, filename)
    df = pd.read_csv(os.path.join(SOURCE, filename))
    
    newdf = getbxparks(df)
    filename = '-'.join(['bxparks'] + filename.split('-')[1:])
    newdf.to_csv(os.path.join(DEST, filename), index=False)

#
# Combine all quarter CSVs into a year
#

BXPARKSYEARS = "./bxparksyears/"

# 2014
df3 = pd.read_csv("./bxparks/bxparks-2014-q3.csv")
df4 = pd.read_csv("./bxparks/bxparks-2014-q4.csv")

concat = pd.concat([df3, df4])
concat = concat.groupby('PARK', as_index=False).sum()
concat.to_csv(BXPARKSYEARS + '2014.csv', index=False)

# 2015
df1 = pd.read_csv("./bxparks/bxparks-2015-q1.csv")
df2 = pd.read_csv("./bxparks/bxparks-2015-q2.csv")
df3 = pd.read_csv("./bxparks/bxparks-2015-q3.csv")
df4 = pd.read_csv("./bxparks/bxparks-2015-q4.csv")

concat = pd.concat([df1, df2, df3, df4])
concat = concat.groupby('PARK', as_index=False).sum()
concat.to_csv(BXPARKSYEARS + '2015.csv', index=False)

# 2016
df1 = pd.read_csv("./bxparks/bxparks-2016-q1.csv")
df2 = pd.read_csv("./bxparks/bxparks-2016-q2.csv")
df3 = pd.read_csv("./bxparks/bxparks-2016-q3.csv")
df4 = pd.read_csv("./bxparks/bxparks-2016-q4.csv")

concat = pd.concat([df1, df2, df3, df4])
concat = concat.groupby('PARK', as_index=False).sum()
concat.to_csv(BXPARKSYEARS + '2016.csv', index=False)

# 2017
df1 = pd.read_csv("./bxparks/bxparks-2017-q1.csv")
df2 = pd.read_csv("./bxparks/bxparks-2017-q2.csv")
df3 = pd.read_csv("./bxparks/bxparks-2017-q3.csv")
df4 = pd.read_csv("./bxparks/bxparks-2017-q4.csv")

concat = pd.concat([df1, df2, df3, df4])
concat = concat.groupby('PARK', as_index=False).sum()
concat.to_csv(BXPARKSYEARS + '2017.csv', index=False)

# 2018
df1 = pd.read_csv("./bxparks/bxparks-2018-q1.csv")
df2 = pd.read_csv("./bxparks/bxparks-2018-q2.csv")
df3 = pd.read_csv("./bxparks/bxparks-2018-q3.csv")
df4 = pd.read_csv("./bxparks/bxparks-2018-q4.csv")

concat = pd.concat([df1, df2, df3, df4])
concat = concat.groupby('PARK', as_index=False).sum()
concat.to_csv(BXPARKSYEARS + '2018.csv', index=False)

# 2019
df1 = pd.read_csv("./bxparks/bxparks-2019-q1.csv")
df2 = pd.read_csv("./bxparks/bxparks-2019-q2.csv")
df3 = pd.read_csv("./bxparks/bxparks-2019-q3.csv")
df4 = pd.read_csv("./bxparks/bxparks-2019-q4.csv")

concat = pd.concat([df1, df2, df3, df4])
concat = concat.groupby('PARK', as_index=False).sum()
concat.to_csv(BXPARKSYEARS + '2019.csv', index=False)

# 2020
df1 = pd.read_csv("./bxparks/bxparks-2020-q1.csv")
df2 = pd.read_csv("./bxparks/bxparks-2020-q2.csv")
df3 = pd.read_csv("./bxparks/bxparks-2020-q3.csv")
df4 = pd.read_csv("./bxparks/bxparks-2020-q4.csv")

concat = pd.concat([df1, df2, df3, df4])
concat = concat.groupby('PARK', as_index=False).sum()
concat.to_csv(BXPARKSYEARS + '2020.csv', index=False)

# 2020
df1 = pd.read_csv("./bxparks/bxparks-2021-q1.csv")
df2 = pd.read_csv("./bxparks/bxparks-2021-q2.csv")

concat = pd.concat([df1, df2])
concat = concat.groupby('PARK', as_index=False).sum()
concat.to_csv(BXPARKSYEARS + '2021.csv', index=False)

df2014 = pd.read_csv("./bxparksyears/2014.csv")
df2015 = pd.read_csv("./bxparksyears/2015.csv")
df2016 = pd.read_csv("./bxparksyears/2016.csv")
df2017 = pd.read_csv("./bxparksyears/2017.csv")
df2018 = pd.read_csv("./bxparksyears/2018.csv")
df2019 = pd.read_csv("./bxparksyears/2019.csv")
df2020 = pd.read_csv("./bxparksyears/2020.csv")
df2021 = pd.read_csv("./bxparksyears/2021.csv")

# select first five parks with most crime for 2014. These are the parks that
# will be used for next years as well.
selectparks = df2014.sort_values(by=['TOTAL'], ascending=False)['PARK'].to_list()[:5]

# collect yearly total crimes for selected parks.
parkstotal = defaultdict(list)
for park in selectparks:
    selected2014 = df2014[df2014['PARK'].isin(selectparks)]
    selected2015 = df2015[df2015['PARK'].isin(selectparks)]
    selected2016 = df2016[df2016['PARK'].isin(selectparks)]
    selected2017 = df2017[df2017['PARK'].isin(selectparks)]
    selected2018 = df2018[df2018['PARK'].isin(selectparks)]
    selected2019 = df2019[df2019['PARK'].isin(selectparks)]
    selected2020 = df2020[df2020['PARK'].isin(selectparks)]
    selected2021 = df2021[df2021['PARK'].isin(selectparks)]

    if selected2014[selected2014['PARK'] == park]['TOTAL'].any():
        parkstotal[park].append(("2014", int(selected2014[selected2014['PARK'] == park]['TOTAL'])))

    if selected2015[selected2015['PARK'] == park]['TOTAL'].any():
        parkstotal[park].append(("2015", int(selected2015[selected2015['PARK'] == park]['TOTAL'])))

    if selected2016[selected2016['PARK'] == park]['TOTAL'].any():
        parkstotal[park].append(("2016", int(selected2016[selected2016['PARK'] == park]['TOTAL'])))

    if selected2017[selected2017['PARK'] == park]['TOTAL'].any():
        parkstotal[park].append(("2017", int(selected2017[selected2017['PARK'] == park]['TOTAL'])))

    if selected2018[selected2018['PARK'] == park]['TOTAL'].any():
        parkstotal[park].append(("2018", int(selected2018[selected2018['PARK'] == park]['TOTAL'])))

    if selected2019[selected2019['PARK'] == park]['TOTAL'].any():
        parkstotal[park].append(("2019", int(selected2019[selected2019['PARK'] == park]['TOTAL'])))

    if selected2020[selected2020['PARK'] == park]['TOTAL'].any():
        parkstotal[park].append(("2020", int(selected2020[selected2020['PARK'] == park]['TOTAL'])))

    if selected2021[selected2021['PARK'] == park]['TOTAL'].any():
        parkstotal[park].append(("2021", int(selected2021[selected2021['PARK'] == park]['TOTAL'])))


# create ./images diretory if it doesn't exist.
imgdir = './images/'
if not os.path.exists(imgdir):
    os.makedirs(imgdir)

#
# create bar plots for selected parks.
#

park = 'CROTONA PARK'
lst = parkstotal[park]
x, y = [t[0] for t in lst], [t[1] for t in lst]
pal = ['#1F77B4']
plt.figure(figsize=(8, 6))
splot=sns.barplot(x='Year', y='Total', data=pd.DataFrame({"Year":x, "Total":y}), palette=pal)
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.1f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
plt.xlabel("Year", size=14)
plt.ylabel("Total Crimes", size=14)
plt.title(park, size=18)
plt.savefig(imgdir + '-'.join(park.lower().replace('.','').split(' ')) + "-total.png")

park = 'VAN CORTLANDT PARK'
lst = parkstotal[park]
x, y = [t[0] for t in lst], [t[1] for t in lst]
pal = ['#1F77B4']
plt.figure(figsize=(8, 6))
splot=sns.barplot(x='Year', y='Total', data=pd.DataFrame({"Year":x, "Total":y}), palette=pal)
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.1f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
plt.xlabel("Year", size=14)
plt.ylabel("Total Crimes", size=14)
plt.title(park, size=18)
plt.savefig(imgdir + '-'.join(park.lower().replace('.','').split(' ')) + "-total.png")

park = 'ST. JAMES PARK'
lst = parkstotal[park]
x, y = [t[0] for t in lst], [t[1] for t in lst]
pal = ['#1F77B4']
plt.figure(figsize=(8, 6))
splot=sns.barplot(x='Year', y='Total', data=pd.DataFrame({"Year":x, "Total":y}), palette=pal)
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.1f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
plt.xlabel("Year", size=14)
plt.ylabel("Total Crimes", size=14)
plt.title(park, size=18)
plt.savefig(imgdir + '-'.join(park.lower().replace('.','').split(' ')) + "-total.png")

park = 'MULLALY PARK'
lst = parkstotal[park]
x, y = [t[0] for t in lst], [t[1] for t in lst]
pal = ['#1F77B4']
plt.figure(figsize=(8, 6))
splot=sns.barplot(x='Year', y='Total', data=pd.DataFrame({"Year":x, "Total":y}), palette=pal)
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.1f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
plt.xlabel("Year", size=14)
plt.ylabel("Total Crimes", size=14)
plt.title(park, size=18)
plt.savefig(imgdir + '-'.join(park.lower().replace('.','').split(' ')) + "-total.png")

park = 'SOUNDVIEW PARK'
lst = parkstotal[park]
x, y = [t[0] for t in lst], [t[1] for t in lst]
pal = ['#1F77B4']
plt.figure(figsize=(8, 6))
splot=sns.barplot(x='Year', y='Total', data=pd.DataFrame({"Year":x, "Total":y}), palette=pal)
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.1f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
plt.xlabel("Year", size=14)
plt.ylabel("Total Crimes", size=14)
plt.title(park, size=18)
plt.savefig(imgdir + '-'.join(park.lower().replace('.','').split(' ')) + "-total.png")

