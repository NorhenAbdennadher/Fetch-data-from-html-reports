"""
File:           main.py
Author:         Norhen Abdennadher
Date:           24.02.2023
Description:    Connect to the database server, fetch data
                and insert it into MySQL database.
"""

import os
import argparse
import pandas as pd
from configparser import ConfigParser
from sqlalchemy import create_engine, text, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from cyclomatic_complexity_table import cyclometric_complexity
from misra_compliance_table import misra_compliance
from polyspace_compliance_table import polyspace_compliance
from binary_size_table import bp_binary_size
from CyclomaticComplexity import fetch_cyclcomp
from MISRACompliance import fetch_misraCompliance
from PolyspaceCompliance import fetch_polyspaceCompliance


def connect_database(db_server, db_user, db_password, db_port, db):
    """
    initializes a connection to a mysql database and returns a session
    :param db_server: the database server
    :param db_user: username of database
    :param db_password: password of database-user
    :param db_port: the port of the MySQL server
    :param db: name of the database
    :return: database-session | None
    """
    try:
        #The Engine is the starting point for any SQLAlchemy application. It’s “home base” for the 
        # actual database and its DBAPI, delivered to the SQLAlchemy application through a connection 
        # pool and a Dialect, which describes how to talk to a specific kind of database/DBAPI combination.
        engine = create_engine("mysql+pymysql://" + db_user + ":" + db_password
                               + "@" + db_server + ":" + db_port + "/" + db)
        engine.connect()
        factory = sessionmaker(bind=engine)
        session = factory()

    except Exception as e:
        print("Exception: ", e)
        return None
    return (engine,session)


def main():

    """ 
    parser = argparse.ArgumentParser(description='Tool for fetching data for ASPICE DAshboard Project')
    parser.add_argument('--CP_path', type=str, help='Path to polyspace code prover')
    parser.add_argument('--BF_path', type=str, help='Path to polyspace bug finder')
    parser.add_argument('--CM_path', type=str, help='Path to check memory file')

    args = parser.parse_args()
    BF_path = os.path.abspath(args.BF_path)
    CP_path = os.path.abspath(args.CP_path)
    CM_path = os.path.abspath(args.CM_path)

    with open(CM_path, 'r') as f:
        contents = f.read() 
    """
    #Read the configuration file
    config = ConfigParser()
    config.read('jenkins/aspice_dashboard/fetching_data_ci/config.ini')

    #extract ram and rom size information from the check memory file
    cm_file=os.path.abspath(config.get("check_memory_file", "cm_path"))
    
    with open(cm_file, 'r') as f:
        content = f.read()

    rom_size_percent = content.split('ROM_SIZE_RATIO:')[1].split(' %')[0].strip()
    dram_size_percent = content.split('RW_SIZE_RATIO:')[1].split(' %')[0].strip()
    stack_size_percent = content.split('STACK_SIZE_RATIO:')[1].split(' %')[0].strip()


    #Connect to the database
    #read database credentials
    server=config.get("database", "server")
    user=config.get("database", "user")
    pwr=config.get("database", "pwd")
    port=config.get("database", "port")
    name=config.get("database", "db")

    
    engine,session = connect_database(server, user, pwr,  port, name)
    
    # check if connection to dummy-database was successful
    if session is None:
        print("Error connecting to database!")
        raise SystemExit(1)
    print(engine,session)
    
    #fetch the data and create instances
    date=pd.to_datetime('today').date()
    
    count1,count2,count3,count4,range1,range2,range3,range4= fetch_cyclcomp(config)
    new_cc1 = cyclometric_complexity(date=date, 
                                range=range1, 
                                count=count1
                                )
    new_cc2 = cyclometric_complexity(date=date, 
                                range=range2, 
                                count=count2
                                )
    new_cc3 = cyclometric_complexity(date=date, 
                                range=range3, 
                                count=count3
                                )
    new_cc4 = cyclometric_complexity(date=date, 
                                range=range4, 
                                count=count4
                                )
    
    total_warnings, reviewed, unreviewed = fetch_misraCompliance (config)
    new_mc = misra_compliance(id=1,
                              total_warnings=int(total_warnings), 
                              unjustified_warnings=int(unreviewed), 
                              justified_warnings=int(reviewed), 
                              date=date)
    
    unjustified_red,justified_red,justified_orange,unjustified_orange,unjustified_grey,justified_grey=fetch_polyspaceCompliance(config)
    new_pc_red = polyspace_compliance(color= 'red',
                                    justified=int(justified_red),
                                    unjustified=int(unjustified_red),
                                    date=date)
    new_pc_orange = polyspace_compliance(color= 'orange',
                                    justified=int(justified_orange),
                                    unjustified=int(unjustified_orange),
                                    date=date)
    new_pc_grey = polyspace_compliance(color= 'grey',
                                    justified=int(justified_grey),
                                    unjustified=int(unjustified_grey),
                                    date=date)
    new_bs= bp_binary_size(rom=float(rom_size_percent), 
                           dram=float(dram_size_percent), 
                           date=date,
                           stack=float(stack_size_percent))
    
    # query for truncating the tables

    del_query_1 = text('TRUNCATE bp_cyclometric_complexity')
    del_query_2 = text('TRUNCATE bp_misra_compliance')
    del_query_3 = text('TRUNCATE bp_polyspace_compliance')
    session.execute(del_query_1.execution_options(autocommit=True))
    session.execute(del_query_2.execution_options(autocommit=True))
    session.execute(del_query_3.execution_options(autocommit=True))
    session.commit()

    #add data to database
    session.add(new_cc1)
    session.add(new_cc2)
    session.add(new_cc3)
    session.add(new_cc4)
    session.add(new_mc)
    session.add(new_pc_red)
    session.add(new_pc_orange)
    session.add(new_pc_grey)
    session.add(new_bs)
    session.commit()
    
    """inspector = inspect(engine)
    for table_name in inspector.get_table_names():
        print(table_name)
        for column in inspector.get_columns(table_name):
            print("Column: %s" % column['name'])"""

if __name__ == "__main__":
    main()
