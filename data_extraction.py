import os
import json
import pandas as pd
import sqlite3

# Define the base path to the unzipped data folder
base_path = "D:/GITHUB projects/PhonePe/pulse-master/data/"

# ==========================================
# 1. AGGREGATED DATA EXTRACTION FUNCTIONS
# ==========================================
def extract_agg_trans():
    path = base_path + "aggregated/transaction/country/india/state/"
    columns = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []}
    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if os.path.isdir(state_path):
            for year in os.listdir(state_path):
                year_path = os.path.join(state_path, year)
                if os.path.isdir(year_path):
                    for file in os.listdir(year_path):
                        with open(os.path.join(year_path, file), 'r') as f:
                            data = json.load(f)
                            try:
                                for i in data['data']['transactionData']:
                                    columns['Transaction_type'].append(i['name'])
                                    columns['Transaction_count'].append(i['paymentInstruments'][0]['count'])
                                    columns['Transaction_amount'].append(i['paymentInstruments'][0]['amount'])
                                    columns['State'].append(state)
                                    columns['Year'].append(year)
                                    columns['Quarter'].append(int(file.strip('.json')))
                            except: pass
    df = pd.DataFrame(columns)
    df['State'] = df['State'].str.replace('-', ' ').str.title()
    return df

def extract_agg_user():
    path = base_path + "aggregated/user/country/india/state/"
    columns = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'User_Count': [], 'Percentage': []}
    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if os.path.isdir(state_path):
            for year in os.listdir(state_path):
                year_path = os.path.join(state_path, year)
                if os.path.isdir(year_path):
                    for file in os.listdir(year_path):
                        with open(os.path.join(year_path, file), 'r') as f:
                            data = json.load(f)
                            try:
                                if data['data']['usersByDevice'] is not None:
                                    for i in data['data']['usersByDevice']:
                                        columns['Brands'].append(i['brand'])
                                        columns['User_Count'].append(i['count'])
                                        columns['Percentage'].append(i['percentage'])
                                        columns['State'].append(state)
                                        columns['Year'].append(year)
                                        columns['Quarter'].append(int(file.strip('.json')))
                            except: pass
    df = pd.DataFrame(columns)
    df['State'] = df['State'].str.replace('-', ' ').str.title()
    return df

def extract_agg_insur():
    path = base_path + "aggregated/insurance/country/india/state/"
    columns = {'State': [], 'Year': [], 'Quarter': [], 'Insurance_type': [], 'Insurance_count': [], 'Insurance_amount': []}
    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if os.path.isdir(state_path):
            for year in os.listdir(state_path):
                year_path = os.path.join(state_path, year)
                if os.path.isdir(year_path):
                    for file in os.listdir(year_path):
                        with open(os.path.join(year_path, file), 'r') as f:
                            data = json.load(f)
                            try:
                                for i in data['data']['transactionData']:
                                    columns['Insurance_type'].append(i['name'])
                                    columns['Insurance_count'].append(i['paymentInstruments'][0]['count'])
                                    columns['Insurance_amount'].append(i['paymentInstruments'][0]['amount'])
                                    columns['State'].append(state)
                                    columns['Year'].append(year)
                                    columns['Quarter'].append(int(file.strip('.json')))
                            except: pass
    df = pd.DataFrame(columns)
    df['State'] = df['State'].str.replace('-', ' ').str.title()
    return df

# ==========================================
# 2. MAP DATA EXTRACTION FUNCTIONS
# ==========================================
def extract_map_trans():
    path = base_path + "map/transaction/hover/country/india/state/"
    columns = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Transaction_count': [], 'Transaction_amount': []}
    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if os.path.isdir(state_path):
            for year in os.listdir(state_path):
                year_path = os.path.join(state_path, year)
                if os.path.isdir(year_path):
                    for file in os.listdir(year_path):
                        with open(os.path.join(year_path, file), 'r') as f:
                            data = json.load(f)
                            try:
                                for i in data['data']['hoverDataList']:
                                    columns['District'].append(i['name'])
                                    columns['Transaction_count'].append(i['metric'][0]['count'])
                                    columns['Transaction_amount'].append(i['metric'][0]['amount'])
                                    columns['State'].append(state)
                                    columns['Year'].append(year)
                                    columns['Quarter'].append(int(file.strip('.json')))
                            except: pass
    df = pd.DataFrame(columns)
    df['State'] = df['State'].str.replace('-', ' ').str.title()
    df['District'] = df['District'].str.replace(' district', '').str.title()
    return df

def extract_map_user():
    path = base_path + "map/user/hover/country/india/state/"
    columns = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Registered_users': [], 'App_opens': []}
    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if os.path.isdir(state_path):
            for year in os.listdir(state_path):
                year_path = os.path.join(state_path, year)
                if os.path.isdir(year_path):
                    for file in os.listdir(year_path):
                        with open(os.path.join(year_path, file), 'r') as f:
                            data = json.load(f)
                            try:
                                for district, metrics in data['data']['hoverData'].items():
                                    columns['District'].append(district)
                                    columns['Registered_users'].append(metrics['registeredUsers'])
                                    columns['App_opens'].append(metrics['appOpens'])
                                    columns['State'].append(state)
                                    columns['Year'].append(year)
                                    columns['Quarter'].append(int(file.strip('.json')))
                            except: pass
    df = pd.DataFrame(columns)
    df['State'] = df['State'].str.replace('-', ' ').str.title()
    df['District'] = df['District'].str.replace(' district', '').str.title()
    return df

