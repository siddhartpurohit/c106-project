import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            marks_in_percentage.append(float(i["Marks In Percentage"]))
            days_present.append(float(i["Days Present"]))

    return {"x" : marks_in_percentage, "y": days_present}

def findCorrelation(datasource):
    c = np.corrcoef(datasource["x"], datasource["y"])
    print("correclation is : ",c[0,1])

def setup():
    data_path  = "studentmarks.csv"



    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()