#!/usr/bin/env python

import psycopg2

DB_NAME = "news"
SQL_QUERY_1 = """SELECT path,COUNT(*) as total 
FROM log JOIN articles ON path = format('/article/'||articles.slug) 
GROUP BY path ORDER BY total DESC LIMIT 3"""
SQL_QUERY_2 = """SELECT name,COUNT(*) AS total 
FROM authors JOIN articles ON author = authors.id JOIN log ON path = format('/article/'||articles.slug) 
GROUP BY name ORDER BY total DESC"""
SQL_QUERY_3_SUCCESS = """SELECT date(time) as Date,count(*) as SuccessTime 
FROM log where status = '200 OK' 
GROUP BY Date ORDER BY SuccessTime desc"""
SQL_QUERY_3_FAIL = """SELECT date(time) as Date,count(*) as ErrorTime 
FROM log where status = '404 NOT FOUND' 
GROUP BY Date ORDER BY ErrorTime desc"""


def get_data_from_query(query, database_name):
    db = psycopg2.connect(database=database_name)
    c = db.cursor()
    c.execute(query)
    data = c.fetchall()
    db.close()
    return data


def question_one():
    print ("Question 1")
    for data in get_data_from_query(SQL_QUERY_1, DB_NAME):
        print('{0} {2} {1} {3}'.format(data[0].replace("/article/", "").replace("-", " ")
                                       , data[1]
                                       , ":"
                                       , "views")
              )

    return "======"


def question_two():
    print ("Question 2")
    for data in get_data_from_query(SQL_QUERY_2, DB_NAME):
        print('{0} {1} {2} {3}'.format(data[0], ":", data[1], "views"))

    return "======"


def question_three():
    print ("Question 3");
    for good_data in get_data_from_query(SQL_QUERY_3_SUCCESS, DB_NAME):
        for bad_data in get_data_from_query(SQL_QUERY_3_FAIL, DB_NAME):
            if good_data[0] == bad_data[0]:
                bad_traffic_percent = (bad_data[1]*100)/good_data[1]
                if bad_traffic_percent > 1:
                    print('{0} {1} {2} {3} {4}'.format("Date:"
                                                       , good_data[0]
                                                       , "has bad Traffic of "
                                                       , bad_traffic_percent
                                                       , "%"))

    return "======"


def get_all_answer():
    print(question_one())
    print(question_two())
    return question_three()


print(get_all_answer())
