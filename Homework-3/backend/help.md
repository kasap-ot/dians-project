**Useful commands:**
- docker-compose build
- docker-compose up
- docker-compose down
- docker-compose run app alembic revision --autogenerate -m "Migration message"
- docker-compose run app alembic upgrade head
- ./venv/Scripts/activate
- pip install package_name
- pip freeze > requirements.txt

On container startup, recreate alembic migrations

**OpenAPI:** localhost:8000/docs;
**pgAdmin:** localhost:5050