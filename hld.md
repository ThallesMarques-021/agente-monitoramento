markdown
# 🧩 HLD – High-Level Design: Web Monitor Agent

## 🎯 Objetivo

Desenvolver um agente de monitoramento de rede em container Docker que realize testes periódicos de conectividade (ping) e desempenho HTTP (tempo de resposta e códigos de status) em sites específicos. Os dados serão armazenados em um banco de dados e visualizados em dashboards do Grafana.

---

## 🏗️ Arquitetura de Alto Nível

```plaintext
+------------------+       +----------------+       +----------------+
|  Dockerized App  |  -->  |  Banco de Dados|  -->  |     Grafana    |
| (Ping + HTTP)    |       |   (MongoDB)    |       |  (Dashboards)  |
+------------------+       +----------------+       +----------------+
🔄 Fluxo de Dados
O agente executa testes de ping e HTTP periodicamente (a cada minuto).

Os resultados são armazenados no MongoDB com timestamp.

O Grafana se conecta ao MongoDB (via plugin ou exportação) e exibe os dados em dashboards configuráveis.

🧱 Componentes
1. Agente de Monitoramento (Python)
ping_monitor.py: Mede latência e status de conectividade usando ping3.

http_monitor.py: Mede tempo de resposta e códigos HTTP usando requests.

scheduler.py: Agendador que executa os testes periodicamente com schedule.

2. Banco de Dados (MongoDB)
Armazena documentos com os resultados dos testes:

ping: host, latência, status, timestamp

http: host, status_code, tempo de resposta, timestamp

3. Grafana
Visualiza os dados em tempo real.

Dashboards sugeridos:

Latência média por host

Perda de pacotes

Tempo de resposta HTTP

Códigos de status HTTP

⚙️ Tecnologias
Componente	Tecnologia
Linguagem	Python 3.11
Banco de Dados	MongoDB
Visualização	Grafana
Orquestração	Docker Compose
Monitoramento	ping3, requests
Agendamento	schedule (Python)
🔐 Segurança e Resiliência
Containers isolados via Docker

Reinício automático com restart: always

Possibilidade de adicionar autenticação no MongoDB e Grafana

📈 Escalabilidade
Fácil adição de novos hosts monitorados

Possível adaptação para múltiplos agentes em diferentes regiões

Suporte a exportação para bancos SQL ou sistemas de alerta

📌 Considerações Finais
Este projeto é modular, leve e extensível. Pode ser usado para monitoramento interno de redes, verificação de disponibilidade de serviços externos ou como base para soluções mais robustas de observabilidade.
