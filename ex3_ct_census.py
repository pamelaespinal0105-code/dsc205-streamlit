import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the Data
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/CT-towns-income-census-2020.csv"
df = pd.read_csv(url)

# 2. Data Cleaning
df['Per capita income'] = df['Per capita income'].str.replace(
    '$', '').str.replace(',', '').astype(int)

df['Median household income'] = df['Median household income'].str.replace(
    '$', '').str.replace(',', '').astype(int)

df['Median family income'] = df['Median family income'].str.replace(
    '$', '').str.replace(',', '').astype(int)

st.title("CT Census Data 2020")

# Part 1: County Selection
st.header("Explore by County")

counties = sorted(df['County'].unique())
selected_county = st.selectbox("Select a County:", counties)

county_df = df[df['County'] == selected_county]

st.dataframe(
    county_df[['Place', 'County', 'Median household income']],
    width=800,
    height=200
)

# Part 2: Income Range Slider
st.header("Filter by Income Range")

min_income = int(df['Median household income'].min())
max_income = int(df['Median household income'].max())

income_range = st.slider(
    "Select Median Household Income Range:",
    min_value=min_income,
    max_value=max_income,
    value=(min_income, max_income)
)

filtered_income_df = df[
    (df['Median household income'] >= income_range[0]) &
    (df['Median household income'] <= income_range[1])
]

st.dataframe(
    filtered_income_df[['Place', 'County', 'Median household income']],
    width=800,
    height=200
)

# Part 3: Top 5 and Bottom 5 Bar Graph
st.header("Highest and Lowest Median Household Income")

df_sorted = df.sort_values('Median household income')

bottom_5 = df_sorted.head(5)
top_5 = df_sorted.tail(5)

extremes_df = pd.concat([bottom_5, top_5])

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(
    extremes_df['Place'],
    extremes_df['Median household income']
)

ax.set_xlabel("City/Town")
ax.set_ylabel("Median Household Income ($)")
ax.set_title("5 Highest and 5 Lowest Median Household Incomes")

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig)
