# Compostech MVP — Backend Flask + MQTT

MVP de monitoramento de compostagem com ingestão via MQTT (ESP32) e dashboard web em Flask, focado em temperatura, umidade, pH, gás e alertas, com polling simples no frontend.

## Arquitetura (MVP)
- Firmware (ESP32) publica telemetria a cada ~3s em `compostech/{deviceId}/data/{sensorType}` e alertas em `compostech/{deviceId}/alert/{type}`.
- Backend Flask assina os tópicos, mantém o último snapshot em memória (thread-safe) e expõe API REST + dashboard.
- Dashboard HTML/JS realiza polling de `/api/sensordata` a cada 5s.

## Rodando local
```bash
cp .env.example .env
make dev
# Acesse http://localhost:5000

🚀 INSTRUÇÕES DE IMPLANTAÇÃO
Crie a estrutura de pastas conforme diagrama acima

Copie cada arquivo para seu respectivo caminho

Execute localmente:

bash
cp .env.example .env
make dev
Ou via Docker:

bash
docker compose up --build
Acesse: http://localhost:5000

O MVP está totalmente funcional com:

✅ Backend Flask + MQTT thread-safe

✅ Dashboard com polling automático

✅ Sistema de alertas em tempo real

✅ Configuração Docker completa

✅ CI/CD com GitHub Actions

✅ Firmware ESP32 de exemplo

✅ Documentação completa