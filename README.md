# mathoptdev

Python CLI and SDK for mathopt.dev the platform for mathematical optimization. 

This provides a set of tools to solve combinatorial problems formulated as MPS files in the cloud. 


# Installation 

Install with pip
```
pip install mathoptdev
```
Install with uv (recommended package manager): 
```
uv add mathoptdev 
```
This installs a CLI that you can call with 
```
opt --help 
```
or 

```
uv run opt --help 
```
if you use uv. 
# Login 
This command will guide you through the login process. 
```
opt login 
```
We store the api token in the variable MATHOPT_API_TOKEN in your .env file. 

After logging in, check the user with 
```
opt user 
```

# Create problem instances 
To get you stated, we provide a helper command to generate Travelling Sallesman Problems (TSP). 

```
opt tsp -c 5 
```
where the option `-c` corresponds to the number of cities in the problem. The MPS file is saved in the tsp folder in the current directory. 

After generating a few instances, upload them to the server with the following command: 
```
opt instance create tsp 
```
You can query the database with 
```
opt instance list 
```
or 

```
import mathoptdev as opt 
opt.queries.get_instances() 
```
to verify if we successfully processed your instances. 

# Solve instances 
To solve an instance, you need to provide its id and the id of the strategy you want to use to solve it. 

See the following example: 
[examples/create_jobs.py](examples/create_jobs.py)
