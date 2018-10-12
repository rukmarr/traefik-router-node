### Node services for traefik-router

#### usage:

`sudo docker build -t config_api .`

`sudo docker run -d -v traefik:/etc/traefik --name traefik_config -p 8081:80 config_api`  
`sudo docker run -d -v traefik:/etc/traefik --name traefik_server -p 8080:8080 traefik`  

* 8080 is default routing port
* 8081 is default configuration port
