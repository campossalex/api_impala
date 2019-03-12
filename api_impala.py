from impala.dbapi import connect
import json

def query(args):
    id = args.get('name')
    conn = connect(host='10.0.0.168', port=21050)
    cursor = conn.cursor()
    cursor.execute('SELECT * from simon_r.players where name = "' + id + '"')
    for row in cursor:
        return row
    
#query(json.loads('{ "name": "Aaron Swinson" }'))
