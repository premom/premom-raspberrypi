import os
import pymysql
import serial

db = pymysql.connect(
        host='52.79.238.48',
        port=3306,
        user='premom',
        passwd='asdf7070!',
        db='PreMom',
        charset='utf8')

cursor = db.cursor()


is_seat = 1;
idx = 1;

sql = "update tbl_seat set is_seat=1 where idx=1"

cursor.execute(sql)

db.commit()
db.close()
