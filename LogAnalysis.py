#!/usr/bin/env python

import psycopg2

DB_NAME = "news"
SQL_QUERY_1 = """SELECT title, views
    FROM articles
    INNER JOIN
        (SELECT path, count(path) AS views
         FROM log
         GROUP BY log.path) AS log
    ON log.path = '/article/' || articles.slug
    ORDER BY views DESC
    LIMIT 3;"""
SQL_QUERY_2 = """SELECT name,COUNT(*) AS total
FROM authors JOIN articles ON author = authors.id
JOIN log ON path = format('/article/'||articles.slug)
GROUP BY name ORDER BY total DESC"""
SQL_QUERY_3 = """SELECT
    date(time) as Date,
    Count(CASE status when '200 OK' then 1 else null end) as SuccessTime,
    Count(CASE status when '404 NOT FOUND' then 1 else null end) as FailTime,
    (COALESCE(Count(CASE status when '404 NOT FOUND' then 1 else null end),0)
     *100)/ Count(CASE status when '200 OK' then 1 else null end)
     as ErrorPercentage
from
log
GROUP BY
Date ORDER BY ErrorPercentage desc  """


def get_data_from_query(query, database_name):
    db = psycopg2.connect(database=database_name)
    c = db.cursor()
    c.execute(query)
    data = c.fetchall()
    db.close()
    return data


def question_one():
    report_string = "Question 1 \n"
    for data in get_data_from_query(SQL_QUERY_1, DB_NAME):
        report_string += '{0} {2} {1} {3} \n'.format(data[0].replace("/article/", "").replace("-", " "), data[1], ":", "views")
    return report_string


def question_two():
    report_string="Question 2 \n"
    for data in get_data_from_query(SQL_QUERY_2, DB_NAME):
        report_string += '{0} {1} {2} {3}'.format(data[0], ":", data[1], "views \n")

    return report_string


def question_three():
    report_string = "Question 3 \n"
    for data in get_data_from_query(SQL_QUERY_3, DB_NAME):
        if data[3] > 1:
            report_string += '{0} {1} {2} {3} {4}'.format("Date:", data[0], "has bad Traffic of ", data[3], "% \n")

    return report_string


def get_all_answer():
    f = open('Report.txt', 'w')
    f.write(str(question_one()))
    f.write(str(question_two()))
    f.write(str(question_three()))
    f.close()
    return ""


if __name__ == '__main__':
    get_all_answer()
else:
    print('I am being imported from another module')
