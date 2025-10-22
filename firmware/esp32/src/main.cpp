// Exemplo ilustrativo (PlatformIO/Arduino)
#include <Arduino.h>

unsigned long last = 0;
const unsigned long INTERVAL = 3000;

void setup() {
  // WiFi.begin(...); mqtt.connect(...);
}

void publish(const char* sensor, float value) {
  // String topic = "compostech/" + deviceId + "/data/" + sensor;
  // mqtt.publish(topic.c_str(), String(value).c_str());
}

void loop() {
  unsigned long now = millis();
  if (now - last >= INTERVAL) {
    last = now;
    float t = 60.0; // leitura sensor
    float h = 50.0;
    float p = 7.2;
    int g = 10;

    publish("temperature", t);
    publish("humidity", h);
    publish("ph", p);
    // mqtt.publish(".../data/gas", String(g).c_str());

    if (g > 30) {
      // mqtt.publish(".../alert/odor", "High odor");
    }
  }
  // mqtt.loop();
}