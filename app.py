import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# --- 1. SETUP & CONFIGURATION ---
st.set_page_config(page_title="PhonePe Pulse Dashboard", layout="wide", page_icon="📈")
st.title(" PhonePe Pulse Data Visualization Dashboard")
st.markdown("Explore transaction, user, and insurance data across India.")

# --- 2. DATABASE CONNECTION FUNCTION ---
# Using @st.cache_data so the app doesn't re-query the database for every single click
@st.cache_data
def run_query(query):
    conn = sqlite3.connect('phonepe_pulse.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Fetch initial lists for dropdowns
years = run_query("SELECT DISTINCT Year FROM Aggregated_transaction ORDER BY Year DESC")['Year'].tolist()
states = run_query("SELECT DISTINCT State FROM Aggregated_transaction ORDER BY State")['State'].tolist()

# --- 3. SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filter Data")
selected_year = st.sidebar.selectbox("Select Year", years)
selected_quarter = st.sidebar.slider("Select Quarter", 1, 4, 1)
selected_state = st.sidebar.selectbox("Select State", states)

st.write("---")

# --- 4. BUSINESS USE CASE: PAYMENT PERFORMANCE ---
st.subheader(f"📊 Transaction Performance in {selected_state} (Q{selected_quarter}, {selected_year})")

query_agg_trans = f"""
    SELECT Transaction_type, Transaction_count, Transaction_amount
    FROM Aggregated_transaction
    WHERE State = '{selected_state}' AND Year = '{selected_year}' AND Quarter = {selected_quarter}
"""
df_agg_trans = run_query(query_agg_trans)

if not df_agg_trans.empty:
    col1, col2 = st.columns(2)
    
    with col1:
        # Bar chart for Transaction Value
        fig_bar = px.bar(df_agg_trans, x='Transaction_type', y='Transaction_amount', 
                         color='Transaction_type', title='Total Transaction Value by Category',
                         labels={'Transaction_amount': 'Amount (₹)', 'Transaction_type': 'Category'})
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with col2:
        # Pie chart for Transaction Volume (Count)
        fig_pie = px.pie(df_agg_trans, names='Transaction_type', values='Transaction_count',
                         title='Transaction Volume Share', hole=0.3)
        st.plotly_chart(fig_pie, use_container_width=True)
else:
    st.warning("No transaction data available for this selection.")

st.write("---")

# --- 5. BUSINESS USE CASE: GEOGRAPHICAL INSIGHTS ---
st.subheader(f"📍 Top 10 Districts by Transaction Value in {selected_state}")

query_map_trans = f"""
    SELECT District, SUM(Transaction_amount) as Total_Amount
    FROM Map_map
    WHERE State = '{selected_state}' AND Year = '{selected_year}' AND Quarter = {selected_quarter}
    GROUP BY District
    ORDER BY Total_Amount DESC
    LIMIT 10
"""
df_map_trans = run_query(query_map_trans)

if not df_map_trans.empty:
    fig_districts = px.bar(df_map_trans, x='District', y='Total_Amount', 
                           color='District', title=f'Highest Performing Districts in {selected_state}')
    st.plotly_chart(fig_districts, use_container_width=True)
else:
    st.warning("No district data available for this selection.")

st.write("---")

# --- 6. BUSINESS USE CASE: USER ENGAGEMENT / SEGMENTATION ---
st.subheader(f"📱 User Device Preferences in {selected_state} ({selected_year})")

query_agg_user = f"""
    SELECT Brands, SUM(User_Count) as Total_Users
    FROM Aggregated_user
    WHERE State = '{selected_state}' AND Year = '{selected_year}'
    GROUP BY Brands
    ORDER BY Total_Users DESC
"""
df_agg_user = run_query(query_agg_user)

if not df_agg_user.empty:
    fig_brands = px.pie(df_agg_user, names='Brands', values='Total_Users', 
                        title='Top Smartphone Brands Used by PhonePe Customers')
    st.plotly_chart(fig_brands, use_container_width=True)
else:
    st.info("Brand data is typically only available up to Q1 2022 in the PhonePe dataset.")