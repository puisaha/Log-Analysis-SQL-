# Logs Analysis
## Project Description
Python script uses psycopg2 to query a mock PostgreSQL database for a fictional news website.
My program shows three outputs:
top 3 articles of all time.
authors ranked by article views.
the days where more than 1% of logged access requests were errors.

news database has three table,table names are : articles,author,log.
articles : coloumns are author,title,slug,lead,body,lead,time,id.
author : coloumns are name,bio,id
log : coloumns are path,ip,method,status,time,id.The log has a database row for each time a reader loaded a web page.

Prerequisites:
Python 2.7
PostgreSQL
psycopg2

how to create the news database :
you can get the database:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

1.	Set-up Instructions :
	Create the news database in PostgreSQL
	From the command line, launch the psql console by typing: psql
	Check to see if a news database already exists by listing all databases with the command: \l
	If a news database already exists, drop it with the command: DROP DATABASE news;
	Create the news database with the command: CREATE DATABASE news;
	exit the console by typing: \q

2.  Unzip the downloaded file. unzip newsdata.zip.
	You should now have an sql script called newsdata.sql.

3.  From the command line, navigate to the directory containing newsdata.sql.

4. Import the schema and data in newsdata.sql to the news database by typing: psql -d news -f newsdata.sql.

How to run :
1. Once the news database has been set up, from the command line navigate to the directory containing newsdb.py.
2. Run the script by typing: python newsdb.py.



IDLE:
Open IDLE
In the menu bar click on Run -> Run Module or press F5 on your keyboard


