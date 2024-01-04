import glob
import pandas as pd
from datetime import datetime


def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe


def extract_from_xml(file_to_process):
    dataframe = pd.read_xml(file_to_process)
    return dataframe


def extract():
    # create an empty data frame to hold extracted data
    extracted_data_internal = pd.DataFrame(columns=['name', 'height', 'weight'])

    # process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data_internal = pd.concat([extracted_data_internal, pd.DataFrame(extract_from_csv(csvfile))],
                                            ignore_index=True)

    # process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data_internal = pd.concat([extracted_data_internal, pd.DataFrame(extract_from_json(jsonfile))],
                                            ignore_index=True)

    # process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data_internal = pd.concat([extracted_data_internal, pd.DataFrame(extract_from_xml(xmlfile))],
                                            ignore_index=True)

    return extracted_data_internal


def transform(data):
    """
    convert inches to meters and round off to  two decimal 1 inch is 0.0254
    """
    data['height'] = round(data.height * 0.0254, 2)
    """
    convert inches to meters and round off to  two decimal 1 inch is 0.45359237
    """
    data['weight'] = round(data.weight * 0.45359237, 2)

    return data


def load_data(target_file_parameter, transformed_data_parameter):
    transformed_data_parameter.to_csv(target_file_parameter)


def log_progress(log_file_parameter, message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file_parameter, 'a') as f:
        f.write(timestamp + ',' + message + '\n')


if __name__ == '__main__':
    log_file = 'person_data/log_file.txt'
    target_file = 'transformed_data.csv'

    log_progress(log_file, "ETL: job started")

    log_progress(log_file, "ETL: extracting data started")
    extracted_data = extract()
    log_progress(log_file, "ETL: extracting data ended")

    log_progress(log_file, "ETL: transform data started")
    transformed_data = transform(extracted_data)
    log_progress(log_file, "ETL: transform data ended")

    log_progress(log_file, "ETL: load data started")
    load_data(target_file, transformed_data)
    log_progress(log_file, "ETL: load data ended")

    log_progress(log_file, "ETL: job completed")
