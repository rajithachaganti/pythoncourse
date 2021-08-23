from findlength.utils import conn
def save_data(data, ch_count):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO WORD_DATA VALUES(%s,%s)"
        print(data, ch_count)
        cursor.execute(query, (data,ch_count))
        conn.commit()
        return True
    except Exception as e:
        print("Exception details : ", e)
    finally:
        cursor.close()
        conn.close()
