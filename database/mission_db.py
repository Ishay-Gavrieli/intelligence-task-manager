from database.db_connection import DB_connection


instance_connection = DB_connection()


class MissionDB:
    def create_mission(self,data):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "insert into missions(title,description,location,difficulty,importance,status) values(%s,%s,%s,%s,%s,%s)"
            result = cursor.execute(sql,(data["title"],data["description"],data["location"],data["difficulty"],data["importance"],data["status"]))
            conn.commit()
            return result

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
            cursor.execute("select * from missions where id = %s",(id,))
            result = cursor.fetchone()
            return result
        
        finally:
            cursor.close()
            conn.close()


    def assign_mission(self,m_id, a_id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("update missions set status = ASSIGNED assigned_agent_id = %s where id = %s ",(a_id,m_id))
            conn.commit()
            return {"message":"success"}
        
        finally:
            cursor.close()
            conn.close()


    def update_mission_status(id, status):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("update missions set status = %s where id = %s ",(status,id))
            conn.commit()
            return {"message":"success"}
        
        finally:
            cursor.close()
            conn.close()


    def get_open_missions_by_agent(id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select status from missions where id = %s",(id,))
            result = cursor.fetchone()
            return result
        
        finally:
            cursor.close()
            conn.close()



    def count_all_missions():
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select count(*) as count from missions")
            result = cursor.fetchall()
            return result["count"]
        
        finally:
            cursor.close()
            conn.close()



    def count_by_status(status):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select count(*) as count from missions where status = %s",(status,))
            result = cursor.fetchall()
            return result["count"]
        
        finally:
            cursor.close()
            conn.close()



    def count_open_missions():
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select count(*) as count from missions where status = NEW")
            result = cursor.fetchall()
            return result["count"]
        
        finally:
            cursor.close()
            conn.close()


    def count_critical_missions():
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select count(*) as count from missions where risk_level = CRITICAL")
            result = cursor.fetchall()
            return result["count"]
        
        finally:
            cursor.close()
            conn.close()


    def get_top_agent():
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select name from agents order by completed_missions desc limit 1")
            result = cursor.fetchone()
            return result
        
        finally:
            cursor.close()
            conn.close()


