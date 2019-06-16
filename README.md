# Proyecto de creación de tickets

## Requerimientos
* Docker (docker-compose)

## Ejecución
Entrar a la imagen docker
```shell
docker exec -it tickets-system_web_1 /bin/bash
```

Instalar paquetes
```shell
pip install -r requirements.txt
```

Ejecutar migraciones
```shell
python manage.py migrate
```

Ejecutar servidor
```shell
python manage.py runserver 0.0.0.0:8001
```

## ¿Cómo funciona?

**Creación de tickets**
```shell
curl -X POST \
  http://localhost:8001/api/v1/tickets/new/ \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token b530861c818419a500e176d785e130a165a9a23e' \
  -d '{
	"title": "test",
	"description": "This is a test."
}'
```

**Listar todos los tickets**
```shell
curl -X GET \
  http://localhost:8001/api/v1/tickets/list/ \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token b530861c818419a500e176d785e130a165a9a23e' \
```

**Generación de token para usuario**
```shell
curl -X POST \
  http://localhost:8001/api-token-auth/ \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "admin",
	"password": "admin123"
}'
```

**Información de un usuario**
```shell
curl -X POST \
  http://localhost:8001/api/v1/users/detail/ \
  -H 'Authorization: token b530861c818419a500e176d785e130a165a9a23e' \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "admin"
}'
```

## TODO
Implementación de _front end_
