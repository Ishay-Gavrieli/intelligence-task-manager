from fastapi import APIRouter
from database.mission_db import MissionDB
from database.agent_db import AgentDB
from logs.basic_log import logger


instance_agent = AgentDB()

instance_missions = MissionDB()

reports_router = APIRouter()



@reports_router.get("/summary")
def summary_all():
    return {"active_agents_count": instance_agent.count_active_agents(),
            "total_missions": instance_missions.count_all_missions(),
            "open_missions": instance_missions.count_open_missions(),
            "completed_missions": instance_missions.count_by_status(status="completed"),
            "failed_missions": instance_missions.count_by_status(status="failed"),
            "cancelled_missions": instance_missions.count_by_status(status="CANCELED")
            }



@reports_router.get("/missions-by-status")
def missions_by_status():
    return { "new": instance_missions.count_by_status(status="NEW"),
            "assigned":instance_missions.count_by_status(status="ASSIGNED"),
            "in_progress": instance_missions.count_by_status(status="IN_PROGRESS"),
            "completed": instance_missions.count_by_status(status="completed"),
            "failed": instance_missions.count_by_status(status="failed"),
            "canceled": instance_missions.count_by_status(status="CANCELED")}



@reports_router.get("/top-agent")
def get_top_agent():
    return instance_missions.get_top_agent()