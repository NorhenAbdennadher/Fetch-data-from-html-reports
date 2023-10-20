"""
File:           PolyspaceCompliance.py
Author:         Norhen Abdennadher
Date:           24.02.2023
Description:    Fetching polyspace compliance data
                from Code prover report.
"""


# Necessary imports
import os
from html_extractor import html2df
from bs4 import BeautifulSoup

def fetch (all_tables, color):
    unjustified=0
    justified=0
    #iterate over the list tables, and check the color and the corresponding status
    style= '[style="color:{};"]'.format(color)
    for table in all_tables[5:]:
        row=table.find_all('tr') #find all rows in the selected table
        color_elements=table.select(style) #find all elements in red color
        color_row=[]
        color_ID=[]

        for r in row:
            elem=r.select(style)
            if (len(elem)!=0):
                color_row.append(r)
        #till here we have a list of all rows that have a colored element in this table.
        for rrow in color_row:
            html_text=str(rrow)
            soup = BeautifulSoup(html_text, 'html.parser')
            span_element = soup.find('span')
            extracted_id = span_element.text
            color_ID.append(extracted_id)
        #till here we have red_ID that contains the ID of red color and red_elements that has the element itself
        if (len(color_elements)>0):
            dftable=html2df.list_2df(table)
            for id in color_ID:
                value=html2df.get_value(dftable, id, "Status")
                if value=="Unreviewed":
                    unjustified+=1
                else:
                    justified+=1
    return(unjustified,justified)

def fetch_polyspaceCompliance (config):
    """
    Fetch the polyspace compliance from the code prover report
    :path: the path to the code prover report
    :return: unjustified_red,justified_red,unjustified_orange,justified_orange,unjustified_grey,justified_grey,date
    """
    path=os.path.abspath(config.get("code_prover_file", "cp_path"))
    # Opening the html file.
    HTMLFileToBeOpened = open(path, "r")
    # Reading the file and storing in a variable
    contents = HTMLFileToBeOpened.read()
    #Creating a list with all the tables
    all_tables=html2df.get_html_tables(contents)
    #table=html2df.select_table('span', 'Non-initialized local variable', all_tables, 1)
    (unjustified_red,justified_red)=fetch (all_tables,'#FF0000')
    (unjustified_orange,justified_orange)=fetch (all_tables,'#FFA500')
    (unjustified_grey,justified_grey)=fetch (all_tables,'#808080')
    return(unjustified_red,justified_red,unjustified_orange,justified_orange,unjustified_grey,justified_grey)


