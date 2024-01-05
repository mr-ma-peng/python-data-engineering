# Code for ETL operations on Country-GDP data
# Importing the required libraries
import sqlite3
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attributes = ['Name', 'MC_USD_Billion']



def log_progress(message):
    """ This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('./banks_latest_data/etl_project_log.txt', 'a') as f:
        f.write(timestamp + ': ' + message + '\n')


def extract(url, table_attribs):
    """ This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. """
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 0:
            name_link = cols[1].find_all('a')[-1]
            if name_link is not None:
                data_dict = {
                    'Name': name_link.text,
                    'MC_USD_Billion': cols[2].text
                }
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)
    return df


def transform(df, csv_path):
    """ This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies"""

    return df


def load_to_csv(df, output_path):
    """ This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing."""


def load_to_db(df, sql_connection, table_name):
    """ This function saves the final data frame to a database
    table with the provided name. Function returns nothing."""


def run_query(query_statement, sql_connection):
    """ This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. """


''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''


log_progress("Preliminaries complete. Initiating ETL process")
df = extract(url, table_attributes)
print(df)
log_progress("Data extraction complete. Initiating Transformation process")
# df = transform(df)
# log_progress("Data transformation complete. Initiating Loading process")
# load_to_csv(df, output_path)
# log_progress("Data saved to CSV file")
# sql_connection = sqlite3.connect("")
# log_progress("SQL Connection initiated")
# load_to_db(df, sql_connection, table_name)
# log_progress("Data loaded to Database as a table, Executing queries")
# run_query("SELECT * FROM", sql_connection)
# log_progress("Process Complete")
# sql_connection.commit()
# log_progress("Server Connection closed")
