import pandas as pd
import numpy as np
from TwoD_Plotting import bar_plots as barplot


df = pd.read_csv('Dataset/BankChurners.csv')

CLIENT_NUM_int = df['CLIENTNUM']
Customer_Age_int = df['Customer_Age']
Total_Trans_Amt_int = df['Total_Trans_Amt']
Attrition_Flag = df['Attrition_Flag']
Dependent_count_int = df['Dependent_count']
Education_Level = df['Education_Level']
Marital_Status = df['Marital_Status']
Income_Category = df['Income_Category']
Card_Category = df['Card_Category']
Months_on_book_int = df['Months_on_book']
Total_Relationship_Count_int = df['Total_Relationship_Count']
Months_Inactive_12_mon_int = df['Months_Inactive_12_mon']
Contacts_Count_12_mon_int = df['Contacts_Count_12_mon']
Credit_Limit_int = df['Credit_Limit']
Total_Revolving_Bal_int = df['Total_Revolving_Bal']
Total_Trans_Ct_int = df['Total_Trans_Ct']
Avg_Open_To_Buy_int = df['Avg_Open_To_Buy']
Total_Amt_Chng_Q4_Q1_float = df['Total_Amt_Chng_Q4_Q1']
Total_Trans_Amt_int = df['Total_Trans_Amt']
Total_Ct_Chng_Q4_Q1_float = df['Total_Ct_Chng_Q4_Q1']
Avg_Utilization_Ratio_float = df['Avg_Utilization_Ratio']
Gender = df['Gender']

y = Total_Trans_Ct_int/10
x = np.arange(len(Customer_Age_int))
simple_bar = barplot.SimpleBarChart('Customer_Age', 'Credit_Limit', 'Credit Limit Statistics')
simple_bar.bar(x, y, Dependent_count_int)
simple_bar.showbar()

#simpleplot = barplot.SimplePlotting('Customer_Age', 'Credit_Limit', 'Credit Limit and Customer Age bar')
#simpleplot.plots(Customer_Age_int, Total_Trans_Ct_int, Dependent_count_int)

#
# one = sum(Customer_Age_int)/5
# two = sum(Dependent_count_int)
# three = sum(Months_on_book_int)/5
# four = sum(Total_Relationship_Count_int)
# five = sum(Months_Inactive_12_mon_int)
# six = sum(Total_Trans_Ct_int)
# pieslice = [one, two, three, four, five, six]
# pielabels = ['Customer_Age', 'Dependent_count', 'Months_on_book', 'Total_Relationship_Count',
#              'Months_Inactive_12_mon', 'Total_Trans_Ct']
# explode = [0.1, 0, 0, 0, 0, 0]
# simplepiechart = barplot.SimplePieChart('Pie Chart View')
# simplepiechart.piecharts(pieslice, pielabels, explode)

#
# stock_pie_labels = ['Dependent count', 'Months on book', 'Total Relationship Count', 'Months Inactive 12_mon',
#                     'Total Trans Ct']
# simplestackplot = barplot.SimplePieChart('Stack Plot View')
# simplestackplot.stackplotting(Customer_Age_int, Dependent_count_int, Months_on_book_int,
#                               Total_Relationship_Count_int, Months_Inactive_12_mon_int, Total_Trans_Ct_int, stock_pie_labels)
