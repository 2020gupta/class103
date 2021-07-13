import pandas as pd
import plotly.express as px

df=pd.read_csv("data1.csv")
graph=px.scatter(df,x="Population",y="Per capita",color="Country",title="Scatter Graph",size="Percentage")
graph.show()