import psycopg2
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
cur.close()
conn.close()
print('connections closed')
