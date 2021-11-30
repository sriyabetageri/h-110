import plotly.figure_factory as ff
import statistics 
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["id"].tolist()
populationmean = statistics.mean(data)





def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)- 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)

    return mean


def show_fig(mean_list): 
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temp"],show_hist= False)
    fig.add_trace(go.Scatter(x=[mean,mean], y = [0,1],mode ="lines", name = "Mean" ))
    fig.show()


def setup():
    mean_list = []
    for i in range(0,1000):
        setOfMean = randomSetOfMean(100)
        mean_list.append(setOfMean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution",mean)

setup()




population_mean = statistics.mean(data)
print("population_mean",population_mean)


def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        setOfMean = randomSetOfMean(100)
        mean_list.append(setOfMean)

    std_deviation = statistics.stdev(mean_list)
    print("standard deviation of sampling distribution", std_deviation)

standard_deviation()



