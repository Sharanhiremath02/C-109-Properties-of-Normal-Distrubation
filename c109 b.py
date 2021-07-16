import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df=pd.read_csv("height-weight.csv")
#fig=ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)
#fig=ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)
data=df["Height(Inches)"].tolist()
mean=sum(data)/len(data)
print("Mean of The data is{}".format(mean))

std_dev=statistics.stdev(data)
print("Standard Deviation is{}".format(std_dev))

first_start,first_end=mean-std_dev,mean+std_dev
second_start,second_end=mean-(2*std_dev),mean+(2*std_dev)
third_start,third_end=mean-(3*std_dev),mean+(3*std_dev)
list_of_data1=[result for result in data if result>first_start and result<first_end]
list_of_data2=[result for result in data if result>second_start and result<second_end]
list_of_data3=[result for result in data if result>third_start and result<third_end]
print(len(list_of_data1)*100/len(data))
print(len(list_of_data2)*100/len(data))
print(len(list_of_data3)*100/len(data))
#print("Len of first Standard Deviation{}".format[])

fig=ff.create_distplot([data],["result"],show_hist=False)
fig.show()
#fig.add_trace(go.Scatter(x=[first_start,std_dev]))




