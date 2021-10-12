from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os

def get_data(config_path):
    config = read_yaml(config_path)
    
    #save dataset in the local directory 
    # create path to directory: artifacts/raw_local_dir/data.csv
    artifacts_dir = config["artifacts"]['artifacts_dir']
    raw_local_dir = config["artifacts"]['raw_local_dir']
    raw_local_file = config["artifacts"]['raw_local_file']

    ##path to directory
    raw_local_file_path = os.path.join(artifacts_dir, raw_local_dir, raw_local_file)

    df = pd.read_csv(raw_local_file_path)
    print(df.head())


    

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path = parsed_args.config)
