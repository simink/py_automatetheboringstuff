#! python3
# tabulates population and number of census tracts for each country

import openpyxl, pprint
print('Opening workbook...')

wb = openpyxl.load_workbook('./docs/censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

### fill in data
print('Reading rows...')

for row in range(2, sheet.max_row+1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # make sure key for state exists
    countyData.setdefault(state, {})

    # make sure key for this county exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # each row represents one census tract, increment by one
    countyData[state][county]['tracts'] += 1

    # add pop
    countyData[state][county]['pop'] += int(pop)

### write results to file
print('Writing results...')
resultFile = open('./docs/census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')
