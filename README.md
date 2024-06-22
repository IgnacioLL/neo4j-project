# How to run

This neo4j project runs on top of a docker container. To run the whole project we will have to have the following requirements:
- Install python neo4j client `pip install neo4j`
- Install docker

After this we can run the whole code by running the following commands:

Init container:
- `sudo docker run --name neo4j -p7474:7474 -p7687:7687 -d -v temporal_zone:/var/lib/neo4j/import -e NEO4J_AUTH=neo4j/example-password neo4j`

Where we should modify the given password for a real one in this command and config.py file. 

Copy files into docker container:
- `sudo docker cp temporal_zone neo4j:/var/lib/neo4j/import/`

Run A2: 
- `python PartA2.LLORET_Paulsson/script.py`

Run A3
- `python PartA3.LLORET_Paulsson/script.py`

Run B
- `python PartB.LLORET_Paulsson/script.py`

Run C
- `python PartC.LLORET_Paulsson/script.py`

Run D
- `python PartD.LLORET_Paulsson/script.py`
