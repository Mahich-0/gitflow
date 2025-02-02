import sqlite3


def saving_data(tm, kills):
    con = sqlite3.connect("pygame.db")
    cursor = con.cursor()
    cursor.execute(f'INSERT INTO data(time, kills) VALUES ({tm // 1000}, {kills})')
    con.commit()
    con.close()


def return_data():
    con = sqlite3.connect("pygame.db")
    cursor = con.cursor()
    res = cursor.execute(f'SELECT time, kills FROM data ORDER BY id DESC').fetchall()
    con.commit()
    con.close()
    return res[0]


def return_record():
    con = sqlite3.connect("pygame.db")
    cursor = con.cursor()
    res = cursor.execute(f'SELECT time, kills FROM data ORDER BY time DESC').fetchall()
    con.commit()
    con.close()
    return res[0]
