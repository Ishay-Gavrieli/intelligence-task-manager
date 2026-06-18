from fastapi import APIRouter,HTTPException
from database.mission_db import MissionDB
from logs.basic_log import logger

instance_missions = MissionDB()

misions_router = APIRouter()


@misions_router.post("")
def create_mission(data:dict):
    logger.info("POST /create_mission")
    try:
        result = instance_missions.create_mission(data)
        if result:
            logger.info("success to create mission")
            return result
        logger.error(f"failde to create mission")
        raise HTTPException(status_code=400,detail="bad data")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")


@misions_router.get("")
def all_missions():
    logger.info("get /all_missions")
    try:
        result = instance_missions.get_all_missions()
        if result:
            logger.info("success to get all_missions")
            return result
        logger.error(f"failde to get all_missions")
        raise HTTPException(status_code=400,detail="bad data")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")



@misions_router.get("/{id}")
def mission_by_id(id:int):
    logger.info("get /mission_by_id")
    try:
        result = instance_missions.get_mission_by_id(id)
        if result:
            logger.info("success to get mission_by_id")
            return result
        logger.error(f"failde to get mission_by_id")
        raise HTTPException(status_code=400,detail="bad data")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")
    



@misions_router.put("/{id}/assign/{agent_id}")
def assign_mission(id:int,agent_id:int):
    logger.info("get /assign_mission")
    try:
        result =  instance_missions.assign_mission(id,agent_id)
        if result:
            logger.info("success to assign_mission")
            return result
        logger.error(f"failde to assign_mission")
        raise HTTPException(status_code=400,detail="bad data")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")
    
    



@misions_router.put("/{id}/start")
def start_mission(id:int):
    logger.info("get /start_mission")
    try:
        result = instance_missions.update_mission_status(id,status="IN_PROGRESS")
        if result:
            logger.info("success to start_mission")
            return result
        logger.error(f"failde to start_mission")
        raise HTTPException(status_code=400,detail="bad data")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")
    



@misions_router.put("/{id}/complete")
def end_succesfuly_mission(id:int):
    logger.info("get /end_succesfuly_mission")
    try:
        result = instance_missions.update_mission_status(id,status="COMPLETED")
        if result:
            logger.info("end_succesfuly_mission")
            return result
        logger.error(f"failde to end_succesfuly_mission")
        raise HTTPException(status_code=400,detail="bad data")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")
    


@misions_router.put("/{id}/fail")
def end_failed_mission(id:int):
    logger.info("get /end_failed_mission")
    try:
        result = instance_missions.update_mission_status(id,status="FAILED")
        if result:
            logger.info("end_failed_mission")
            return result
        logger.error(f"failde to end_failed_mission")
        raise HTTPException(status_code=400,detail="bad data")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")
    
    

@misions_router.put("/{id}/cancel")
def canceled_mission(id:int):
    logger.info("get /canceled_mission")
    try:
        result = instance_missions.update_mission_status(id,status="CANCELED")
        if result:
            logger.info("success to canceled_mission")
            return result
        logger.error(f"failde to canceled_mission")
        raise HTTPException(status_code=400,detail="bad data")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"error{e}")
        raise HTTPException(status_code=500,detail="internal server error")
    
    