from database.db_connection import DB_connection


instance_connection = DB_connection()


class AgentDB:
    def create_agent(self,data):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "insert into agents (name,specialty,agent_rank) valuse(%s,%s,%s)"
            cursor.execute(sql,(data["name"],data["specialty"],data["agent_rank"],))
            conn.commite()
            return {"message":"success to create agent"}

        finally:
            cursor.close()
            conn.close()

    def get_all_agents(self):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select * from agents")
            result = cursor.fetchall()
            return result

        finally:
            cursor.close()
            conn.close()

    def get_agent_by_id(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select * from agents where id = %s",(id,))
            result = cursor.fetchone()
            return result
        
        finally:
            cursor.close()
            conn.close()


    

    def update_agent(self,id, data):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "update agents set name = %s,specialty = %s,is_active = %s,completed_missions = %s,failed_missions = %s,agent_rank = %s, where id = %s"
            cursor.execute(sql,(data["name"],data["specialty"],data["is_active"],data["completed_missions"],data["failed_missions"],data["agent_rank"],id))
            conn.commite()
            return {"message":"success to update agent"}
        finally:
            cursor.close()
            conn.close()

    def deactivate_agent(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "update agents set is_active = FALSE  where id = %s"
            cursor.execute(sql,(id))
            conn.commite()
            return {"message":"success to deactivate agent"}
        finally:
            cursor.close()
            conn.close()


    def increment_complete(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "update agents set completed_missions = completed_missions + 1  where id = %s"
            cursor.execute(sql,(id))
            conn.commite()
            return {"message":"success to increment agent"}
        finally:
            cursor.close()
            conn.close()


    def increment_failed(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "update agents set completed_missions = completed_missions - 1  where id = %s"
            cursor.execute(sql,(id))
            conn.commite()
            return {"message":"success to increment failde agent"}
        finally:
            cursor.close()
            conn.close()

    def get_agent_performance(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select completed_missions as completed,failed_missions as failed,count(*) as count from agents where id = %s"(id,))
            result = cursor.fetchall()
            return {"completed":result["completed"],
                    "failed":result["failed"],
                    "total":result["completed"] + result["failed"],
                    "success_rate": (result["completed"] + result["failed"]) / result["completed"]}
        
        finally:
            cursor.close()
            conn.close()



    def count_active_agents(self):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select * from agents where is_active = TRUE")
            result = cursor.fetchall()
            return result
        
        finally:
            cursor.close()
            conn.close()

