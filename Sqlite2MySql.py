from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import json

def copyTable(table_name, metadata, local_conn, remote_conn, auto_increment=False):
    print "Working on table %s" % table_name
    
    _table = Table(table_name, metadata, autoload=True, autoload_with=local_conn)

    metadata.create_all(remote_conn,[_table])

    result = local_conn.execute(_table.select())

    for i,r in enumerate(result):
        rnew = r
        if auto_increment:
            rnew = list(r)
            rnew[0]=None
            rnew=tuple(rnew)
        #print rnew
        #print str(_table.insert().values(rnew))
        remote_conn.execute(_table.insert().values(rnew))
        print "%d %s" % (i+1,rnew)
        
    return

# connect to the remote Database
f=open("pwd.json")
db_params = json.load(f)
f.close()

"""    
remote_conn = pymysql.connect(database = db_params["database"],
                              user     = db_params["user"],
                              password = db_params["password"],
                              host     = db_params["server"]) #,
                              #ssl      = db_params["ssl"])
    
   
remote_cursor = remote_conn.cursor()
"""

Session = sessionmaker()

engine = create_engine("sqlite:////mnt/windows/Users/Marcello-User/Dropbox/HH_Contacts.sqlite")
remote_engine = create_engine("mysql+pymysql://%(user)s:%(password)s@%(server)s/%(database)s?charset=utf8mb4" % db_params,convert_unicode=True)

Session.configure(bind=remote_engine)

sess = Session()

meta = MetaData()

copyTable("event", meta, engine, remote_engine)
copyTable("organization", meta, engine, remote_engine)
copyTable("attendee", meta, engine, remote_engine)
copyTable("category", meta, engine, remote_engine)
copyTable("contact", meta, engine, remote_engine)
copyTable("responsible", meta, engine, remote_engine)
copyTable("interaction", meta, engine, remote_engine)

sess.commit()
sess.close()