# MUST HAVE:
# Read the data from the spreadsheet - done
# Collect all of the sales from each month into a single list - done
# Output the total sales across all months - done

# SHOULD HAVE:
# The gender split of those applying and those hired should be shown to determine whether you are more likely to be hired if you are of a particular gender (Gemma) - done
# Produce education level and skill score of a particular candidate when you input their candidate number (Allegra)
# avg number of company worked at for each candidate (Simi)

# COULD HAVE:
# The percentage of people hired as a result of the interview should be shown - done

# WON'T HAVE:
# The user should be able to input a candidates skill score and see whether they got hired 
# The minimum, maximum and average age someone is recruited at should be shown 
# median education level (most popular level of education attained by candidate)
# most popular recruitment strategy used recruiters
#  A way to filter by types of degree and multiple at the same time e.g. bacherlors and masters, bachelors and phd, or maybe just level of education

# Task 1 - read the data from the spreadsheet
import csv
with open('sales.csv', 'r') as sales_file: # defines to read and from where
    spreadsheet = csv.DictReader(sales_file)
    for row in spreadsheet:
        print(dict(row)) # instructs to print all the data in the dictionary


# Task 2 - Collect all of the sales from each month into a single list
with open('sales.csv', 'r') as sales_file:
  spreadsheet = csv.DictReader(sales_file)
  sales = []
  for row in spreadsheet:
      sale_price = row['sales']
      sales.append(sale_price)
      print(row['month']) # instructs to print the month
      print(row['sales']) # instructs to print the sales for that month


# Task 3 - Output the total sales across all months

# int_sales = int(row['sales']) for s in sales
# sum_sales = sum(row['sales'])
# print(sum_sales)

import csv
total_sum = 0 # used to start the sum at 0 and add further numbers to this
with open('sales.csv', 'r') as sales_file:
    spreadsheet = csv.DictReader(sales_file)
    for row in spreadsheet:
        total_sum += int(row['sales'])
        # print(f"Total Sum: {total_sum}") this if you want to print all the months cumulatively
    print(total_sum)

