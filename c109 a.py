import random
import statistics
import plotly.figure_factory as ff

dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1 + dice2)
print(sum(dice_result))
print(len(dice_result))

mean=sum(dice_result)/len(dice_result)
print("Mean Of data Is{}".format(mean))
median=statistics.median(dice_result)
print("Median Of Data Is{}".format(median))
mode=statistics.mode(dice_result)
print("Mode of data is{}".format(mode))

fig=ff.create_distplot([dice_result],["result"],show_hist=False)
fig.show()

std_dev=statistics.stdev(dice_result)
print("Standard Deviation is{}".format(std_dev))