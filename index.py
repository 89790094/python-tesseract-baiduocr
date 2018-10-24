from apscheduler.schedulers.blocking import BlockingScheduler

from mongo import db
from mysql import conn, cursor
from baidu import baiduOcr
from tesseract import general, advanced
from help import fetchRemoteImg, fetchImgUrl


def main():
    pass


'''mongodb'''


def mongoJob():
    task = db.taskExecuteLog.find_one({'tit': 'question_ocr_keyword'})
    if task != None:
        for qs in db.question.find({'audit.pass': False, 'createAt': {'$gt': task['flag']}}).sort('creatAt').limit(1):
            pass
    else:
        for qs in db.question.find({'audit.pass': False}).sort('creatAt').limit(1):
            db.taskExecuteLog.update_one({'tit': 'question_ocr_keyword'}, {'$set': {'flag': qs['createAt'], 'count': 1}}, upsert=True)


'''mysql'''

def mysqlJob():
    # sql
    sql = 'select * from ms_qstem where id=413846;'
    cursor.execute(sql)
    result = cursor.fetchone()
    print(fetchImgUrl(result['question']))


if __name__ == '__main__':
    print(mysqlJob())
