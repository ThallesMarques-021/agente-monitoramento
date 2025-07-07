# 📡 Agente de Monitoramento Web com Docker, SQLite e Grafana

Este projeto é um agente de monitoramento de sites desenvolvido em Python, containerizado com Docker e visualizado via Grafana. Ele coleta dados como tempo de carregamento e código de status HTTP de páginas web e salva os resultados em um banco de dados SQLite.

---

## ✅ Funcionalidades

- ⏱️ Mede tempo de resposta (latência) de sites configurados
- 📶 Registra códigos de status HTTP (200, 404, etc.)
- 🗃️ Armazena os dados em um banco SQLite 
- 📊 Exibe dashboards via Grafana com plugin SQLite
- 🔁 Coleta executada periodicamente (a cada 60 segundos)
- 🐳 Totalmente baseado em containers com Docker Compose

---

## 🚀 Como executar o projeto

### 1. Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)

### 2. Clonar o repositório

```bash
git clone https://github.com/ThallesMarques-021/agente-monitoramento
cd monitoring-agent

Subir os containers
docker compose up --build

Acessar o Grafana

http://localhost:3000

Login padrão:

Usuário: admin

Senha: admin

monitoring-agent/
├── agent/
│   ├── agent.py                # Script principal de monitoramento
│   └── Dockerfile              # Imagem baseada em python:3.10-slim ou personalizada
├── grafana-custom/
│   └── Dockerfile              # Instala plugin SQLite no Grafana
├── db/                         # Volume persistente do SQLite
│   └── monitor.db              # Criado automaticamente pelo script
├── docker-compose.yml          # Orquestração dos serviços
├── README.md
└── HLD.md                      # Arquitetura e prints (incluso abaixo)


Abaixo, um exemplo real de dashboard em funcionamento no Grafana com dados do agente:

![image](https://github.com/user-attachments/assets/99f39744-7edb-4123-b7fa-5c5a07a7bd3c)

