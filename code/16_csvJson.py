### Chapter 16 - Working with csv and json

## csv ------------------------------------------------------------------------

# import
import csv
exFile = open('../data/example.csv')
exReader = csv.reader(exFile)
exData = list(exReader)
exData

# accessing values
exData[0][1]

# read via loops
exFile = open('../data/example.csv')
exReader = csv.reader(exFile)
for row in exReader:
    print('row #' + str(exReader.line_num) + ' ' + str(row))

# write objects
outputFile = open('../data/output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['a','b','c'])
outputWriter.writerow(['hello, world!','haha','zz'])
outputWriter.writerow(['1','2.1','3.1'])
outputFile.close()

# DictReader 
exampleFile = open('../data/example.csv')
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name',
'amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])

# DictWriter
import csv
outputFile = open('../data/output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
outputFile.close()


## JSON modules ---------------------------------------------------------------

# reading - loads
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue

# writing - dumps
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
stringOfJsonData