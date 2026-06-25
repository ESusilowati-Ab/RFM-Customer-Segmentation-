# 📊 RFM Customer Segmentation Dashboard

Customer segmentation project using RFM (Recency, Frequency, Monetary) analysis on the Brazilian E-Commerce (Olist) dataset to identify customer behavior patterns, high-value customers, and retention opportunities.

---

## 🎯 Business Problem

Understanding customer purchasing behavior is essential for improving retention and increasing customer lifetime value (CLV).

This project aims to:

- Identify high-value customers
- Detect customers at risk of churn
- Analyze purchasing behavior
- Provide actionable business recommendations
- Build an interactive dashboard for business stakeholders

---

## 📂 Dataset

Dataset: Brazilian E-Commerce Public Dataset by Olist

The dataset contains:

- Customer Information
- Orders
- Products
- Payments
- Sellers
- Delivery Information

After data preparation and feature engineering, the final RFM dataset contains:

- 95,420 unique customers
- Recency
- Frequency
- Monetary
- RFM Scores
- Customer Segments

---

## 🛠 Tools & Technologies

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Jupyter Notebook
- Git & GitHub

---

## 📈 Project Workflow

### 1. Data Cleaning

- Handle missing values
- Validate data types
- Remove inconsistencies
- Merge multiple datasets

### 2. Exploratory Data Analysis (EDA)

- Customer behavior analysis
- Revenue analysis
- Product category analysis
- Correlation analysis

### 3. RFM Analysis

Calculate:

- Recency
- Frequency
- Monetary

Generate:

- R Score
- F Score
- M Score
- RFM Score

### 4. Customer Segmentation

Customers are classified into segments such as:

- Champions
- Loyal Customers
- Potential Loyalists
- Customers Needing Attention
- At Risk
- Lost Customers

### 5. Dashboard Development

Interactive dashboard built with Streamlit.

---

## 📊 Dashboard Features

### KPI Cards

- Total Customers
- Total Revenue
- Average Recency
- Average Frequency
- Average Monetary
- Segment Count
- Largest Segment
- Best Segment

### Visualizations

1. Customer Distribution by Segment
2. Revenue Contribution by Segment
3. Average Monetary by Segment
4. Average Frequency by Segment
5. Average Recency by Segment
6. RFM Score Distribution
7. Recency vs Monetary Scatter Plot

---

## 🔍 Key Business Insights

### 1. Customer Retention Challenge

Approximately 96.95% of customers made only one purchase.

This indicates that customer acquisition is strong, but customer retention remains a major challenge.

### 2. Champions Drive Revenue

The Champions segment contributes significantly to overall revenue and should be prioritized through loyalty programs.

### 3. Re-engagement Opportunity

Customers Needing Attention represent a valuable group that can be targeted through win-back campaigns before they become inactive.

### 4. Growth Opportunity

Increasing repeat purchases presents the largest opportunity for revenue growth without significantly increasing acquisition costs.

---

## 💡 Business Recommendations

- Launch loyalty programs for Champions
- Create personalized marketing campaigns
- Implement second-purchase incentives
- Develop win-back campaigns for inactive customers
- Improve customer retention strategy

---

## 📷 Dashboard Preview

![Dashboard Preview](dashboard olist.png)

---

## 🚀 Live Dashboard

Streamlit App:

[View Dashboard](https://olistsegmentation.streamlit.app/))

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ESusilowati-Ab/RFM-Customer-Segmentation.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
RFM-Customer-Segmentation/
│
├── app.py
├── requirements.txt
├── README.md
├── rfm_analysis.csv
├── Data_Cleaning.ipynb
├── EDA_VISUALISASI_RFM.ipynb
├── dashboard_screenshot.png
└── assets/
```

---

## 👤 Author

Erna Susilowati

Aspiring Data Analyst | Python | SQL | Power BI | Streamlit
You can access the interactive Streamlit dashboard here: [Olist Customer Segmentation Dashboard](https://olistsegmentation.streamlit.app/)
