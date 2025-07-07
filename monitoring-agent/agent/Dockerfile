FROM python:3.10-slim

WORKDIR /app
COPY agent.py .

# Instala o ping e dependências
RUN apt-get update && apt-get install -y iputils-ping && \
    pip install requests psycopg2-binary


CMD ["python", "agent.py"]