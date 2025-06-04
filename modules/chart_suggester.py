def suggest_charts(df):
    suggestions = []
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    categorical_cols = df.select_dtypes(include='object').columns.tolist()

    # Avoid recommending the same column for both x and y
    for i in range(len(numeric_cols)):
        for j in range(len(numeric_cols)):
            if i != j:
                suggestions.append({
                    'type': 'line',
                    'x': numeric_cols[i],
                    'y': numeric_cols[j],
                    'title': f'Line Chart: {numeric_cols[j]} over {numeric_cols[i]}'
                })
                suggestions.append({
                    'type': 'scatter',
                    'x': numeric_cols[i],
                    'y': numeric_cols[j],
                    'title': f'Scatter Chart: {numeric_cols[j]} vs {numeric_cols[i]}'
                })

    for col in numeric_cols:
        suggestions.append({
            'type': 'histogram',
            'x': col,
            'y': None,
            'title': f'Histogram of {col}'
        })

    for col in categorical_cols:
        if len(df[col].unique()) < 10:  # Limit to avoid messy pie charts
            value_counts = df[col].value_counts()
            if not value_counts.empty:
                suggestions.append({
                    'type': 'pie',
                    'x': col,
                    'y': None,
                    'title': f'Pie Chart of {col}'
                })

    # Add a few bar charts if meaningful
    for cat in categorical_cols:
        for num in numeric_cols:
            suggestions.append({
                'type': 'bar',
                'x': cat,
                'y': num,
                'title': f'Bar Chart: {num} by {cat}'
            })

    return suggestions[:6]  # Limit to top 6 recommendations
