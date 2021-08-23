import psycopg2
try:
    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            database="postgres",
                            user="postgres",
                            password="5678"
                            )
    cur = conn.cursor()
    query = 'create table demo(name varchar(15), age numeric(2))'
    cur.execute(query)
    conn.commit()
except Exception as e:
    print('exception=', e)
finally:
    cur.close()
    conn.close()
    print('connections closed')

