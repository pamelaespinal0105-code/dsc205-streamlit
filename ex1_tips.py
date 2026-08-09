import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
tips_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(tips_url)

# 2. Title and Description
st.title('Restaurant Tips')
st.markdown("""
This report explores a dataset containing information about restaurant bills, 
including the total amount paid, the tip given, and details about the diners.
""")

# 3. Data Section
st.subheader('The data')
st.dataframe(df, width=700, height=250)

# 4. Row count and Summary Statistics
st.write(f"The dataset contains {len(df)} rows.")
st.write(df[['total_bill', 'tip']].describe())

# 5. Histogram of Total Bill
st.subheader('Distribution of the total bill')
fig, ax = plt.subplots()
ax.hist(df['total_bill'], bins=20, color='skyblue', edgecolor='black')
ax.set_xlabel('Total Bill ($)')
ax.set_ylabel('Frequency')
st.pyplot(fig, clear_figure=True)

# 6. Scatter Plot: Total Bill vs Tip
st.subheader('Relationship: Total Bill vs Tip')
fig2, ax2 = plt.subplots()
ax2.scatter(df['total_bill'], df['tip'], s=12, color='coral')
ax2.set_xlabel('Total Bill ($)')
ax2.set_ylabel('Tip ($)')
st.pyplot(fig2, clear_figure=True)
