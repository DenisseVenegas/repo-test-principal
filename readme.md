Este repositorio permite levantar la aplicación Wisecore junto con su base de datos PostgreSQL usando Docker Compose.  
La aplicación backend se obtiene automáticamente desde DockerHub y siempre está actualizada.

## Requisitos
- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/)

# Cómo levantar la app

1. Clona este repositorio:
   ```bash
   git clone https://github.com/DenisseVenegas/repo-test-principal
   cd repo-test-principal

2. Copia el archivo .env y edítalo si quieres cambiar credenciales:
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_DB=testdb
    API_KEY=your_api_key_here

3. Descarga la última versión de las imágenes
    docker compose pull

4. Levanta todo con docker-compose
    docker compose up --build

5. Abre en tu navegador
    - http://localhost:8000/ → mensaje inicial

    - http://localhost:8000/status → estado de la BD

    - http://localhost:8000/apikey → muestra tu API_KEY

    - http://localhost:8000/docs → documentación interactiva de FastAPI

## Cómo detener los contenedores

docker compose down -v

## Notas

El backend se obtiene desde la imagen DockerHub:
denissevm/repo-test-backend:latest

Cada vez que se actualiza el código en el repo backend, la imagen se reconstruye automáticamente con GitHub Actions y se publica en DockerHub.

Para asegurarte de usar la última versión, ejecuta siempre:
    docker compose pull
