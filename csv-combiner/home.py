import pandas as pd
import os.path as path

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
    print(inputlist)
    from pathlib import Path
    #source_files = sorted(Path('path_to_source_directory').glob('*.csv'))

    dataframes = []
    for file in inputlist:
        try:
            # df = pd.read_csv('fixtures/'+file)  # additional arguments up to your needs
            df = pd.read_csv(file)  # additional arguments up to your needs
            file_name = file.rsplit('/', 1)[-1]
            df['filename'] = file_name
            # print(df)
            dataframes.append(df)
        except FileNotFoundError:
            print("File not found.")
        except pd.errors.EmptyDataError:
            print("No data")
        except pd.errors.ParserError:
            print("Parse error")
        except Exception:
            print("Some other exception")


    print('============================')
    print(dataframes)
    df_all = pd.concat(dataframes)
    file_name = 'result.csv'
    df_all.to_csv(file_name,  encoding='utf-8')

if __name__ == '__main__':
    main()