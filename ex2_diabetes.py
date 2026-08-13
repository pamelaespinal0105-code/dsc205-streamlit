import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the Diabetes Dataset
# Using a reliable raw URL for the Pima Indians Diabetes dataset
data_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
df = pd.read_csv(data_url, names=column_names)

# 2. Sidebar Setup
st.sidebar.header("Dashboard Filters")
st.sidebar.markdown("Filter the data to see differences between patient groups.")

# Radio button to select Outcome (0 = Non-Diabetic, 1 = Diabetic)
outcome_choice = st.sidebar.radio(
    "Select Patient Status:",
    options=[0, 1],
    format_func=lambda x: "Diabetic" if x == 1 else "Non-Diabetic"
)

# 3. Filter Data based on Selection
filtered_df = df[df['Outcome'] == outcome_choice]

# 4. Main Page Content
st.title("Diabetes Dataset Analysis")
st.markdown(f"Currently viewing data for: **{'Diabetic' if outcome_choice == 1 else 'Non-Diabetic'}** patients.")

# Display metrics
col1, col2 = st.columns(2)
col1.metric("Patient Count", len(filtered_df))
col2.metric("Avg Glucose", round(filtered_df['Glucose'].mean(), 2))

# 5. Visualization
st.subheader(f"Glucose Distribution for {'Diabetics' if outcome_choice == 1 else 'Non-Diabetics'}")

fig, ax = plt.subplots()
ax.hist(filtered_df['Glucose'], bins=15, color='seagreen', edgecolor='white')
ax.set_xlabel("Glucose Level")
ax.set_ylabel("Number of Patients")
st.pyplot(fig)

# 6. Optional raw data display
if st.checkbox("Show raw data"):
    st.subheader("Raw Data (Filtered)")
    st.dataframe(filtered_df)
