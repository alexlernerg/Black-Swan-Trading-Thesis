import mysql.connector
from mysql.connector import MySQLConnection, Error

def connect_database():

	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="password",
	  database="tradingstrategy",
	  auth_plugin='mysql_native_password',
	)
	print(mydb)
	return mydb

def insert(end_date, ten_per_highest_beta, ten_per_lowest_beta,
				portfolio_value, return_percentage_change, current_bucket_list, mycursor, con_mydb):

	# if ten_per_highest_beta is not None:
	# 	ten_per_highest_beta = ','.join(ten_per_highest_beta)
	# if ten_per_lowest_beta is not None:
	# 	ten_per_lowest_beta = ','.join(ten_per_lowest_beta)
	# if current_bucket_list is not None:
	# 	current_bucket_list = ','.join(current_bucket_list)

	query = ("INSERT INTO temp_portfolio (date_stamp,buy_list,sell_list,portfolio_value,return_percentage,bucket) VALUES (%s,%s,%s,%s,%s,%s)")
	values = (end_date, ten_per_highest_beta, ten_per_lowest_beta,
				portfolio_value, return_percentage_change, current_bucket_list)
	mycursor.execute( query, values )
	last_row_id = mycursor.lastrowid
	print(last_row_id)
	con_mydb.commit()
	return last_row_id


if __name__ == "__main__":

	""" create table """

	con_mydb = connect_database()
	mycursor = con_mydb.cursor()
	mycursor.execute(
			"CREATE TABLE temp_portfolio ( seq_no INT AUTO_INCREMENT PRIMARY KEY, date_stamp Date , buy_list Varchar(10000) , sell_list Varchar(10000) , portfolio_value Float(65,10) , return_percentage Float(65,10), bucket Varchar(10000) )")
