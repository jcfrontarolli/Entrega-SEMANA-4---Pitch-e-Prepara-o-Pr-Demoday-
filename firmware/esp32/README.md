# Firmware ESP32 — Skeleton MVP

- Publica a cada ~3s nos tópicos `compostech/{deviceId}/data/{sensorType}` (temperature, humidity, ph, gas).
- Publica alertas em `compostech/{deviceId}/alert/{type}` (odor, ph) sob thresholds simples.
- Reconexão automática ao Wi-Fi/MQTT e loop não-bloqueante.