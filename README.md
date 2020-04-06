
#How to use

Install docker

pip3 install docker-compose

change password in the stack.yml file

docker-compose up -f stack.yml -d

Admin panel available at http://localhost:8080


Run command docker ps and sae the container id or names such as mysql-container_db_1

To run mysql commands use command: docker exec -it mysql-container_db_1  bash

In bash run command mysql -p 


