import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

pf=pd.read_csv("data2.csv")
score=pf["reading score"].tolist()

mean=sum(score)/len(score)
median = statistics.median(score)
mode = statistics.mode(score)

print(median)
print(mode)
print(mean)

fig = ff.create_distplot([score], ["reading scores"], show_hist=False)
fig.show()

std_deviation=statistics.stdev(score)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
thin_1_std_deviation = [result for result in score if result > first_std_deviation_start and result < first_std_deviation_end]
thin_2_std_deviation = [result for result in score if result > second_std_deviation_start and result < second_std_deviation_end]
thin_3_std_deviation = [result for result in score if result > third_std_deviation_start and result < third_std_deviation_end]

print(thin_1_std_deviation)
print(thin_2_std_deviation)
print(thin_3_std_deviation)
