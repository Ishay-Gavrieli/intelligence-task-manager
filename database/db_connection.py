import mysql.connector


class DB_connection:
    def get_connection(self):
        return mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = 1234,
            database = "Intelligence_db")
    
    def create_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS Intelligence_db;")
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def creat_table(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        create_agent = """CREATE TABLE IF NOT EXISTS agents(
                                id INT PRIMARY KEY AUTO_INCREMENT,
                                name VARCHAR(50) NOT NULL,
                                specialty VARCHAR(50),
                                is_active BOOLEAN DEFAULT TRUE,
                                completed_missions INT DEFAULT 0,
                                failed_missions INT DEFAULT 0,
                                agent_rank ENUM("Junior","Senior","Commander"));"""


        create_mission = """CREATE TABLE IF NOT EXISTS missions(
                                id INT PRIMARY KEY AUTO_INCREMENT,
                                title VARCHAR(50),
                                description VARCHAR(100),
                                location VARCHAR(50),
                                difficulty INT CHECK (difficulty >= 1 AND  difficulty <= 10),
                                importance INT CHECK (difficulty >= 1 AND  difficulty <= 10),
                                status VARCHAR(50) DEFAULT "NEW",
                                risk_level VARCHAR(50),
                                assigned_agent_id INT NULL);"""
        try:
            cursor.execute(create_agent)
            cursor.execute(create_mission)
            conn.commit()
        finally:
            cursor.close()
            conn.close()
