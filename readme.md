### Node services for traefik-router

#### Настройка
* 7080 - стандартный порт прокси-сервера, меняется в traefik.toml
* 7081 - стандартный порт api конфигуратора, меняется в uwsgi.ini

#### Запуск
`# conda env create -f env.yml -n router`
`# activate router`
`# nohup uwsgi --ini uwsgi.ini & disown`
`# nohup ./traefik -c traefik.conf`
