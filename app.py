import os
import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="RFM Customer Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================

# FIX #6: path relatif biasa ("rfm_analysis.xlsx") tergantung folder
# tempat "streamlit run" dijalankan (current working directory), BUKAN
# folder tempat app.py berada — ini sering bikin FileNotFoundError kalau
# Streamlit dijalankan dari folder lain. Diganti supaya selalu mencari
# di folder yang sama dengan app.py sendiri.
APP_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(APP_DIR, "rfm_analysis.xlsx")

@st.cache_data
def load_data(path: str):
    # FIX #2: file aslinya .xlsx, bukan .csv
    return pd.read_excel(path, engine="openpyxl")

if not os.path.exists(DATA_PATH):
    st.error(
        f"File tidak ditemukan: `{DATA_PATH}`\n\n"
        "Pastikan **rfm_analysis.xlsx** ada di folder yang sama dengan **app.py** ini."
    )
    st.stop()

df = load_data(DATA_PATH)

# ==================================================
# SIDEBAR FILTER
# ==================================================

st.sidebar.header("Filters")

segment_filter = st.sidebar.multiselect(
    "Select Segment",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

filtered_df = df[
    df["Segment"].isin(segment_filter)
]

# FIX #1: tanpa guard ini, kalau semua segmen di-uncheck app langsung
# crash (ValueError: attempt to get argmax of an empty sequence) di
# largest_segment / best_segment / top_segment di bawah.
if filtered_df.empty:
    st.warning("Pilih minimal satu segmen di sidebar untuk melihat data.")
    st.stop()

# ==================================================
# HEADER
# ==================================================

st.title("📊 RFM Customer Segmentation Dashboard")
st.markdown("Customer Analytics & Business Intelligence")

# ==================================================
# KPI CALCULATION
# ==================================================

total_customer = filtered_df["customer_unique_id"].nunique()

total_revenue = filtered_df["Monetary"].sum()

avg_recency = filtered_df["Recency"].mean()

avg_frequency = filtered_df["Frequency"].mean()

avg_monetary = filtered_df["Monetary"].mean()

segment_count = filtered_df["Segment"].nunique()

largest_segment = (
    filtered_df["Segment"]
    .value_counts()
    .idxmax()
)

best_segment = (
    filtered_df.groupby("Segment")["Monetary"]
    .sum()
    .idxmax()
)

# ==================================================
# KPI ROW 1
# ==================================================

# FIX #7: row 1 pakai 5 kolom, row 2 pakai 3 kolom — batas kolomnya
# nggak sejajar (lihat "Largest Segment" nggak pas di bawah kolom apa
# pun di row 1, dan ada area kosong besar di kanan). Disamakan jadi
# 4+4 supaya kedua baris membentuk satu grid yang rapi.

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Customers",
    f"{total_customer:,}"
)

col2.metric(
    "Revenue",
    # FIX #5: data Olist dalam Real Brasil, bukan USD
    f"R$ {total_revenue:,.0f}"
)

col3.metric(
    "Avg Monetary",
    f"R$ {avg_monetary:,.0f}"
)

col4.metric(
    "Segment Count",
    segment_count
)

# ==================================================
# KPI ROW 2
# ==================================================

col5,col6,col7,col8 = st.columns(4)

col5.metric(
    "Avg Recency",
    f"{avg_recency:.1f} days"
)

col6.metric(
    "Avg Frequency",
    f"{avg_frequency:.2f}"
)

col7.metric(
    "Largest Segment",
    largest_segment
)

col8.metric(
    "Best Segment",
    best_segment
)

# ==================================================
# SEGMENT SUMMARY
# ==================================================

segment_summary = (
    filtered_df
    .groupby("Segment")
    .agg(
        Customers=("customer_unique_id","count"),
        Revenue=("Monetary","sum"),
        Avg_Monetary=("Monetary","mean"),
        Avg_Frequency=("Frequency","mean"),
        Avg_Recency=("Recency","mean")
    )
    .reset_index()
)

