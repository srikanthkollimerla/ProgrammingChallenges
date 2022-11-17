import pandas as pd
import os
from functools import reduce
import sys


# ./fixtures/clothing.csv ./fixtures/accessories.csv ./fixtures/household_cleaners.csv

class CSVCombiner:

    def main(self):
        flag = False
        output_name = 'result.csv'
        inputlist = []
        for i in range(1, len(sys.argv) - 1):
            if sys.argv[i] == '>':
                flag = True
            else:
                inputlist.append(sys.argv[i])

        if flag == True:
            output_name = sys.argv[len(sys.argv) - 1]
        else:
            inputlist.append(sys.argv[len(sys.argv) - 1])

        try:
            os.remove(output_name)
        except FileNotFoundError:
            print("File doesn't exist.")

        #to find all the unique headers in all the given input files
        endList = []
        for file in inputlist:
            try:
                print('here:',file)
                list = pd.read_csv(file, nrows=0).columns.tolist()
                endList.extend(list)
            except FileNotFoundError:
                print("File not found.")
        endList.append('filename') #to save the source of the record

        endList = reduce(lambda re, x: re+[x] if x not in re else re, endList, [])

        df1 = pd.DataFrame(columns=endList)
        df1.to_csv(output_name, index=False, mode='a', encoding='utf-8') #an empty csv file with headers gets created


        for file in inputlist:
            try:
                df = pd.read_csv(file, chunksize=1000)
                file_name = file.rsplit('/', 1)[-1]

                for chunk in df:
                    chunk['filename'] = file_name

                    header = chunk.columns.values.tolist()
                    data_concat = pd.concat([df1, chunk],  # Append two pandas DataFrames
                                            ignore_index=True,
                                            sort=False)
                    data_concat.to_csv(output_name, index=False, header=False, mode='a', encoding='utf-8')
                    #chunk of records are extracted from each datafram and then the specific columns are assigned with values.
            except FileNotFoundError:
                print("File not found.")
            except pd.errors.EmptyDataError:
                print("No data")
            except pd.errors.ParserError:
                print("Parse error")
        return True

    def print(self, inputlist=[]):
        print('here')
        flag = False
        output = 'result.csv'
        print(len(sys.argv))
        for i in range(1,len(sys.argv) - 1):
            if sys.argv[i] == '>':
                flag = True
            else:
                inputlist.append(sys.argv[i])

        if flag == True:
            output = sys.argv[len(sys.argv) - 1]
        else:
            inputlist.append(sys.argv[len(sys.argv) - 1])

        print(inputlist)
        print(output)




if __name__ == '__main__':
    csvCombiner = CSVCombiner()
    csvCombiner.main()