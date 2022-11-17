import pandas as pd
import os.path as path
import os
import numpy as np
from functools import reduce

DIR = path.abspath(path.dirname(__file__))
FILES = {
    'clothing.csv': ('Blouses', 'Shirts', 'Tanks', 'Cardigans', 'Pants', 'Capris', '"Gingham" Shorts',),
    'accessories.csv': ('Watches', 'Wallets', 'Purses', 'Satchels',),
    'household_cleaners.csv': ('Kitchen Cleaner', 'Bathroom Cleaner',),
}

# ./fixtures/clothing.csv ./fixtures/accessories.csv ./fixtures/household_cleaners.csv

def main():
    text = input("prompt \n")
    files = text.split('>')
    inputlist = files[0].split('./')
    from pathlib import Path
    #source_files = sorted(Path('path_to_source_directory').glob('*.csv'))

    dataframes = []
    output_name = 'result.csv'
    try:
        os.remove(output_name)
    except FileNotFoundError:
        print("File doesn't exist.")

    print(inputlist)
    print("-------------------------------")

    endList = []
    #index_col=-1
    for file in inputlist:
        try:
            list = pd.read_csv(file, nrows=0).columns.tolist()
            #print(list)
            endList.extend(list)
        except FileNotFoundError:
            print("File not found.")
    endList.append('filename')

    endList = reduce(lambda re, x: re+[x] if x not in re else re, endList, [])
    #print('------------',endList)
    df1 = pd.DataFrame(columns=endList)
    df2 = pd.DataFrame(columns=endList)
    #print(df1)
    df1.to_csv(output_name, index=False, mode='a', encoding='utf-8')


    for file in inputlist:
        try:
            #print('here',file)
            df = pd.read_csv(file, chunksize=1000)

            #print('here',df.columns)
            file_name = file.rsplit('/', 1)[-1]
            #print("finally",file_name)

            tempFrame = pd.DataFrame(columns=endList)
            for chunk in df:
                chunk['filename'] = file_name
                #print(output_name)
                header = chunk.columns.values.tolist()
                print(header)
                data_concat = pd.concat([df1, chunk],  # Append two pandas DataFrames
                                        ignore_index=True,
                                        sort=False)
                print(data_concat)
                data_concat.to_csv(output_name, index=False, header=False, mode='a', encoding='utf-8') #working
            #dataframes.append(df)
        except FileNotFoundError:
            print("File not found.")
        except pd.errors.EmptyDataError:
            print("No data")
        except pd.errors.ParserError:
            print("Parse error")


if __name__ == '__main__':
    main()