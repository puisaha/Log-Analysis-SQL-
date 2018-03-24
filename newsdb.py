#!/usr/bin/env python
# "Database code" for the DB Forum.


import datetime
import psycopg2
import bleach


DBNAME = "news"


def execute_query(q):
        """Connects to the database and returns the results"""
        db = psycopg2.connect(dbname=DBNAME)
        c = db.cursor()
        c.execute(q)
        rows = c.fetchall()
        db.close()
        return rows


def print_top_articles():
        """Prints out the top 3 articles of all time."""
        query = """SELECT articles.title, COUNT(*) AS num
                FROM articles
                JOIN log
                ON log.path = '/article/' || articles.slug
                GROUP BY articles.title
                ORDER BY num DESC
                LIMIT 3;"""
        results = execute_query(query)
        # print results
        print ("top 3 articles of all time :")
        for row in results:
                print('"{}" -- {} views'.format(row[0], row[1]))
        print


def print_top_authors():
        """Prints a list of authors ranked by article views."""
        query = """SELECT authors.name, count(*) AS num
                FROM authors
                JOIN articles
                ON authors.id = articles.author
                JOIN log
                ON log.path = '/article/' || articles.slug
                GROUP BY authors.name
                ORDER BY num DESC
                LIMIT 4;"""
        results = execute_query(query)
        # print results
        print ("most popular authors of all time :")
        for row in results:
                print('"{}" -- {} views'.format(row[0], row[1]))
        print


def print_errors_over_one():
        """Prints where more than 1% of logged access requests were errors."""
        query = """ SELECT status_table.day, ROUND(((errors_table.err_requests * 1.0)/
                status_table.all_requests),3)
                AS percentage
                FROM
                (SELECT DATE_TRUNC('day',time)"day",
                COUNT (*) AS err_requests FROM log
                WHERE status LIKE '404%' GROUP BY day)
                AS errors_table
                JOIN
                (SELECT DATE_TRUNC('day',time)"day",
                COUNT (*)AS all_requests FROM log GROUP BY day )
                AS status_table
                ON status_table.day=errors_table.day
                WHERE (ROUND (((errors_table.err_requests * 1.0)/
                status_table.all_requests),3)>0.01);"""
        results = execute_query(query)
        # print results
        print ("errors are :")
        for row in results:
                print('{} -- {}% errors'.format(
                    row[0].strftime("%b %d %Y"), row[1]))

if __name__ == '__main__':
        print_top_articles()
        print_top_authors()
        print_errors_over_one()
