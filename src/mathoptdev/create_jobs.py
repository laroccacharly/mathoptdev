import pydantic 
from .send_request import send_request

class InstanceStrategyPair(pydantic.BaseModel):
    instance_id: str
    strategy_id: str

class CreateJobsRequest(pydantic.BaseModel):
    instance_strategy_pairs: list[InstanceStrategyPair]

def create_jobs(request: CreateJobsRequest) -> dict:
    pairs = request.instance_strategy_pairs
    body = {
        "action": "create_jobs",
        "instance_strategy_pairs": [
            {
                "instance_id": pair.instance_id,
                "strategy_id": pair.strategy_id
            }
            for pair in pairs
        ]
    }
    return send_request(body)

