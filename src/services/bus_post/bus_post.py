import json
import pymysql

# DATABASE
DATABASE = {
    'host': 'YOUR HOST',
    'user': 'YOUR USER',
    'password': 'YOUR PASS',
    'db': 'YOUR DATABASE',
    'port': 3306,
    'cursorclass': pymysql.cursors.DictCursor
}


def main(evt, ctx):
    print('Event data:', evt)
    response = {'statusCode': 200, 'body': None}
    try:
        conn = pymysql.connect(**DATABASE)
        cursor = conn.cursor()
        params = None
        sql = 'SELECT 1;'
        if evt['action'] == "insert":
            sql = """
            INSERT INTO post(message, bus_id, user_id, published)
            VALUES(%s, %s, %s, 1)
            """
            params = (evt['data']['message'], evt['data']['bus_id'], evt['data']['user_id'])
        if evt['action'] == 'select':
            sql = """SELECT * FROM post ORDER BY id DESC;"""

        if params:
            result = cursor.execute(sql, params)
            response['statusCode'] = 201
        else:
            result = cursor.execute(sql)
            result = cursor.fetchall()
        conn.commit()
        conn.close()
    except Exception as e:
        response['statusCode'] = 500
        response['body'] = e
    return response