def extract_map_insur():
    path = base_path + "map/insurance/hover/country/india/state/"
    columns = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Insurance_count': [], 'Insurance_amount': []}
    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if os.path.isdir(state_path):
            for year in os.listdir(state_path):
                year_path = os.path.join(state_path, year)
                if os.path.isdir(year_path):
                    for file in os.listdir(year_path):
                        with open(os.path.join(year_path, file), 'r') as f:
                            data = json.load(f)
                            try:
                                for i in data['data']['hoverDataList']:
                                    columns['District'].append(i['name'])
                                    columns['Insurance_count'].append(i['metric'][0]['count'])
                                    columns['Insurance_amount'].append(i['metric'][0]['amount'])
                                    columns['State'].append(state)
                                    columns['Year'].append(year)
                                    columns['Quarter'].append(int(file.strip('.json')))
                            except: pass
    df = pd.DataFrame(columns)
    df['State'] = df['State'].str.replace('-', ' ').str.title()
    df['District'] = df['District'].str.replace(' district', '').str.title()
    return df

# ==========================================
# 3. TOP DATA EXTRACTION FUNCTIONS
# ==========================================
def extract_top_trans():
    path = base_path + "top/transaction/country/india/state/"
    columns = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Transaction_count': [], 'Transaction_amount': []}
    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if os.path.isdir(state_path):
            for year in os.listdir(state_path):
                year_path = os.path.join(state_path, year)
                if os.path.isdir(year_path):
                    for file in os.listdir(year_path):
                        with open(os.path.join(year_path, file), 'r') as f:
                            data = json.load(f)
                            try:
                                for i in data['data']['districts']:
                                    columns['District'].append(i['entityName'])
                                    columns['Transaction_count'].append(i['metric']['count'])
                                    columns['Transaction_amount'].append(i['metric']['amount'])
                                    columns['State'].append(state)
                                    columns['Year'].append(year)
                                    columns['Quarter'].append(int(file.strip('.json')))
                            except: pass
    df = pd.DataFrame(columns)
    df['State'] = df['State'].str.replace('-', ' ').str.title()
    df['District'] = df['District'].str.title()
    return df

def extract_top_user():
    path = base_path + "top/user/country/india/state/"
    columns = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Registered_users': []}
    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if os.path.isdir(state_path):
            for year in os.listdir(state_path):
                year_path = os.path.join(state_path, year)
                if os.path.isdir(year_path):
                    for file in os.listdir(year_path):
                        with open(os.path.join(year_path, file), 'r') as f:
                            data = json.load(f)
                            try:
                                for i in data['data']['districts']:
                                    columns['District'].append(i['name'])
                                    columns['Registered_users'].append(i['registeredUsers'])
                                    columns['State'].append(state)
                                    columns['Year'].append(year)
                                    columns['Quarter'].append(int(file.strip('.json')))
                            except: pass
    df = pd.DataFrame(columns)
    df['State'] = df['State'].str.replace('-', ' ').str.title()
    df['District'] = df['District'].str.title()
    return df

def extract_top_insur():
    path = base_path + "top/insurance/country/india/state/"
    columns = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Insurance_count': [], 'Insurance_amount': []}
    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if os.path.isdir(state_path):
            for year in os.listdir(state_path):
                year_path = os.path.join(state_path, year)
                if os.path.isdir(year_path):
                    for file in os.listdir(year_path):
                        with open(os.path.join(year_path, file), 'r') as f:
                            data = json.load(f)
                            try:
                                for i in data['data']['districts']:
                                    columns['District'].append(i['entityName'])
                                    columns['Insurance_count'].append(i['metric']['count'])
                                    columns['Insurance_amount'].append(i['metric']['amount'])
                                    columns['State'].append(state)
                                    columns['Year'].append(year)
                                    columns['Quarter'].append(int(file.strip('.json')))
                            except: pass
    df = pd.DataFrame(columns)
    df['State'] = df['State'].str.replace('-', ' ').str.title()
    df['District'] = df['District'].str.title()
    return df

# ==========================================
# 4. EXECUTION AND DATABASE LOADING
# ==========================================
print("Starting Data Extraction... This may take a minute.")

# Extract all 9 DataFrames
df_agg_trans = extract_agg_trans()
df_agg_user = extract_agg_user()
df_agg_insur = extract_agg_insur()

df_map_trans = extract_map_trans()
df_map_user = extract_map_user()
df_map_insur = extract_map_insur()

df_top_trans = extract_top_trans()
df_top_user = extract_top_user()
df_top_insur = extract_top_insur()

print("Extraction Complete! Connecting to SQLite Database...")

# Connect to the SQLite database
conn = sqlite3.connect('phonepe_pulse.db')

# Push all 9 DataFrames into 9 separate SQL tables
df_agg_trans.to_sql('Aggregated_transaction', conn, if_exists='replace', index=False)
df_agg_user.to_sql('Aggregated_user', conn, if_exists='replace', index=False)
df_agg_insur.to_sql('Aggregated_insurance', conn, if_exists='replace', index=False)

df_map_trans.to_sql('Map_map', conn, if_exists='replace', index=False)
df_map_user.to_sql('Map_user', conn, if_exists='replace', index=False)
df_map_insur.to_sql('Map_insurance', conn, if_exists='replace', index=False)

df_top_trans.to_sql('Top_map', conn, if_exists='replace', index=False)
df_top_user.to_sql('Top_user', conn, if_exists='replace', index=False)
df_top_insur.to_sql('Top_insurance', conn, if_exists='replace', index=False)

print("All 9 tables successfully created and populated in 'phonepe_pulse.db'!")

# Close the database connection
conn.close()