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

3. Levanta todo con docker-compose
    docker compose up --build

4. Abre en tu navegador
    - http://localhost:8000/ → mensaje inicial

- http://localhost:8000/status → estado de la BD

- http://localhost:8000/apikey → muestra tu API_KEY

- http://localhost:8000/docs → documentación interactiva de FastAPI