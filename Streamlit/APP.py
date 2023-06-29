import mysql.connector
import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
import pandas as pd

connect3=sqlite3.connect("warehouse.db")
try:
    connect3.execute(
        """Create Table Warehouse (
            user_id INT NOT NULL,
            Name VARCHAR(20) NOT NULL,
            Lat FLOAT NOT NULL, Lon FLOAT NOT NULL, capacity INT NOT NULL, Date_time DATETIME ,Status_oc INT NOT NULL, Remarks VARCHAR(20) NOT NULL )"""
        
    )
except:
    print("DB already exists")
    
container =st.container()
with st.sidebar:
    selected=option_menu(menu_title="Main menu",options=["Home","ADD Warehouses"])
    if selected=="Home":
        container.title('Streamlit Warehouse Management App')
        container.caption('The APP uses Python to Add Warehouses ')
        
    elif selected=="ADD Warehouses":
        user_id =st.text_input("USER ID ")
        Name=st.text_input("Name")
        Lat=st.text_input("Lat")
        Lon=st.text_input("Lon")
        capacity=st.text_input("Capacity in tons")
        Date_time =st.text_input("Datetime DD-MM-YY HH:MM")
        Status_oc=st.text_input("Status ",0)
        Remarks =st.text_input("Remarks")
        conn=mysql.connector.connect(
        host="sql12.freemysqlhosting.net",
        user="sql12628843",
        password='tEVtIWSk1S',
        database="sql12628843" 
        )
        cursor=conn.cursor()
        selectquery="select * from Warehouse"
        cursor.execute(selectquery)
        records=cursor.fetchall()
        print(cursor.column_names)
        s1="insert into Warehouse values(%s,%s,%s,%s,%s,%s,%s,%s)"
        t=(user_id,Name,Lat,Lon,capacity,Date_time,Status_oc,Remarks)
        if st.button("Upload to SQL"):
            try:
                cursor.execute(s1,t)
                container.write ("Record Added")
                conn.commit()
                connect3.execute(s1,t)
            except:
                container.write ("Record Already exists")
        
        conn.close()
        connect3.close()
        