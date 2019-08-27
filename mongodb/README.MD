https://hub.docker.com/_/mongo

## How to use this image
Start a mongo server instance
$ docker run --name some-mongo -d mongo:tag
... where some-mongo is the name you want to assign to your container and tag is the tag specifying the MongoDB version you want. See the list above for relevant tags.

## Connect to MongoDB from another Docker container
The MongoDB server in the image listens on the standard MongoDB port, 27017, so connecting via Docker networks will be the same as connecting to a remote mongod. The following example starts another MongoDB container instance and runs the mongo command line client against the original MongoDB container from the example above, allowing you to execute MongoDB statements against your database instance:

$ docker run -it --network some-network --rm mongo mongo --host some-mongo test
... where some-mongo is the name of your original mongo container.

... via docker stack deploy or docker-compose
Example stack.yml for mongo:

# Use root/example as user/password credentials
version: '3.1'

services:

  mongo:
    image: mongo
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: example
Try in PWD

Run docker stack deploy -c stack.yml mongo (or docker-compose -f stack.yml up), wait for it to initialize completely, and visit http://swarm-ip:8081, http://localhost:8081, or http://host-ip:8081 (as appropriate).

Container shell access and viewing MongoDB logs
The docker exec command allows you to run commands inside a Docker container. The following command line will give you a bash shell inside your mongo container:

$ docker exec -it some-mongo bash
The MongoDB Server log is available through Docker's container log:

$ docker logs some-mongo