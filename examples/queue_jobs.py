import mathoptdev as opt
from mathoptdev.types import QueueJobsRequest

jobs_data = opt.queries.get_jobs()
jobs = jobs_data['jobs']

pending_jobs = [job for job in jobs if job['status'] == 'PENDING']

print(f"Found {len(pending_jobs)} pending jobs")

request = QueueJobsRequest(job_ids=[job['id'] for job in pending_jobs])
response = opt.queue_jobs(request)
opt.pretty_log(response)