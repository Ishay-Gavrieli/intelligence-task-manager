from database.db_connection import DB_connection


instance_connection = DB_connection()


class MissionDB:
    def create_mission(self,data):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "insert into missions (title,description,location,difficulty,importance,status) valuse(%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,(data["title"],data["description"],data["location"],data["difficulty"],data["importance"],data["status"],))
            conn.commite()
            return {"message":"success to create missions"}

        finally:
            cursor.close()
            conn.close()

    def get_all_agents(self):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select * from missions")
            result = cursor.fetchall()
            return result

        finally:
            cursor.close()
            conn.close()

    def get_agent_by_id(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select * from mission where id = %s",(id,))
            result = cursor.fetchone()
            return result
        
        finally:
            cursor.close()
            conn.close()


