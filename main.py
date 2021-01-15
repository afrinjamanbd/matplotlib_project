import pandas as pd
import numpy as np
from TwoDimensional_Plotting import BarPlot as Bar
from TwoDimensional_Plotting import Plotting as Plot
from TwoDimensional_Plotting import PieChart as Pie
from TwoDimensional_Plotting import StackPlot as Stack
from TwoDimensional_Plotting import SubPlot as SubPlot
from TwoDimensional_Plotting import Histogram as Hist
from TwoDimensional_Plotting import ScatterPlot as Scatter_plt



df = pd.read_csv('Dataset/BankChurners.csv')

# Sets Column names into variables
Gender = df['Gender']
CLIENT_NUM_int = df['CLIENT_NUM']
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
Total_Trans_Amt_int_ = df['Total_Trans_Amt']
Total_Ct_Chng_Q4_Q1_float = df['Total_Ct_Chng_Q4_Q1']
Avg_Utilization_Ratio_float = df['Avg_Utilization_Ratio']

#
# x = np.arange(len(Customer_Age_int))
# y = Total_Trans_Ct_int/10
# simple_bar = Bar.BarChart(x, y, '#32E300', 'Credit Limit Statistics')
# simple_bar.add()
# simple_bar.set_title('boom')
# simple_bar.xy_title("x title", 'y title')
# simple_bar.color = '#FF3A2D'
# simple_bar.add_new(x, Dependent_count_int, 0, 'y and z')
# simple_bar.show()

#
# plot = Plot.Plotting(Customer_Age_int.sort_values(), Total_Trans_Ct_int.sort_values(), '#FF3A2D',
#                      'Credit Limit and Customer Age bar')
# plot.add()
# plot.color = '#32E300'
# plot.add_new(Customer_Age_int.sort_values(), Dependent_count_int.sort_values(), 0, 'Customer age and Dependent count')
# # plot.show()

#
# one = sum(Customer_Age_int)/5
# two = sum(Dependent_count_int)
# three = sum(Months_on_book_int)/5
# four = sum(Total_Relationship_Count_int)
# five = sum(Months_Inactive_12_mon_int)
# six = sum(Total_Trans_Ct_int)
# explode = [0.1, 0, 0, 0, 0, 0]
# Pie.explode = explode
# pie_slice = [one, two, three, four, five, six]
# pie_labels = ['Customer_Age', 'Dependent_count', 'Months_on_book', 'Total_Relationship_Count',
#               'Months_Inactive_12_mon', 'Total_Trans_Ct']
# pie_chart = Pie.PieChart(pie_slice, pie_labels)
# pie_chart.add()
# pie_chart.show()


# stock_pie_labels = ['Dependent count', 'Months book', 'Total Relation Count', 'Months Inactive 12_mon',
#                     'Total Trans Ct']
# arr = [Customer_Age_int, Dependent_count_int, Months_on_book_int, Total_Relationship_Count_int,
#        Months_Inactive_12_mon_int, Total_Trans_Ct_int]
# stack_plot = Stack.StackPlot(arr, stock_pie_labels)
# stack_plot.add()
# stack_plot.show()

# histogram = Hist.Histogram(Total_Trans_Ct_int, 5, True)
# histogram.add()
# histogram.add_new(Months_on_book_int,10,False)
# histogram.show()

# scatter_plot = Scatter_plt.ScatterPlot(Customer_Age_int, Dependent_count_int, False)
# scatter_plot.add()
# scatter_plot.show()