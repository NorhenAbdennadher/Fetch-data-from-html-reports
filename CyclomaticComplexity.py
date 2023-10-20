"""
File:           CyclomaticComplexity.py
Author:         Norhen Abdennadher
Date:           24.02.2023
Description:    Fetching cyclomatic complexity
                data from Code prover report.
"""


# Necessary imports
import os
import pandas as pd
from html_extractor import html2df

  
def fetch_cyclcomp(config): 
    """
    Fetch the cyclomatic complexity from the code prover report
    :path: the path to the code prover report
    :return: count and value
    """
    val1=config.get("cyclometric_complexity_ranges", "value1")
    val2=config.get("cyclometric_complexity_ranges", "value2")
    val3=config.get("cyclometric_complexity_ranges", "value3")

    input_path=os.path.abspath(config.get("cyclometric_complexity_file", "input_path"))
    output_path=os.path.abspath(config.get("cyclometric_complexity_file", "output_path"))

    df = pd.read_csv(input_path, delimiter='\t')
    df=df.to_excel(output_path, index=False)
    dataframe = pd.read_excel(output_path)
    #filter all rows with check = cyclomatic complexity
    dataframe=dataframe[dataframe['Check']=='Cyclomatic Complexity']
    dataframe['Information']=pd.to_numeric(dataframe['Information'])
    #count how many functions have a cc in a certain range
    count1=len(dataframe[dataframe['Information'] <= int(val1)])
    count2=len(dataframe[(dataframe['Information'] > int(val1)) & (dataframe['Information'] <= int(val2))])
    count3=len(dataframe[(dataframe['Information'] > int(val2)) & (dataframe['Information'] <= int(val3))])
    count4=len(dataframe[dataframe['Information'] > int(val3)])

    #Create the ranges
    range1='[<={}]'.format(val1)
    range2='[{}-{}]'.format(int(val1)+1, val2)
    range3='[{}-{}]'.format(int(val2)+1, val3)
    range4='[>{}]'.format(val3)

    return(count1,count2, count3,count4,range1,range2,range3,range4)









