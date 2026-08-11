import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the Data
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/CT-towns-income-census-2020.csv"
df = pd.read_csv(url)

# 2. Data Cleaning
# Ensure 'Median household income' is numeric (remove commas and symbols if present)
if df['Median household income'].dtype == 'object':
    df['Median household income'] = df['Median household income'].str.replace('[$,]', '', regex=True).astype(float)

# Drop any rows with missing income or town data to ensure clean visualizations
df = df.dropna(subset=['Median household income', 'Town', 'County'])

st.title("CT Census Data 2020")

# --- Part 1: County Selection ---
st.header("Explore by County")
counties = sorted(df['County'].unique())
selected_county = st.selectbox("Select a County:", counties)

county_df = df[df['County'] == selected_county]
st.dataframe(county_df[['Town', 'County', 'Median household income']], width=800, height=200)


# --- Part 2: Income Range Slider ---
st.header("Filter by Income Range")
min_income = int(df['Median household income'].min())
max_income = int(df['Median household income'].max())

# Create a range slider
income_range = st.slider(
    "Select Median Household Income Range:",
    min_value=min_income,
    max_value=max_income,
    value=(min_income, max_income)
)

# Filter based on slider range
filtered_income_df = df[
    (df['Median household income'] >= income_range[0]) & 
    (df['Median household income'] <= income_range[1])
]
st.dataframe(filtered_income_df[['Town', 'County', 'Median household income']], width=800, height=200)


# --- Part 3: Top 5 and Bottom 5 Bar Graph ---
st.header("Income Extremes: Top 5 & Bottom 5 Towns")

# Sort data and get the extremes
df_sorted = df.sort_values('Median household income', ascending=False)
top_5 = df_sorted.head(5)
bottom_5 = df_sorted.tail(5)

# Combine them for the chart
extremes_df = pd.concat([top_5, bottom_5])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(extremes_df['Town'], extremes_df['Median household income'], color=['#2ecc71']*5 + ['#e74c3c']*5)

# Labels and formatting
ax.set_xlabel("City/Town")
ax.set_ylabel("Median Household Income ($)")
ax.set_title("Highest (Green) and Lowest (Red) Median Incomes in CT")
plt.xticks(rotation=45, ha='right')

st.pyplot(fig)
