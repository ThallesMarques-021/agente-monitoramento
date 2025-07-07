# 🌐 Web Monitor Agent

Agente de monitoramento de rede em container Docker que realiza testes de ping e HTTP em sites específicos, armazena os dados no MongoDB e exibe dashboards no Grafana.

---

## 📦 Funcionalidades

- 🔁 Ping para medir latência (RTT) e perda de pacotes
- 🌐 Verificação de tempo de carregamento e códigos HTTP de:
  - google.com
  - youtube.com
  - rnp.br
- 🗃️ Armazenamento dos dados em MongoDB
- 📊 Visualização dos dados em dashboards do Grafana

---

## 🧰 Tecnologias Utilizadas

| Componente       | Tecnologia         |
|------------------|--------------------|
| Agente           | Python + Docker    |
| Banco de Dados   | MongoDB            |
| Visualização     | Grafana            |
| Orquestração     | Docker Compose     |

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   https://github.com/ThallesMarques-021/agente-monitoramento
   cd web-monitor-agent
  docker-compose up -d

Acesse o Grafana:

URL: http://localhost:3000

Usuário: admin

Senha: admin


