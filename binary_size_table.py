"""
File:           binary_size_table.py
Author:         Norhen Abdennadher
Date:           07.03.2023
Description:    Binary size mapping class, preparing
                instances to insert into MySQL table.
"""

from sqlalchemy import Column, Date, BigInteger, FLOAT
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class bp_binary_size(base):
    __tablename__ = "bp_binary_size"

    id = Column(
        BigInteger,  
        autoincrement=True,
        nullable = False, 
        primary_key = True
    )

    date = Column(
        Date, 
        nullable = False
    )

    rom = Column(
        FLOAT, 
        nullable = False
    )

    dram = Column(
        FLOAT, 
        nullable = False
    )

    stack = Column(
        FLOAT, 
        nullable = False
    )

    def __init__(self, date,rom,dram,stack,id=None):
        if id is not None:
            self.id = id

        self.date = date 
        self.rom = rom
        self.dram = dram
        self.stack= stack