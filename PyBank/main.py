import os
import csv

filepath = os.path.join('resources', 'budget_data.csv')

totalMonth = 0
totalAmount = 0
amounts = []
dates = []
change = 0
changes = 0
max = 0
min = 0
maxLast = 0
minLast = 0
maxDate = ""
minDate = ""

with open(filepath) as bankfile :
    csvreader = csv.reader(bankfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
      totalMonth += 1
      totalAmount += int(row[1])
      amounts.append(int(row[1]))
      dates.append(row[0])

    for i in range(1, totalMonth):
      change = (amounts[i] - amounts[i-1])
      if change > max:
         max = change
         maxLast = amounts[i]
      elif change < min:
         min = change
         minLast = amounts[i]
      changes += change

    average = round(changes/(totalMonth - 1), 2)
    
    table = list(zip(dates, amounts))
    for date, amount in table:
      if amount == maxLast:
         maxDate = date
      elif amount == minLast:
         minDate = date

    result = (f"""
          \nFinancail Analysis 
          \n-----------------------------
          \nTotal Months: {totalMonth} 
          \nTotal: {totalAmount} 
          \nAverage Change: ${average} 
          \nGreatest Increase in Profits: {maxDate}(${max}) 
          \nGreatest Decrease in Profits: {minDate}(${min})
          """)
    print(result)

output_path = os.path.join('analysis','results.txt')
with open(output_path, 'w') as textfile :
   textfile.write(result)