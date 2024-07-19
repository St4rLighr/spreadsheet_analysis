# print education level and skillscore for a candidate
# take input for candidate number
# get candidate row from csv
# print education level and SkillScore
import csv
data = [] #make empty list
with open('recruitment_data.csv', 'r') as f:
    spreadsheet = csv.DictReader(f)
    for row in spreadsheet:
        data.append(row)
# print(len(data)) needed to find out how many rows there were
# candidate_number = input(f'Enter a candidate number between 0 and {len(data)}') #wanted to show what I did with len, in case more data was added. I wrote the code, reformatted it into the function and then cut this line


def candidate():
    candidate_number = int(input(f'Enter a candidate number between 0 and {len(data)}'))#wrap everything inside function candidate
    row=data[candidate_number]
    print(f"EducationLevel = {row['EducationLevel']}, SkillScore = {row['SkillScore']}")

candidate() #call the function 
print()



# The gender split of those applying and those hired should be shown to determine whether you are more likely to be hired if you are of a particular gender (Gemma)

# Broken down into
# Show how many males applied
# Show how many females applied
# Show how many candidates got offers
# Show how many females and males got offers

# to calculate the total number of candidates interviewed
import csv
data =[]
with open('recruitment_data.csv', 'r') as recruitment_file: # used to define which file will be read from
    spreadsheet = csv.DictReader(recruitment_file)
    for row in spreadsheet:
        data.append(row) # used to add to the rows to the list
    print('{} is the total number of candidates interviewed'.format(len(data))) # len used to count the number of rows of candidates
    print() #added a line to make the data look a bit neater

# to count the number of females. The 'Gender' data has females as 1 and males as 0
import csv
total_sum_females = 0 # used to start the sum at 0 and add further numbers to this
with open('recruitment_data.csv', 'r') as recruitment_file:
        spreadsheet = csv.DictReader(recruitment_file)
        for row in spreadsheet:
                total_sum_females += int(row['Gender']) #this was used to count the number of "1s" which equates to the number of females
        print('{} is the total number of females interviewed'.format(total_sum_females))

# to use the female number to figure out males that were interviewed from total
def sum(x, y):
    return x - y # used to show the total males is the total number of rows minus any that contain females
result = sum((len(data)), total_sum_females)
print("{} is the total number of males interviewed".format(result))
print()


# to calculate the total number of females interviewed as a percentage
def sum(x, y):
    return (x / y) * 100
result = sum(total_sum_females, len(data))
print("{}% is the total percentage of females interviewed".format(result))

# to calculate the total number of males interviewed as a percentage
def sum(x, y):
    return (x / y) * 100
result = sum((len(data)-total_sum_females), len(data))
print("{}% is the total percentage of males interviewed".format(result))
print() #added a line to make the data look a bit neater

# to calculate the percentage of people hired. Whilst this is a 'could have' requirement, it made sense to add this in here as was looking at similar data anyway.
# if someone is hired, their HiringDecision is 1
total_sum_successful = 0
with open('recruitment_data.csv', 'r') as recruitment_file:
        spreadsheet = csv.DictReader(recruitment_file)
        for row in spreadsheet:
                total_sum_successful += int(row['HiringDecision'])
        print('{} is the total number of candidates successful in getting a job'.format(total_sum_successful))

# to calculate the total number of unsuccessful interviews
def sum(x, y):
    return x - y
result = sum((len(data)), total_sum_successful)
print("{} is the total number of candidates who were not successful in getting a job".format(result))
print() #added a line to make the data look a bit neater

# to calculate the total number of successful interviews as a percentage
def sum(x, y):
    return (x / y) * 100
result = sum(total_sum_successful, len(data))
print("{}% is the total percentage of successful interviews".format(result))

# to calculate the total number of unsuccessful interviews as a percentage
def sum(x, y):
    return (x / y) * 100
result = sum((len(data)-total_sum_successful), len(data))
print("{}% is the total percentage of unsuccessful interviews".format(result))
print() #added a line to make the data look a bit neater

import pandas as pd

import csv
with open('recruitment_data.csv', 'r') as recruitment_file:
    spreadsheet = csv.DictReader(recruitment_file)
    data = []
    for row in spreadsheet:
                data.append({'Gender': row['Gender'], 'HiringDecision': row['HiringDecision']})

df = pd.DataFrame(data)
df['Gender'] = pd.to_numeric(df['Gender'])
df['HiringDecision'] = pd.to_numeric(df['HiringDecision'])
sum_females_offered = ((df['Gender'] == 1) & (df['HiringDecision'] == 1)).sum()
print("The total number of females who received job offers is:", sum_females_offered)

# to calculate the total number of successful female interviews as a percentage
def sum(x, y):
    return (x / y) * 100
result = round(sum(sum_females_offered, total_sum_females))
print("This means that {}% of female candidates were successful at interview".format(result))

# to calculate the total number of unsuccessful female interviews as a percentage
def sum(x, y):
    return (x / y) * 100
result = round(sum((total_sum_females-sum_females_offered), (total_sum_females)))
print("This means that {}% of female candidates were unsuccessful at interview".format(result))
print() #added a line to make the data look a bit neater

#to calculate the number of males who received an offer from interview
import pandas as pd

import csv
with open('recruitment_data.csv', 'r') as recruitment_file:
    spreadsheet = csv.DictReader(recruitment_file)
    data = []
    for row in spreadsheet:
                data.append({'Gender': row['Gender'], 'HiringDecision': row['HiringDecision']})

df = pd.DataFrame(data)
df['Gender'] = pd.to_numeric(df['Gender'])
df['HiringDecision'] = pd.to_numeric(df['HiringDecision'])
sum_males_offered = ((df['Gender'] == 0) & (df['HiringDecision'] == 1)).sum()
print("The total number of males who received job offers is:", sum_males_offered)

# to calculate the total number of successful male interviews as a percentage
def sum(x, y):
    return (x / y) * 100
result = round(sum(sum_males_offered, 762))
print("This means that {}% of male candidates were successful at interview".format(result))

# to calculate the total number of unsuccessful male interviews as a percentage
def sum(x, y):
    return (x / y) * 100
result = round(sum((762-sum_males_offered), (762)))
print("This means that {}% of male candidates were unsuccessful at interview".format(result))
print() #added a line to make the data look a bit neater

print("We can therefore conclude that the proportion of females who received a job off at interview was the same as the proportion of males")
print()

# if were to do more, would learn how to convert CSV data to change Gender to female and male rather than 1 and 0 and utilise if and count functions further




 
# avg number of company worked at for each candidate
# To find how frequently a candidate changes companies
import statistics # Allows us to use the mean function to find the mean previous company of each candidate

import csv
avg = []
with open('recruitment_data.csv', 'r') as recruitment_file:
    spreadsheet = csv.DictReader(recruitment_file)
    for row in spreadsheet:
      previous_company = int(row ['PreviousCompanies']) #for loop converts each individual value to an integer
      avg.append (previous_company) #adds each integer value to the list
      avg_previous = statistics.mean(avg) # Calculates the mean
      rounded_previous_company = round(avg_previous) # Rounds the mean to the nearest whole number
         
      print(rounded_previous_company)  # gives mean of previous companies for all candidates

