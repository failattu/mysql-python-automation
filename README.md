
# How to use

Install docker

pip3 install docker-compose

change password in the stack.yml file

docker-compose -f stack.yml up -d

Admin panel available at http://localhost:8080


Run command docker ps and sae the container id or names such as mysql-container_db_1

To run mysql commands use command: docker exec -it mysql-container_db_1  bash

In bash run command mysql -p 


# How to use my main.py

Change the first 4 values to enable the host, username, password and database to what you need.

pip3 install mysql.connector

python3 main.py

# How to reset the whole environment

Run: docker-compose -f stack.yml down

# I have a CSV or comparable to import

I added a data mount that mounts the folder /data into /data in the mysql database so you can place your files there and run them on the container

