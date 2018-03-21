import sqlite3
from YimiAutoCurrency.constants import sqlite_path


def sqlite_select(sql, data=''):
    conn = sqlite3.connect(sqlite_path.DATABASE)
    cur = conn.cursor()
    data = cur.execute(sql, data).fetchall()
    col_name_list = [tup[0] for tup in cur.description]
    cur.close()
    conn.close()
    data = [{key: str(value) for key, value in zip(col_name_list, da)} for da in data]
    return data


def sqlite_update(sql):
    conn = sqlite3.connect(sqlite_path.DATABASE)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


def sqlite_inster(sql):
    conn = sqlite3.connect(sqlite_path.DATABASE)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    print(sqlite_select('SELECT * FROM user_case_suite_data;'))
