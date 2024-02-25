    # Connect to the database 
from datetime import date, datetime
from flask import Blueprint, request
import psycopg
import random
from psycopg.rows import class_row
from pydantic import BaseModel, ConfigDict, PostgresDsn
from typing import TypeVar, Optional, Generic
from typing import List
from flask_reports.models.web import Response
import asyncio

# FIXME Need Blueprint if no routes?
db_bp = Blueprint('db', __name__)

class Product(BaseModel):
    id: int
    name: str
    labelid: int
    category: str
    gender: str
    currentlyactive: bool
    created: datetime
    updated: Optional[datetime]

class Color(BaseModel):
    id: int
    name: str
    rgb: str

# class Foo(BaseModel):
#     f1: str  # required, cannot be None
#     f2: Optional[str]  # required, can be None - same as str | None
#     f3: Optional[str] = None  # not required, can be None
#     f4: str = 'Foobar'  # not required, but cannot be None

class Result(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    success: bool
    conn: Optional[psycopg.Connection] = None
    err: Optional[str] = None

class ProductResult(BaseModel):
    success: bool
    res: Optional[List[Product]] = None

class DbConn:
    def db_connect() -> Result:
        conn = psycopg.connect(dbname="flask_reports", 
                                user="postgres", 
                                password="postgres", 
                                host="localhost", port="5432") 


        res = Result(success=True, conn=conn)

        return res

    def get_colors() -> Response[List[Color]]:
        colors_query = '''SELECT * FROM webshop.colors'''
        products_query = '''SELECT * FROM webshop.products'''
    
        # Select all products from the table 
        conn_res = DbConn.db_connect()
        print(conn_res)
        if conn_res.success:
            conn = conn_res.conn
            with conn.cursor(row_factory=class_row(Color)) as cur:
                cur.execute(colors_query) 
        
                # Fetch the data 
                data = cur.fetchall() 
            
                # close cursor & connection 
                cur.close() 
                conn.close()

                print(data)
            
            return Response[List[Color]](data=data)
        else:
            return Response[List[Color]](data=None)
