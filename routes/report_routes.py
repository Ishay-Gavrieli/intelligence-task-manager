from fastapi import APIRouter,HTTPException
from database.mission_db import MissionDB
from database.agent_db import AgentDB
from logs.basic_log import logger


instance_agent = AgentDB()

instance_missions = MissionDB()

reports_router = APIRouter()



@reports_router.get("/summary")
def summary_all():

    logger.info("get /summary_all")
    try:
        result = {"active_agents_count": instance_agent.count_active_agents(),
                "total_missions": instance_missions.count_all_missions(),
                "open_missions": instance_missions.count_open_missions(),
                "completed_missions": instance_missions.count_by_status(status="completed"),
                "failed_missions": instance_missions.count_by_status(status="failed"),
                "cancelled_missions": instance_missions.count_by_status(status="CANCELED")
                }
        if result:
            logger.info("success to get summary_all")
            return result
        logger.error(f"failde to get summary_all")
        raise HTTPException(status_code=400,detail="bad data")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")


@reports_router.get("/missions-by-status")
def missions_by_status():
    logger.info("get /missions_by_status")
    try:
       
        result =  { "new": instance_missions.count_by_status(status="NEW"),
                "assigned":instance_missions.count_by_status(status="ASSIGNED"),
                "in_progress": instance_missions.count_by_status(status="IN_PROGRESS"),
                "completed": instance_missions.count_by_status(status="completed"),
                "failed": instance_missions.count_by_status(status="failed"),
                "canceled": instance_missions.count_by_status(status="CANCELED")}
        if result:
            logger.info("success to get missions_by_status")
            return result
        logger.error(f"failde to get missions_by_status")
        raise HTTPException(status_code=400,detail="bad data")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")


@reports_router.get("/top-agent")
def get_top_agent():

    logger.info("get /get_top_agent")
    try:

        result = instance_missions.get_top_agent()
        if result:
            logger.info("success to get_top_agent")
            return result
        logger.error(f"failde to get_top_agent")
        raise HTTPException(status_code=400,detail="bad data")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")