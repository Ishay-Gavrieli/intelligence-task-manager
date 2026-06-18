# System description:

Intelligence Task Management System The system stores in tables in a database the agent's information, his rank, and the tasks, including the type of task and its difficulty. 
The purpose of the system is to manage all the data from creating an agent, updating an agent, checking whether he is active or not, and checking how many tasks he has, how many have been completed, and how many have not. 
The system needs to add a task to the agent, change his status, count tasks by level, and return general data such as which agent has completed the most tasks. The system needs to route the task level according to the agent's rank.



# The folder structure:

intelligence-task-manager/
├── main.py 
├── database/
│   ├── db_connection.py
│   ├── agent_db.py
│   └── mission_db.py
├── routes/
│  ├── agent_routes.py
│  ├── mission_routes.py
│  └── report_routes.py
├── logs/
│  └── app.log
|  └── basic_log.py
|
├── README.md
├── requirements.txt
└── .gitignore


# Table structure:

## Agent table:
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
specialty VARCHAR(50),
is_active BOOLEAN DEFAULT TRUE,
completed_missions INT DEFAULT 0,
failed_missions INT DEFAULT 0,
agent_rank ENUM("Junior","Senior","Commander")


## missions table:
id INT PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(50),
description VARCHAR(100),
location VARCHAR(50),
difficulty INT CHECK (difficulty  >= 1 AND difficulty <= 10),
importance INT CHECK (importance >= 1 AND importance <= 10),
status VARCHAR(50) DEFAULT "NEW",
risk_level VARCHAR(50),
assigned_agent_id INT NULL



# Explanation of the MissionDB, AgentDB, connection_db classes:

## class connection_db:
The department contains three methods
one: get_connection()
which creates a connection to mysql 
two: create_database()
Creates Intelligence_db if it does not exist
three: creat_table()
which creates the two tables one for the agents and one for the tasks it does not exist


## class AgentDB:
Responsible for all SQL operations against the agents table. It has nine methods.

One: Create Agent(data). A function that creates a new agent and returns the agent object. 
Two: get_all_agents(). A function that returns a list of all agents. 
Three:get_agent_by_id(id). Returns an agent by ID. If not returns NONE. 
Four:update_agent(id, data). Updates an agent. Can update everything except the ID. 
Five:deactivate_agent(id). Updates an inactive agent by ID. 
Six:increment_complete(id). Updates the number of tasks completed by an agent by ID. 
Seven:increment_failed(id). Updates the number of tasks failed by an agent by ID. 
Eight:get_agent_performance(id). Returns a dictionary with the data completed, failed, total, success_rate and calculates the success_rate value in percentages. 
Nine:count_active_agents() Returns the number of active agents.


## class MissionDB:
Responsible for all SQL operations against the missions table.

One: Create_mission(data). Creates a new task and returns the entire object. 
Two: get_all_missions().Returns all tasks.
Three:get_mission_by_id(id). Returns a mission by ID. If not returns NONE.
Four:assign_mission(m_id, a_id).Assigning a task to an agent  
Five:get_open_missions_by_agent(id). returned by an agent ASSIGNED/IN_PROGRESS tasks 
Six:count_all_missions().Total tasks
Seven:count_by_status(status).Counting by a certain status
Eight: count_open_missions().Open task counter.
Nine:count_critical_missions().CRITICAL TASKS COUNTER.
Ten:get_top_agent().Returns the agent with the most completed tasks.


## system rules:
1 rank must be Commander / Senior / Junior — any other value throws an error.
2 difficulty and importance must be between 1 and 10 — otherwise an error.
3 level_risk is calculated automatically when creating a task — the user does not send it.
4 An agent with False=active_is cannot accept tasks.
5 An agent cannot have more than 3 open tasks (PROGRESS_IN / ASSIGNED) at the same time.
6 If CRITICAL=level_risk — only an agent with the Commander rank can accept the task.
7 Only a task with the status NEW can be assigned. After assignment: ASSIGNED=status.
8 Only a task with the status ASSIGNED can be started. After: PROGRESS_IN=status.
9 Only a task can be finished. PROGRESS_IN and changed to completed or failed status
10 Only a task with the status NEW or ASSIGNED can be canceled — otherwise an error



## Running instructions:
docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0
docker exec -it intelligence-mysql mysql -u root -p
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py


