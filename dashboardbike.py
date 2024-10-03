import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the page title
st.title("Bicycle Usage Dashboard")

# Load your dataset (adjust the file path or source as needed)
# df = pd.read_csv('your_data_file.csv') 

data = {
    'Day Type': ['Weekday', 'Weekday', 'Weekend', 'Weekend'],
    'Year': [2011, 2012, 2011, 2012],
    'Usage': [1092, 2191, 10, 21]
}
df = pd.DataFrame(data)

# Display data
st.write("## Data Preview")
st.dataframe(df)

# Separate data for visualizations
weekdays = df[df['Day Type'] == 'Weekday']
weekends = df[df['Day Type'] == 'Weekend']

# Plot Bicycle Usage: Weekdays vs Weekends
st.write("## Bicycle Usage: Weekdays vs Weekends")
fig, ax = plt.subplots()
ax.plot(weekdays['Year'], weekdays['Usage'], label='Weekdays', marker='o')
ax.plot(weekends['Year'], weekends['Usage'], label='Weekends', marker='o')
ax.set_xlabel('Year')
ax.set_ylabel('Usage')
ax.set_title('Bicycle Usage Trends: Weekdays vs Weekends')
ax.legend()
st.pyplot(fig)

# Plot Total Bicycle Users Each Year
st.write("## Total Bicycle Users Each Year")
total_users_by_year = df.groupby('Year')['Usage'].sum().reset_index()

fig2, ax2 = plt.subplots()
ax2.bar(total_users_by_year['Year'], total_users_by_year['Usage'], color='skyblue')
ax2.set_xlabel('Year')
ax2.set_ylabel('Total Users')
ax2.set_title('Total Bicycle Users Each Year')
st.pyplot(fig2)