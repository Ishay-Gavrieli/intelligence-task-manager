from fastapi import APIRouter
from database.mission_db import MissionDB

instance_missions = MissionDB()

misions_router = APIRouter()


@misions_router.post("")
def create_mission(data:dict):
    return instance_missions.create_mission(data)


@misions_router.get("")
def all_missions():
    return instance_missions.get_all_missions()


@misions_router.get("/{id}")
def mission_by_id(id:int):
    return instance_missions.get_mission_by_id(id)



@misions_router.put("/{id}/assign/{agent_id}")
def assign_mission(m_id:int,a_id:int):
    return instance_missions.assign_mission(m_id,a_id)



@misions_router.put("/{id}/start")
def start_mission(id:int):
    return instance_missions.update_mission_status(id,status="IN_PROGRESS")



@misions_router.put("/{id}/complete")
def end_succesfuly_mission(id:int):
    return instance_missions.update_mission_status(id,status="COMPLETED")


@misions_router.put("/{id}/fail")
def end_failed_mission(id:int):
    return instance_missions.update_mission_status(id,status="FAILED")

@misions_router.put("/{id}/cancel")
def canceled_mission(id:int):
    return instance_missions.update_mission_status(id,status="CANCELED")