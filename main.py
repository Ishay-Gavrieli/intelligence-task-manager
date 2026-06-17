from database.db_connection import DB_connection

instance_connection = DB_connection()

instance_connection.create_database()

instance_connection.create_table()