# ==================================================
# CHART 1
# ==================================================

fig1 = px.bar(
    segment_summary,
    x="Customers",
    y="Segment",
    orientation="h",
    title="Customer Distribution by Segment"
)

# ==================================================
# CHART 2
# ==================================================

fig2 = px.pie(
    segment_summary,
    values="Revenue",
    names="Segment",
    hole=0.5,
    title="Revenue Contribution by Segment"
)

left,right = st.columns(2)

left.plotly_chart(
    fig1,
    use_container_width=True
)

right.plotly_chart(
    fig2,
    use_container_width=True
)

# ==================================================
# CHART 3
# ==================================================

fig3 = px.bar(
    segment_summary,
    x="Segment",
    y="Avg_Monetary",
    title="Average Monetary by Segment"
)

# ==================================================
# CHART 4
# ==================================================

fig4 = px.bar(
    segment_summary,
    x="Segment",
    y="Avg_Frequency",
    title="Average Frequency by Segment"
)

left,right = st.columns(2)

left.plotly_chart(
    fig3,
    use_container_width=True
)

right.plotly_chart(
    fig4,
    use_container_width=True
)

# ==================================================
# CHART 5
# ==================================================

fig5 = px.bar(
    segment_summary,
    x="Segment",
    y="Avg_Recency",
    title="Average Recency by Segment"
)

# ==================================================
# CHART 6
# ==================================================

# FIX #3: RFM_Score_Group adalah KODE gabungan R+F+M (111-555, 125 nilai
# unik) — bukan skala numerik berurutan, jadi histogram langsung di
# field ini nggak bermakna (215 bukan "lebih baik" dari 151). Diganti
# jadi distribusi R_Score / F_Score / M_Score masing-masing (1-5, asli
# ordinal) dalam satu grouped histogram.
score_melt = filtered_df.melt(
    value_vars=["R_Score", "F_Score", "M_Score"],
    var_name="Score Type",
    value_name="Score"
)

fig6 = px.histogram(
    score_melt,
    x="Score",
    color="Score Type",
    barmode="group",
    nbins=5,
    title="R / F / M Score Distribution (1-5)"
)

left,right = st.columns(2)

left.plotly_chart(
    fig5,
    use_container_width=True
)

right.plotly_chart(
    fig6,
    use_container_width=True
)

# ==================================================
# CHART 7
# ==================================================

# FIX #4: scatter asli plot 95,420 titik individual customer (berat di
# browser) + ukuran bubble dari Frequency yang nyaris seragam (mayoritas
# customer cuma belanja 1x). Diagregasi ke level segmen: 1 titik = 1
# segmen, ukuran = jumlah customer — lebih ringan & lebih mudah dibaca.
fig7 = px.scatter(
    segment_summary,
    x="Avg_Recency",
    y="Avg_Monetary",
    size="Customers",
    color="Segment",
    text="Segment",
    title="Recency vs Monetary by Segment"
)

fig7.update_traces(textposition="top center")

st.plotly_chart(
    fig7,
    use_container_width=True
)

# ==================================================
# SEGMENT TABLE
# ==================================================

st.subheader("Segment Summary")

st.dataframe(
    segment_summary,
    use_container_width=True
)

# ==================================================
# INSIGHT
# ==================================================

top_segment = (
    segment_summary
    .sort_values(
        "Revenue",
        ascending=False
    )
    .iloc[0]
)

st.success(
    f"""
    Top Revenue Segment: {top_segment['Segment']}

    Revenue Contribution:
    R$ {top_segment['Revenue']:,.0f}
    """
)

# ==================================================
# DOWNLOAD BUTTON
# ==================================================

csv = segment_summary.to_csv(index=False)

st.download_button(
    label="📥 Download Segment Summary",
    data=csv,
    file_name="segment_summary.csv",
    mime="text/csv"
)