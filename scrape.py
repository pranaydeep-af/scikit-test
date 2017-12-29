from bs4 import BeautifulSoup
import csv
import urllib.request
f = urllib.request.urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/casts.html")
soup = BeautifulSoup(f)
table = soup.find_all('table')
rows = []
for single_table in table:
       for row in single_table.find_all('tr'):
        rows.append([val.text for val in row.find_all('td')])
with open('aw_cast.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(row for row in rows if row)
