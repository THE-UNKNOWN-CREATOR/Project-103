import plotly.express as px
import pandas as pd

data = pd.read_csv("data.csv")
pic = px.scatter(data, x = "Country", y = "InternetUsers", color = "Percentage", size_max=60)
pic.show()