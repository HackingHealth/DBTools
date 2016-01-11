# CreateNewDB.py
# 2015/12/10 Marcello Barisonzi
# Create an empty DB file from scratch

import pymysql, json
from samba.dcerpc.nbt import db_change_info

organization_table = """CREATE TABLE "organization" (
    "id" INTEGER PRIMARY KEY  AUTO_INCREMENT  NOT NULL , 
    "name" TEXT,
    "category_id" INTEGER);
    INSERT INTO organization VALUES (NULL,"Hacking Health", NULL);
    INSERT INTO organization VALUES (NULL,"CHU Sainte-Justine", 1);
    INSERT INTO organization VALUES (NULL,"CUSM/MUHC", 1);
    INSERT INTO organization VALUES (NULL,"CHUM", 1);
    INSERT INTO organization VALUES (NULL,"McGill", 7);
    INSERT INTO organization VALUES (NULL,"Concordia", 7);
    INSERT INTO organization VALUES (NULL,"Universit\u00e9 de Montr\u00e9al", 7);
    INSERT INTO organization VALUES (NULL,"UQ\u00c0M", 7);
    INSERT INTO organization VALUES (NULL,"ETS Montr\u00e9al", 7);
    INSERT INTO organization VALUES (NULL,"Ecole Polytechnique de Montr\u00e9al", 7);
    INSERT INTO organization VALUES (NULL,"Desjardins", 4); 
    INSERT INTO organization VALUES (NULL,"IBM", 2); 
    """

category_table = """CREATE TABLE "category" (
    "id" INTEGER PRIMARY KEY AUTO_INCREMENT  NOT NULL , 
    "type" TEXT)"""

attendee_table = """CREATE TABLE "attendee" (
    "id" INTEGER PRIMARY KEY AUTO_INCREMENT  NOT NULL , 
    "contact_id" INTEGER check(typeof("contact_id") = 'integer'),
    "event_id" INTEGER check(typeof("event_id") = 'integer')
    )"""

responsible_table = """CREATE TABLE "responsible" (
    "id" INTEGER PRIMARY KEY AUTO_INCREMENT  NOT NULL , 
    "contact_id" INTEGER check(typeof("contact_id") = 'integer'),
    "contactHH_id" INTEGER check(typeof("contactHH_id") = 'integer') 
    )"""

contact_table = """CREATE TABLE "contact" (
    "id" INTEGER PRIMARY KEY  AUTO_INCREMENT  NOT NULL ,
    "last_name" TEXT, 
    "first_name" TEXT, 
    "email" TEXT,
    "title" TEXT, 
    "responsible_id",
    "organization_id", 
    "role" TEXT, 
    "category_id", 
    "is_volunteer" BOOL,
    "is_active" BOOL,
    "notes" TEXT 
    )"""
    
event_table = """CREATE TABLE "event" (
    "id" INTEGER PRIMARY KEY  AUTO_INCREMENT  NOT NULL , 
    "eventbrite_id" INTEGER, 
    "date" DATETIME, 
    "event_title" TEXT, 
    "volunteer_call" BOOL)"""
    
# volunteer_table = """CREATE TABLE volunteer(
#   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#   last_name TEXT,
#   first_name TEXT,
#   title TEXT,
#   hh_responsible INT,
#   role TEXT,
#   category_id INT,
#   notes TEXT,
#   organization_id INT
# , email TEXT)"""


def main():
    f=open("pwd.json")
    db_params = json.load(f)
    f.close()
    
    conn = pymysql.connect(database = db_params["database"],
                           user     = db_params["user"],
                           password = db_params["password"],
                           host     = db_params["server"],
                           ssl      = db_params["ssl"])
    
    # create organization table
    conn.executescript(organization_table)
    
    conn.executescript(attendee_table)
    
    conn.execute(contact_table)
    
    #conn.execute(event_table)
    
    conn.execute(responsible_table)
    
    conn.commit()
    
    return

if __name__ == "__main__":
    main()