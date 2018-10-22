import pymysql

conn = pymysql.connect(host='8jieke.com', user='root', password='!Xueand123!', database='yunms', charset='utf8',cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
