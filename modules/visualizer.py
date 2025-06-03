import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

# Styling constants
PLOT_TEMPLATE = "plotly_dark"  # Options: "plotly_white", "seaborn", "plotly_dark", etc.
COLOR_SEQUENCE = px.colors.qualitative.Set3  # Color palette

def get_categorical_column(df):
    cat_cols = df.select_dtypes(include='object').columns
    return cat_cols[0] if len(cat_cols) > 0 else None

# 1. Histogram
def plot_histogram(df, column, bin_size=None):
    color_col = get_categorical_column(df)
    fig = px.histogram(
        df,
        x=column,
        color=color_col,
        nbins=bin_size,
        text_auto=True,
        title=f'Distribution of {column}',
        labels={column: column.capitalize()},
        template=PLOT_TEMPLATE,
        color_discrete_sequence=COLOR_SEQUENCE
    )
    fig.update_layout(
        xaxis_title=column.capitalize(),
        yaxis_title='Frequency',
        bargap=0.1
    )
    return fig

# 2. Pie Chart
def plot_pie_chart(df, column):
    fig = px.pie(
        df,
        names=column,
        title=f'Pie Chart of {column}',
        hole=0.4,
        template=PLOT_TEMPLATE,
        color_discrete_sequence=COLOR_SEQUENCE
    )
    return fig

# 3. Box Plot
def plot_box_plot(df, x_column, y_column):
    fig = px.box(
        df,
        x=x_column,
        y=y_column,
        color=x_column,
        title=f'Box Plot of {y_column} by {x_column}',
        points="all",
        template=PLOT_TEMPLATE,
        color_discrete_sequence=COLOR_SEQUENCE
    )
    return fig

# 4. Line Graph
def plot_line_graph(df, x_column, y_column):
    color_col = get_categorical_column(df)
    fig = px.line(
        df,
        x=y_column,
        y=x_column,
        color=color_col,
        title=f'Line Graph of {y_column} over {x_column}',
        markers=True,
        template=PLOT_TEMPLATE,
        color_discrete_sequence=COLOR_SEQUENCE
    )
    return fig

# 5. Heatmap (Correlation)
def plot_heatmap(df):
    corr = df.corr(numeric_only=True)
    z = np.round(corr.values, 2)
    fig = ff.create_annotated_heatmap(
        z,
        x=list(corr.columns),
        y=list(corr.index),
        colorscale='Viridis',
        showscale=True
    )
    fig.update_layout(
        title='Correlation Heatmap',
        template=PLOT_TEMPLATE
    )
    return fig

# 6. Scatter Plot
def plot_scatter_plot(df, x_column, y_column):
    color_col = get_categorical_column(df)
    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        color=color_col,
        title=f'Scatter Plot of {y_column} vs {x_column}',
        trendline="ols",
        template=PLOT_TEMPLATE,
        color_discrete_sequence=COLOR_SEQUENCE
    )
    return fig
