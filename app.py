import streamlit as st
from modules import data_loader, data_cleaner, data_analyzer, data_visualizer, chart_suggester

st.set_page_config(page_title="AI Data Analyst", layout="wide", initial_sidebar_state="expanded")
st.title("📊 AI Data Analyst App")

if 'user_charts' not in st.session_state:
    st.session_state.user_charts = []

uploaded_file = st.file_uploader("Upload your dataset (CSV, Excel, or JSON)", type=["csv", "xlsx", "json"])

if uploaded_file:
    df = data_loader.load_data(uploaded_file)
    if df is not None:
        df = data_cleaner.clean_data(df)

        st.subheader("📋 Full Data Preview (First 100 Rows)")
        st.dataframe(df.head(100), use_container_width=True)

        st.subheader("📈 Summary Statistics")
        st.dataframe(data_analyzer.get_summary(df), use_container_width=True)

        # Row/column selection
        st.subheader("🎯 Filter Data for Analysis")
        row_option = st.selectbox("Select number of rows to analyze:", ["10", "100", "1000", "10000", "All"], index=2)
        selected_columns = st.multiselect("Select columns to include:", options=df.columns.tolist(), default=df.columns.tolist())
        if selected_columns:
            df = df[selected_columns]
        if row_option != "All":
            df = df.head(int(row_option))

        st.dataframe(df, use_container_width=True)

        # Correlation
        st.subheader("🔗 Correlation Matrix")
        st.plotly_chart(data_analyzer.plot_correlation(df), use_container_width=True)

        # Recommended Charts
        st.subheader("🤖 Recommended Charts")
        suggestions = chart_suggester.suggest_charts(df)
        for i in range(0, len(suggestions), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(suggestions):
                    s = suggestions[i + j]
                    fig = data_visualizer.generate_chart(df, s["type"], s["x"], s.get("y"))
                    cols[j].plotly_chart(fig, use_container_width=True)

        # User-created Charts (only after data is loaded)
        if uploaded_file:
            st.subheader("🎨 Create Your Own Charts")

            user_charts = st.session_state.user_charts
            num_charts = len(user_charts)

            charts_per_row = 3
            total_slots = num_charts + 1  # Extra for add chart button

            for i in range(0, total_slots, charts_per_row):
                cols = st.columns(3)
                for j in range(3):
                    slot_index = i + j
                    if slot_index < num_charts:
                        idx = slot_index
                        chart = user_charts[idx]

                        with cols[j]:
                            # Toggle visibility
                            is_expanded = chart.get("expanded", False)
                            toggle = st.toggle(f"Chart #{idx+1} Settings", value=is_expanded, key=f"toggle_{idx}")
                            st.session_state.user_charts[idx]["expanded"] = toggle

                            if toggle:
                                chart_type = st.selectbox("Chart Type", ["bar", "line", "scatter", "histogram", "pie"], key=f"type_{idx}")
                                x = st.selectbox("X-axis", options=df.columns, index=0, key=f"x_{idx}")
                                y = None
                                if chart_type in ["bar", "line", "scatter"]:
                                    y = st.selectbox("Y-axis", options=df.columns, index=0, key=f"y_{idx}")
                                st.session_state.user_charts[idx].update({
                                    "type": chart_type,
                                    "x": x,
                                    "y": y
                                })

                            chart_type = chart.get("type")
                            x = chart.get("x")
                            y = chart.get("y")
                            if chart_type and x:
                                fig = data_visualizer.generate_chart(df, chart_type, x, y)
                                st.plotly_chart(fig, use_container_width=True)

                            if st.button("🗑 Remove", key=f"remove_{idx}"):
                                st.session_state.user_charts.pop(idx)
                                st.experimental_rerun()

                    elif slot_index == num_charts:
                        with cols[j]:
                            if st.button("➕ Add Chart"):
                                st.session_state.user_charts.append({
                                "type": "bar", "x": df.columns[0], "y": None, "expanded": True
                                })
                                st.rerun()  # <- use this instead of st.experimental_rerun()
