import mathoptdev as opt 
from mathoptdev import pretty_log as print
import time
from mathoptdev.types import CreateJobsRequest, InstanceStrategyPair, QueueJobsRequest

def get_job_by_id(job_id):
    jobs = opt.queries.get_jobs()
    jobs = jobs['jobs']
    job = next((job for job in jobs if job['id'] == job_id), None)
    return job

def create_single_job(): 
    instance_data = opt.queries.get_instances()
    instance = instance_data['instances'][0]
    strategy_data = opt.queries.get_strategies()
    strategy = strategy_data['strategies'][0]
    print(f"Creating job with instance {instance['id']} and strategy {strategy['id']}")
    request = CreateJobsRequest(instance_strategy_pairs=[InstanceStrategyPair(instance_id=instance['id'], strategy_id=strategy['id'])])
    response = opt.create_jobs(request)
    jobs = response['jobs']
    job_id = jobs[0]['id']
    print(f"Job created with id {job_id}")
    request = QueueJobsRequest(job_ids=[job_id])
    response = opt.queue_jobs(request)
    print(response)
    job = get_job_by_id(job_id)
    start_time = time.time()
    while job['status'] != 'COMPLETED':
        time.sleep(1)
        job = get_job_by_id(job_id)
        print(job)
    end_time = time.time()
    print(f"Job completed with status {job['status']}")
    print(f"Time taken: {end_time - start_time} seconds")
    return response

def print_all(): 
    print(opt.queries.get_user())
    print(opt.queries.get_instances())
    # print(opt.queries.get_strategies())

def main():
    print_all() 
    create_single_job() 

if __name__ == "__main__":
    main()
