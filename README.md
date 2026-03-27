# 📈 PhonePe Transaction Insights

**Live Dashboard:** [View the Streamlit App Here](https://phonepe-transaction-insights-ms7sqpb5neh8gpfdjqrz8u.streamlit.app/)

## 📝 Project Overview
The "PhonePe Transaction Insights" project is an end-to-end data engineering and analytics pipeline. It extracts massive volumes of transactional, user, and insurance data from the official PhonePe Pulse repository, transforms it into a structured relational database, and visualizes the findings through an interactive web dashboard. 

This project aims to uncover hidden geographical trends, device usage patterns, and market expansion opportunities within the Indian digital payments ecosystem.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, JSON
* **Database:** SQLite3
* **Visualization:** Plotly Express, Seaborn, Matplotlib
* **Dashboard & Deployment:** Streamlit, Streamlit Community Cloud

## 🚀 Features
* **Interactive Filtering:** Filter data dynamically by Year, Quarter, and State.
* **Transaction Analysis:** Visualizes performance across different payment categories (P2P, Merchant, etc.).
* **Geographical Mapping:** Identifies top-performing and underperforming districts.
* **Device Ecosystem:** Analyzes the dominant smartphone brands used by the customer base.

## 📂 Dataset
Due to the large size of the raw data, it is not included in this repository. The data is dynamically extracted from the official PhonePe Pulse dataset.

**Source:** [PhonePe Pulse GitHub Repository](https://github.com/PhonePe/pulse)

## 💻 How to run locally:
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/SourabhKhamankar22/PhonePe-Transaction-Insights.git

2. Clone the official PhonePe Pulse repository into a folder named pulse-master inside this project directory.

3. Run the ETL (Extract, Transform, Load) script to parse the JSON files and generate the local SQLite database. 
    ```
    data_extraction.py
    ```
4. Launch the Streamlit app:
    ```
    streamlit run app.py
    ```