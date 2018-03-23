#!/usr/bin/env python
# "Database code" for the DB Forum.


import datetime
import psycopg2
import bleach


DBNAME = "news"


def get_query(q):
        """Connects to the database and returns the results"""
        db = psycopg2.connect(dbname=DBNAME)
        c = db.cursor()
        c.execute(q)
        rows = c.fetchall()
        db.close()
        return rows


if __name__ == '__main__':
        print('popular three articles:')
        print
        # make my query
        # What are the most popular three articles of all time?
        q1 = """SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE CONCAT('/article/%',articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;"""
        # Run Query
        results = get_query(q1)  # return rows in result
        # print results
        number = '#'
        i = 0
        for row in results:
            # title = row[0]
                tuple = row
                for j in tuple:
                        print j,
                print
        # print(  number   + title  + ' views' )

        q2 = """SELECT authors.name, count(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path LIKE concat('/article/%',articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 4;"""
        # Run Query
        results = get_query(q2)  # return rows in result
        print
        print("most popular article authors of all time : ")
        print
        # print results
        for row in results:
                tuple = row
                for j in tuple:
                        print j,
                print

        q3 = """ SELECT status_table.day, ROUND(((errors_table.err_requests * 1.0)/
        status_table.all_requests),3)
        AS percentage
        FROM
        (SELECT DATE_TRUNC('day',time)"day", COUNT (*) AS err_requests FROM log
        WHERE status LIKE '404%' GROUP BY day)
        AS errors_table
        JOIN
        (SELECT DATE_TRUNC('day',time)"day",
        COUNT (*)AS all_requests FROM log GROUP BY day ) AS status_table
        ON status_table.day=errors_table.day
        WHERE (ROUND (((errors_table.err_requests * 1.0)/
        status_table.all_requests),3)>0.01);"""

        results = get_query(q3)
        print
        print ("errors are :")
        # print results
        for row in results:
                tuple = row
                print
                for j in tuple:
                        print j,
                print
