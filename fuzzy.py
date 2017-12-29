import sys
import csv  

reload(sys)  
sys.setdefaultencoding('utf8')

import time
from cfuzzyset import cFuzzySet as FuzzySet
import pandas as pd

file1 = 'aw_new.csv'
file2 = 'movies_metadata.csv'

df1=pd.read_csv(file1, error_bad_lines=False) # test file with 964 observations
df2=pd.read_csv(file2, error_bad_lines=False) # test file with 50,000 observations to be matched against

a=FuzzySet() # allocate the FuzzySet object
for row in df1['Title']:
   a.add(str(row)) # Fill the FuzzySet object with all names from file2

start_time = time.time() # Start recording the time

dicto={'index':[],'name':[], 'actual':[]} # Dictionary where I store the output
j=0

for names in df2['title']:
	names = str(names).encode("utf8")
	print names
	print j
	j+=1
	dicto['index'].append(a.get(names)[0][0])
	dicto['name'].append(a.get(names)[0][1])
	dicto['actual'].append(names)

print("--- %s seconds ---" % (time.time() - start_time))

with open('dict.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['score','aw_title','title'])
    for i in range(0,len(dicto['index'])-1):
       writer.writerow([dicto['index'][i], dicto['name'][i], dicto['actual'][i] ])