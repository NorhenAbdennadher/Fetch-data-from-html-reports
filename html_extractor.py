"""
File:           html_extractor.py
Author:         Norhen Abdennadher
Date:           24.02.2023
Description:    Fetching data from a HTML file with
                beautiful soup.
"""


# Necessary imports
import pandas as pd 
from bs4 import BeautifulSoup 
from html_table_extractor.extractor import Extractor


class html2df:

    @staticmethod
    #so this method returns a list of html tables (these tables are also converted to a list)
    def get_html_tables(html) -> list[list[str]]: 
        ''' Parse HTML to BeautifulSoup and extract all tables'''
        if html:
            soup = BeautifulSoup(html, "html.parser") #The HTML file needs to be prepared. This is done by passing the file to the BeautifulSoup constructor
            #Now we can use Beautiful Soup to navigate our website and extract data
            soup.prettify()
            extract_tables = soup.find_all("table")

            #The find_all() method takes an HTML tag as a string argument and returns the list of elements that match with the provided tag.
            return extract_tables

    @staticmethod
    #This method, checks all tables inside the list all table, and create a new list containing only tables that
    #have a header = tag that should be <th>, and that have a header content=table_feature and returns the 1st one
    def select_table(tag: str, table_feature: str, all_tables: list, all: int):
        ''' Return specific table from list of tables based on header name'''
        try:
            #In Html a table header is defined using a <thead> tag where <thead> stands for table head. Each <th> element represents one table cell.
            html_table = [table for table in all_tables for header in table.find_all(
                tag) if table_feature == header.text]
            if (all==0):
                return html_table[0]
            else:
                return html_table
            
        except (TypeError, IndexError):
            return None

    @staticmethod
    #returns table[i,j]
    def get_value(df_table, row: str, column: str) -> str:
        ''' Get value from dataframe table '''
        df_value = df_table[df_table.values == row][column].item()
        return df_value

    @staticmethod
    #converts a html extracted table to a dataframe
    def list_2df(table) -> pd.DataFrame:
        ''' Convert HTML table to Dataframe'''
        ex = Extractor(table)
        ex.parse()
        list_of_lines = ex.return_list()
        df = pd.DataFrame(list_of_lines[1:], columns=list_of_lines[0])
        return df
