from fastapi import FastAPI, Body
from classes import Task

app = FastAPI()



@app.post("/tasks")
async def create_task(task: Task):
    return {"task": task.task, "completed": task.completed}


@app.get("/tasks")
async def read_tasks():
    return [{"task": "Task 1", "completed": False}, {"task": "Task 2", "completed": True}]


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    return {"task_id": task_id, "task": task.task, "completed": task.completed}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return {"task_id": task_id}
