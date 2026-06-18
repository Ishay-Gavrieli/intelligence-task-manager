from database.db_connection import DB_connection
from fastapi import FastAPI
import uvicorn
from routes import agent_routes,mission_routes,report_routes


app = FastAPI()

instance_connection = DB_connection()

instance_connection.create_database()

instance_connection.create_table()


app.include_router(agent_routes.agent_router,prefix="/agents",tags=["agents"])

app.include_router(mission_routes.misions_router,prefix="/missions",tags=["missions"])

app.include_router(report_routes.reports_router,prefix="/reports",tags=["reports"])


if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)