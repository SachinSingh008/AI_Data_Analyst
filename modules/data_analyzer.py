import pandas as pd
import plotly.express as px

def get_summary(df):
    return df.describe(include="all").transpose()

def plot_correlation(df):
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        return px.imshow([[0]], title="No numeric data found.")
    corr = numeric_df.corr()
    fig = px.imshow(corr, text_auto=True, aspect="auto", title="Correlation Heatmap")
    return fig
