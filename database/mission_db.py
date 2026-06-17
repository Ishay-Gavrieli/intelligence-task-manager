from database.db_connection import DB_connection
from fastapi import HTTPException

instance_connection = DB_connection()


class MissionDB:
    def create_mission(self,data):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)
        risk_level = data["difficulty"] * 2 + data["importance"]
        risk = risk_level(risk_level)

        try:
            sql = "insert into missions(title,description,location,difficulty,importance,status,risk_level) values(%s,%s,%s,%s,%s,%s,%s)"
            result = cursor.execute(sql,(data["title"],data["description"],data["location"],data["difficulty"],data["importance"],data["status"],risk))
            conn.commit()
            return result

        finally:
            cursor.close()
            conn.close()

    def get_all_missions(self):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select * from missions")
            result = cursor.fetchall()
            return result

        finally:
            cursor.close()
            conn.close()

    def get_mission_by_id(self,id):
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
        agent = cursor.execute("select is_active from agents where id = %s"(a_id,))
        if not agent:
            raise HTTPException(status_code=400,detail="error")

        count = cursor.execute("select count(*) as count from missions where id = %s and status =IN_PROGRESS or status= ASSIGNED"(a_id,))
        if count["count"] >= 3:
            raise HTTPException(status_code=400,detail="error")

        level = cursor.execute("select risk_level as level from missions where id = %s"(m_id,))
        if level["level"] == "CRITICAL":
            rank = cursor.execute("select agent_rank as rank from agents where id = %s"(a_id,))
            if rank["rank"] != "Commander":
                raise HTTPException(status_code=400,detail="error")
        
        status = cursor.execute("select status as status from missions where id = %s"(m_id,))
        if status["status"] != "NEW":
             raise HTTPException(status_code=400,detail="error")

        try:
            cursor.execute("update missions set status = ASSIGNED assigned_agent_id = %s where id = %s ",(a_id,m_id))
            conn.commit()
            return {"message":"success"}
        
        finally:
            cursor.close()
            conn.close()


    def update_mission_status(self,id, status):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)
        status = cursor.execute("select status as status from missions where id = %s"(id,))
        if status["status"] == "ASSIGNED":
            if status["status"] != "IN_PROGRESS":
                raise HTTPException(status_code=400,detail="error")
        if status["status"] == "CANCELLED":
            if status["status"] != "NEW" or status["status"] != "ASSIGNED":
                raise HTTPException(status_code=400,detail="error")
        if status["status"] == "failed" or status["status"] == status["status"]:
            if status["status"] != "IN_PROGRESS":
                raise HTTPException(status_code=400,detail="error")
        try:
            cursor.execute("update missions set status = %s where id = %s ",(status,id))
            conn.commit()
            return {"message":"success"}
        
        finally:
            cursor.close()
            conn.close()


    def get_open_missions_by_agent(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select status from missions where id = %s",(id,))
            result = cursor.fetchone()
            return result
        
        finally:
            cursor.close()
            conn.close()



    def count_all_missions(self):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select count(*) as count from missions")
            result = cursor.fetchall()
            return result["count"]
        
        finally:
            cursor.close()
            conn.close()



    def count_by_status(self,status):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select count(*) as count from missions where status = %s",(status,))
            result = cursor.fetchall()
            return result["count"]
        
        finally:
            cursor.close()
            conn.close()



    def count_open_missions(self):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select count(*) as count from missions where status = NEW")
            result = cursor.fetchall()
            return result["count"]
        
        finally:
            cursor.close()
            conn.close()


    def count_critical_missions(self):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select count(*) as count from missions where risk_level = CRITICAL")
            result = cursor.fetchall()
            return result["count"]
        
        finally:
            cursor.close()
            conn.close()


    def get_top_agent(self):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select name from agents order by completed_missions desc limit 1")
            result = cursor.fetchone()
            return result
        
        finally:
            cursor.close()
            conn.close()


    def risk_level(self,number):
        if 0 <= number <= 9:
            return "low" 
        elif 10 <= number <= 17:
            return "medium"
        elif 18 <= number <= 24:
            return "high"
        else:
            return "critical"
