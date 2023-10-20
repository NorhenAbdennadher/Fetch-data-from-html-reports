"""
File:           misra_compliace.py
Author:         Norhen Abdennadher
Date:           24.02.2023
Description:    Fetching misra compliance data from
                Bug finder report.
"""


# Necessary imports
import os
from html_extractor import html2df


def fetch_misraCompliance (config):
    """
    Fetch the misra compliance from the bug finder report
    :path: the path to the bug finder report
    :return: count, reviewed, unreviewed, date
    """
    path=os.path.abspath(config.get("bug_finder_file", "bf_path"))
    
    # Opening the html file.
    HTMLFileToBeOpened = open(path, "r")
    # Reading the file and storing in a variable
    contents = HTMLFileToBeOpened.read()
    #Creating a list with all the tables
    all_tables=html2df.get_html_tables(contents)
    #Select the table that contains "MISRA C:2012 Guidelines"
    table=html2df.select_table('td', "MISRA C:2012 Guidelines", all_tables,0)
    #Convert the table to a dataframe, and select the value
    dftable=html2df.list_2df(table)
    count=html2df.get_value(dftable, "MISRA C:2012 Guidelines", "Count")
    reviewed=html2df.get_value(dftable, "MISRA C:2012 Guidelines", "Reviewed")
    unreviewed=html2df.get_value(dftable, "MISRA C:2012 Guidelines", "Unreviewed")
    

    return(count, reviewed, unreviewed)
