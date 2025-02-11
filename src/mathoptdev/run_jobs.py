import pydantic 
from .send_request import send_request

class RunJobsRequest(pydantic.BaseModel):
    job_ids: list[str]

def run_jobs(request: RunJobsRequest) -> dict:
    body = {
        "action": "run_jobs",
        "job_ids": request.job_ids  
    }
    return send_request(body)