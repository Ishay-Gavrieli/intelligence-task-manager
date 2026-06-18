from fastapi import APIRouter,HTTPException
from database.agent_db import AgentDB
from logs.basic_log import logger

instance_agent = AgentDB()

agent_router = APIRouter()


@agent_router.post("")
def create_agent(data:dict):
    logger.info("POST /agents called")
    if not data:
        logger.error("there is not data")
        raise HTTPException(status_code=400,detail="there is not data")
    try:
        return instance_agent.create_agent(data)
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")
    

@agent_router.get("")
def all_agents():
    logger.info("getT / all agents")

    try:
        return instance_agent.get_all_agents()
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")
    


@agent_router.get("/{id}")
def agent_by_id(id:int):
    logger.info("getT / get agent by id")
    if not id:
        raise HTTPException(status_code=400,detail="there is not id")
    try:

        return instance_agent.get_agent_by_id(id)
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")


@agent_router.put("/{id}")
def update_agent_by_id(id:int,data:dict):
    logger.info("put / update_agent_by_id")
    if not id:
        raise HTTPException(status_code=400,detail="there is not id")
    try:
        return instance_agent.update_agent(id,data)
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")



@agent_router.put("/{id}/deactivate")
def deactivate_agent_by_id(id:int):
    logger.info("put / deactivate_agent_by_id")
    if not id:
        raise HTTPException(status_code=400,detail="there is not id")
    try:
        return instance_agent.deactivate_agent(id)
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")


@agent_router.get("/{id}/performance")
def agent_performance_by_id(id:int):
    logger.info("put / agent_performance_by_id")
    if not id:
        raise HTTPException(status_code=400,detail="there is not id")
    try:
        return instance_agent.get_agent_performance(id)
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")