from fastapi import APIRouter,HTTPException
from database.agent_db import AgentDB
from logs.basic_log import logger

instance_agent = AgentDB()

agent_router = APIRouter()


@agent_router.post("")
def create_agent(data:dict):
    logger.info("POST /agents called")

    try:
        result = instance_agent.create_agent(data)
        if result:
            logger.info("success to create agent")
            return result
        logger.error(f"failde to create agent")
        raise HTTPException(status_code=400,detail="bad data")
    

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")
    

@agent_router.get("")
def all_agents():
    logger.info("get / all agents")

    try:
        result = instance_agent.get_all_agents()
        if result:
            logger.info("success to get all agents")
            return result
        logger.error(f"failde to get all agents")
        raise HTTPException(status_code=400,detail="failed")
      
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")
    


@agent_router.get("/{id}")
def agent_by_id(id:int):
    logger.info("get / get agent by id")
    try:
        result = instance_agent.get_agent_by_id(id)
        if result:
            logger.info("success to get agent by id ")
            return result
        logger.error(f"failde to get agent")
        raise HTTPException(status_code=400,detail="failed")
      
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")


@agent_router.put("/{id}")
def update_agent_by_id(id:int,data:dict):
    logger.info("put / update_agent_by_id")
 
    try:
        result = instance_agent.update_agent(id,data)
        if result:
            logger.info("success to update agent by id ")
            return result
        logger.error(f"failde to update agent")
        raise HTTPException(status_code=400,detail="failed")
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")



@agent_router.put("/{id}/deactivate")
def deactivate_agent_by_id(id:int):
    logger.info("put / deactivate_agent_by_id")

    try:
        result = instance_agent.deactivate_agent(id)
        if result:
            logger.info("success to deactivate_agent_by_id")
            return result
        logger.error(f"failde to deactivate_agent_by_id")
        raise HTTPException(status_code=400,detail="failed")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")


@agent_router.get("/{id}/performance")
def agent_performance_by_id(id:int):
    logger.info("put / agent_performance_by_id")

    try:
        result = instance_agent.get_agent_performance(id)
        if result:
            logger.info("success to agent_performance_by_id")
            return result
        logger.error(f"failde to agent_performance_by_id")
        raise HTTPException(status_code=400,detail="failed")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")