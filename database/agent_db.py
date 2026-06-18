from database.db_connection import DB_connection
from fastapi import HTTPException
from logs.basic_log import logger

instance_connection = DB_connection()


class AgentDB:
    def create_agent(self,data):
        valid = ("junior","senior","commander")
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)
        if data["agent_rank"].lower() not in valid:
            logger.error(f"error agent rank is not valid {data["agent_rank"]}")
            raise HTTPException(status_code=400,detail="error agent rank is not valid")
        else:
            rank = data["agent_rank"].lower()
        try:
            sql = "insert into agents (name,specialty,agent_rank) values(%s,%s,%s)"
            cursor.execute(sql,(data["name"],data["specialty"],rank))
            last_id = cursor.lastrowid
            cursor.execute("select * from agents where id = %s",(last_id,))
            result = cursor.fetchone()
            conn.commit()

            logger.info("Agent created successfully:")
            return result
        except Exception as e:

            raise e
        finally:
            cursor.close()
            conn.close()

    def get_all_agents(self):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select * from agents")
            result = cursor.fetchall()
            logger.info("get all agents successfully:")
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
            logger.info("success to get agent by id")
            return result if result else None
        
        finally:
            cursor.close()
            conn.close()


    

    def update_agent(self,id, data):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "update agents set name = %s,specialty = %s,is_active = %s,completed_missions = %s,failed_missions = %s,agent_rank = %s where id = %s"
            cursor.execute(sql,(data["name"],data["specialty"],data["is_active"],data["completed_missions"],data["failed_missions"],data["agent_rank"],id))
            conn.commit()
            logger.info("success to update agent")
            return {"message":"success to update agent"}
        finally:
            cursor.close()
            conn.close()

    def deactivate_agent(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "update agents set is_active = FALSE  where id = %s"
            cursor.execute(sql,(id,))
            conn.commit()
            logger.info("success to deactivate agent")
            return {"message":"success to deactivate agent"}
        finally:
            cursor.close()
            conn.close()


    def increment_complete(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "update agents set completed_missions = completed_missions + 1  where id = %s"
            cursor.execute(sql,(id,))
            conn.commit()
            logger.info("success to increment agent")
            return {"message":"success to increment agent"}
        finally:
            cursor.close()
            conn.close()


    def increment_failed(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "update agents set failed_missions = failed_missions + 1  where id = %s"
            cursor.execute(sql,(id,))
            conn.commit()
            logger.info("success to increment failde agent")
            return {"message":"success to increment failde agent"}
        finally:
            cursor.close()
            conn.close()

    def get_agent_performance(self,id):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select completed_missions as completed,failed_missions as failed from agents where id = %s",(id,))
            result = cursor.fetchone()
            rate = (result["completed"] / (result["completed"] + result["failed"])) * 100
            if rate > 0:
                rate = rate
            else:
                rate = 0
            logger.info("success to get_agent_performance")
            return {"completed":result["completed"],
                    "failed":result["failed"],
                    "total":result["completed"] + result["failed"],
                    "success_rate": round(rate)}
        
        finally:
            cursor.close()
            conn.close()



    def count_active_agents(self):
        conn = instance_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("select count(*) as count from agents where is_active = TRUE")
            result = cursor.fetchone()
            logger.info("success to count_active_agents")
            return result["count"]
        
        finally:
            cursor.close()
            conn.close()

