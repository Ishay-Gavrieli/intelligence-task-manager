from fastapi import APIRouter
from database.agent_db import AgentDB

instance_agent = AgentDB()

agent_router = APIRouter()


@agent_router.post("")
def create_agent(data:dict):
    return instance_agent.create_agent(data)


@agent_router.get("")
def all_agents():
    return instance_agent.get_all_agents()


@agent_router.get("/{id}")
def agent_by_id(id:int):
    return instance_agent.get_agent_by_id(id)



@agent_router.put("/{id}")
def update_agent_by_id(id:int,data:dict):
    return instance_agent.update_agent(id,data)



@agent_router.put("/{id}/deactivate")
def deactivate_agent_by_id(id:int):
    return instance_agent.deactivate_agent(id)


@agent_router.get("/{id}/performance")
def agent_performance_by_id(id:int):
    return instance_agent.get_agent_performance(id)