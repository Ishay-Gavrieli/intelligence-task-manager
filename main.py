from database.db_connection import DB_connection
from fastapi import FastAPI
import uvicorn
from database.mission_db import MissionDB
from database.agent_db import AgentDB
instance_mission = MissionDB()
instance_agent = AgentDB()

app = FastAPI()

instance_connection = DB_connection()



instance_connection.create_database()

instance_connection.create_table()


# @app.post("/")
# def s(data:dict):
#     try:
#         return instance_mission.create_mission(data)
#     except Exception as e:
#         return f"error{e}"
    
# @app.get("/")
# def a():
#     return instance_mission.get_all_missions()


# @app.put("/")
# def f(id:int,status:str):
#     try:
#         return instance_mission.update_mission_status(id,status)
#     except Exception as e:
#         return f"error{e}"


@app.get("/")
def a():
    return instance_agent.count_active_agents()

if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)