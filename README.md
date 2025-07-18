# 🧠 AI Data Analyst

An interactive web app for quick data analysis and visualization. Upload your CSV file and get insightful plots and reports — all powered by Streamlit and Plotly.

---

## 📸 Demo

![AI Data Analyst Demo](images/1.png)  
  
![AI Data Analyst Demo](images/2.png)  

![AI Data Analyst Demo](images/3.png)

![AI Data Analyst Demo](images/4.png)

![AI Data Analyst Demo](images/5.png)

![AI Data Analyst Demo](images/6.png)

![AI Data Analyst Demo](images/7.png)

![AI Data Analyst Demo](images/8.png)

![AI Data Analyst Demo](images/9.png)

---

## ✨ Features

- 📂 **CSV Upload** – Drag-and-drop CSV interface
- 🧼 **Data Cleaning** – Handles missing or inconsistent data
- 📊 **Visualizations** – Auto-generated charts:
  - Histograms
  - Pie Charts
  - Box Plots
  - Line Graphs
  - Correlation Heatmaps
  - Scatter Plots
- 📝 **Report Generator** – Export a basic overview of your data

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone <https://github.com/SachinSingh008/ai-data-analyst.git>
cd ai-data-analyst

### 2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the App

streamlit run app.py
🗂️ Project Structure

├── app.py              # Main Streamlit application  

├── visualizer.py       # Plotting functions (Plotly-based)  

├── modules/            # Data loader, cleaner, analyzer, report generator  

├── requirements.txt    # Python package dependencies  

├── README.md  

└── images/             # Screenshots for documentation  

### 📷 Screenshots

Histogram

Pie Chart

Correlation Heatmap

### 🧪 Technologies Used

Python
Streamlit
Plotly
Pandas
NumPy
