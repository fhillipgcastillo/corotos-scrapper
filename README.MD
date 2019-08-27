

## Build
docker build -t fhillip/python3-beautifulsoup:master -t fhillip/python3-beautifulsoup:latest .

## Pull
docker pull fhillip/python3-beautifulsoup

## Run
docker run -it --name NAME USERNAME/IMAGE:FLAG SCRIPT

### simple run
docker run -it --name scrapperbs fhillip/python3-beautifulsoup:master python main.py
### running trying to copy files/direcory to project and keep it syncronize
docker run -it --rm --name scrapperbs -v "$PWD"/scrapperbs:/usr/src/scrapperbs fhillip/python3-beautifulsoup:master python main.py

## Copy files for image (fix problem to windows Home)
if you are running docker at Windows Home and are having issues with Dockerfile to copy the script files use the follow command to copy them manually

docker cp ./scrapperbs/*.py CONTAINER:/usr/src/scrapperbs

## To exit a running container/image
press CTRL + P, CTRL + Q, using both combination together

## Visualize running containers
docker ps
or
docker container ps -a

### see all docker container
docker ps -a
or
docker container ps -a

## Re-attach or Re-stablish connection
docker exec -it CONTAINER_ID CONTAINER_SCRIPT

## run command on the machin visualizing from outside of the container
docker exec -it CONTAINER_NAME COMMAND

## MOngo
Start a mongo server instance
$ docker run --name some-mongo -d mongo:tag
... where some-mongo is the name you want to assign to your container and tag is the tag specifying the MongoDB version you want. See the list above for relevant tags.

### Use mongo and mongo-express
* configure the mongo-composer.yml
* then run:
* * docker-compose.exe -f mongo-composer.yml up

tini -- /docker-entrypoint.sh
-- /docker-entrypoint.sh mongo-express