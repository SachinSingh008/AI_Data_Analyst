import streamlit as st
import pandas as pd
import io
from modules import data_cleaner, analyzer, visualizer, report_generator

# Set Streamlit to wide mode
st.set_page_config(
    page_title="AI Data Analyst",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Optional custom styling
def set_custom_styles():
    st.markdown("""
        <style>
        .main {
            max-width: 95%;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

set_custom_styles()

# App title and file uploader
st.title("AI Data Analyst")
uploaded_file = st.file_uploader("Upload your Excel or CSV file", type=["csv", "xlsx", "xls"])

if uploaded_file:
    # Load file based on extension
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(uploaded_file)
        # Convert Excel to CSV buffer (optional, for compatibility)
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)
        uploaded_file = csv_buffer
    else:
        st.error("Unsupported file type!")
        st.stop()

    # Clean data
    df = data_cleaner.clean_data(df)

    st.subheader("Data Preview")
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    categorical_cols = df.select_dtypes(include='object').columns.tolist()

    st.subheader("Visualizations")

    # Histogram
    with st.expander("Histograms"):
        cols = st.columns(3)
        for i, col in enumerate(numeric_cols):
            fig = visualizer.plot_histogram(df, col)
            cols[i % 3].plotly_chart(fig, use_container_width=True)

    # Pie Chart
    with st.expander("Pie Charts"):
        cols = st.columns(3)
        for i, col in enumerate(categorical_cols):
            fig = visualizer.plot_pie_chart(df, col)
            cols[i % 3].plotly_chart(fig, use_container_width=True)

    # Box Plot
    with st.expander("Box Plots"):
        cols = st.columns(3)
        plot_index = 0
        for num_col in numeric_cols:
            for cat_col in categorical_cols:
                fig = visualizer.plot_box_plot(df, cat_col, num_col)
                cols[plot_index % 3].plotly_chart(fig, use_container_width=True)
                plot_index += 1

    # Line Graph
    with st.expander("Line Graphs"):
        if len(numeric_cols) >= 2:
            x_col = numeric_cols[0]
            cols = st.columns(3)
            for i, y_col in enumerate(numeric_cols[1:]):
                fig = visualizer.plot_line_graph(df, x_col, y_col)
                cols[i % 3].plotly_chart(fig, use_container_width=True)

    # Heatmap
    with st.expander("Correlation Heatmap"):
        if len(numeric_cols) >= 2:
            fig = visualizer.plot_heatmap(df)
            st.plotly_chart(fig, use_container_width=True)

    # Scatter Plot
    with st.expander("Scatter Plots"):
        if len(numeric_cols) >= 2:
            cols = st.columns(3)
            plot_index = 0
            for i in range(len(numeric_cols)):
                for j in range(i + 1, len(numeric_cols)):
                    fig = visualizer.plot_scatter_plot(df, numeric_cols[i], numeric_cols[j])
                    cols[plot_index % 3].plotly_chart(fig, use_container_width=True)
                    plot_index += 1

    # Report Generation Button
    if st.button("Generate Report"):
        context = {
            "columns": list(df.columns),
            "rows": df.head(10).to_dict(orient='records')
        }
        report_generator.generate_report(context)
        st.success("Report generated!")
