import pandas as pd

acc = pd.read_csv("annualcheeseconsumed.txt", sep=",")

acc

acc = acc.set_index('Year')
acc.head(2)

acc_index_year = pd.read_csv("annualcheeseconsumed.txt", sep=",", index_col=0)

acc_index_year.head()

three_cheese = pd.DataFrame(acc_index_year, columns=['Cheddar', 'Swiss', 'Muenster'])

three_cheese.head()


sorted_by_date = acc.sort_values(["Year"], ascending=False)
sorted_by_date.head(10)

#acc['Cheddar'].sum() / len(acc)
three_cheese['Cheddar'].mean()
three_cheese.mean()

print("hello")

##Part 3
##Reduce the number of columns to just the YEAR and cheddar, swiss, and muenster.
##Part 4
##Sort the data so that the dates go from MOST recent to LEAST recent.
##Part 5
##What is the MEAN of all the cheddar consumed from 1970 to 2017?
