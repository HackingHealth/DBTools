# CreateNewDB.py
# 2015/12/10 Marcello Barisonzi
# Create an empty DB file from scratch

import pymysql, json

organization_table = """CREATE TABLE organization (
    id INTEGER PRIMARY KEY  AUTO_INCREMENT  NOT NULL , 
    name TEXT,
    category_id INTEGER);
    """    
#     INSERT INTO organization VALUES (NULL,"Hacking Health", NULL);
#     INSERT INTO organization VALUES (NULL,"CHU Sainte-Justine", 1);
#     INSERT INTO organization VALUES (NULL,"CUSM/MUHC", 1);
#     INSERT INTO organization VALUES (NULL,"CHUM", 1);
#     INSERT INTO organization VALUES (NULL,"McGill", 7);
#     INSERT INTO organization VALUES (NULL,"Concordia", 7);
#     INSERT INTO organization VALUES (NULL,"Universit\u00e9 de Montr\u00e9al", 7);
#     INSERT INTO organization VALUES (NULL,"UQ\u00c0M", 7);
#     INSERT INTO organization VALUES (NULL,"ETS Montr\u00e9al", 7);
#     INSERT INTO organization VALUES (NULL,"Ecole Polytechnique de Montr\u00e9al", 7);
#     INSERT INTO organization VALUES (NULL,"Desjardins", 4); 
#     INSERT INTO organization VALUES (NULL,"IBM", 2); 
#     """

category_table = """CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTO_INCREMENT  NOT NULL , 
    type TEXT)"""

attendee_table = """CREATE TABLE attendee (
    id INTEGER PRIMARY KEY AUTO_INCREMENT  NOT NULL , 
    contact_id INTEGER check(typeof("contact_id") = 'integer'),
    event_id INTEGER check(typeof("event_id") = 'integer')
    )"""

responsible_table = """CREATE TABLE responsible (
    id INTEGER PRIMARY KEY AUTO_INCREMENT  NOT NULL , 
    contact_id INTEGER check(typeof("contact_id") = 'integer'),
    contactHH_id INTEGER check(typeof("contactHH_id") = 'integer') 
    )"""

contact_table = """CREATE TABLE contact (
    id INTEGER PRIMARY KEY  AUTO_INCREMENT  NOT NULL ,
    last_name TEXT, 
    first_name TEXT, 
    email TEXT,
    title TEXT, 
    responsible_id BOOL,
    organization_id BOOL, 
    role TEXT, 
    category_id BOOL, 
    home_phone TEXT,
    work_phone TEXT,
    mobile_phone TEXT, 
    notes TEXT,
    is_volunteer BOOL,
    is_active BOOL,
    is_vip BOOL
    )"""
    
event_table = """CREATE TABLE event (
    id INTEGER PRIMARY KEY  AUTO_INCREMENT  NOT NULL , 
    eventbrite_id INTEGER, 
    date DATETIME, 
    event_title TEXT, 
    volunteer_call BOOL)"""

interaction_table = """CREATE TABLE interaction (
    id INTEGER PRIMARY KEY  AUTO_INCREMENT  NOT NULL , 
    contact_id INTEGER, 
    responsible_id INTEGER, 
    event_id INTEGER, 
    date DATETIME, 
    notes TEXT)"""

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
                           host     = db_params["server"]) #,
                           #ssl      = db_params["ssl"])
    
   
    c = conn.cursor()
   
#     c.executemany("""DROP TABLE organization;
#                      DROP TABLE attendee;
#                      DROP TABLE category;
#                      DROP TABLE contact;
#                      DROP TABLE event;
#                      DROP TABLE responsible;
#                      DROP TABLE interaction""",[])
   
    c.executemany(organization_table, [])
    
    c.executemany(attendee_table, [])
    
    c.execute(category_table)
    
    c.execute(contact_table)
    
    c.execute(event_table)
    
    c.execute(responsible_table)
    
    c.execute(interaction_table)
    
    conn.commit()
    
    return

if __name__ == "__main__":
    main()