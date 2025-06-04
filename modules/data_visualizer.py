import plotly.express as px

def generate_chart(df, chart_type, x, y=None):
    if chart_type == "bar":
        return px.bar(df, x=x, y=y, title=f"Bar Chart: {y} by {x}")
    elif chart_type == "line":
        return px.line(df, x=x, y=y, title=f"Line Chart: {y} over {x}")
    elif chart_type == "scatter":
        return px.scatter(df, x=x, y=y, title=f"Scatter: {x} vs {y}")
    elif chart_type == "histogram":
        return px.histogram(df, x=x, title=f"Histogram of {x}")
    elif chart_type == "pie":
        counts = df[x].value_counts(normalize=True)
        small = counts[counts < 0.02].sum()
        counts = counts[counts >= 0.02]
        if small > 0:
            counts["Others"] = small
        return px.pie(names=counts.index, values=counts.values, title=f"Pie Chart of {x}")
    else:
        return px.bar(df.head(), title="Fallback Chart")
