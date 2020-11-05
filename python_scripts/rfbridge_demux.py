sensors = {
  "3C003A": ["Havelåge", "ON", "false"],
  "C0E3DA": ["Hoveddør", "ON", "false"],
  "791D5A": ["TESTER", "ON", "false"],
  "45400A": ["Dobbelt terrassedør", "ON", "true"],
  "45400E": ["Dobbelt terrassedør", "OFF", "true"],
  "B1C40A": ["Soveværelse vindue", "ON", "true"],
  "B1C40E": ["Soveværelse vindue", "OFF", "true"],
  "AFF70A": ["Pigernes stue vindue", "ON", "true"],
  "AFF70E": ["Pigernes stue vindue", "OFF", "true"],
  "B2B10A": ["Nathalies vindue", "ON", "true"],
  "B2B10E": ["Nathalies vindue", "OFF", "true"],
  "181F0A": ["Cornelies vindue", "ON", "true"],
  "181F0E": ["Cornelies vindue", "OFF", "true"],
  "B0C30A": ["Indgang vindue haven", "ON", "true"],
  "B0C30E": ["Indgang vindue haven", "OFF", "true"],
  "12C40A": ["Indgang vindue vejen", "ON", "true"],
  "12C40E": ["Indgang vindue vejen", "OFF", "true"],
  "16100A": ["Hjaltes vindue haven", "ON", "true"],
  "16100E": ["Hjaltes vindue haven", "OFF", "true"],
  "0D510A": ["Hjaltes vindue vejen", "ON", "true"],
  "0D510E": ["Hjaltes vindue vejen", "OFF", "true"],
  "E1220A": ["Emilios vindue", "ON", "true"],
  "E1220E": ["Emilios vindue", "OFF", "true"],
  "E0DC0A": ["Colins vindue", "ON", "true"],
  "E0DC0E": ["Colins vindue", "OFF", "true"],
  "9B9B0A": ["Studieværelse vindue", "ON", "true"],
  "9B9B0E": ["Studieværelse vindue", "OFF", "true"],
  "E32A0A": ["Lille badeværelse vindue 2", "ON", "true"],
  "E32A0E": ["Lille badeværelse vindue 2", "OFF", "true"],
  "ACB90A": ["Stort badeværelse vindue 3", "ON", "true"],
  "ACB90E": ["Stort badeværelse vindue 3", "OFF", "true"],
  "45B60A": ["Kontor", "ON", "true"],
  "45B60E": ["Kontor", "OFF", "true"],
  "E6100A": ["Stuedør", "ON", "true"],
  "E6100E": ["Stuedør", "OFF", "true"],
  "E46B0A": ["Pigernes indgang", "ON", "true"],
  "E46B0E": ["Pigernes indgang", "OFF", "true"],
  "E2B70A": ["Køkkendør", "ON", "true"],
  "E2B70E": ["Køkkendør", "OFF", "true"],
  "99A10A": ["Stuevindue 1", "ON", "true"],
  "99A10E": ["Stuevindue 1", "OFF", "true"],
  "E2D60A": ["Stuevindue 2", "ON", "true"],
  "E2D60E": ["Stuevindue 2", "OFF", "true"],
  "E5A20A": ["Stuevindue 3", "ON", "true"],
  "E5A20E": ["Stuevindue 3", "OFF", "true"],
  "E5B50A": ["Soveværelsesdør", "ON", "true"],
  "E5B50E": ["Soveværelsesdør", "OFF", "true"]
}

payload = data.get("payload")
 
if payload is not None:
  if payload in sensors.keys():
    service_data = {"topic": "home/{}".format(sensors[payload][0]), "payload":"{}".format(sensors[payload][1]), "qos":0, "retain":"{}".format(sensors[payload][2])}
  else:
    service_data = {"topic":"home/unknown", "payload":"{}".format(payload), "qos":0, "retain":"false"}
    logger.warning("<rfbridge_demux> Received unknown RF command: {}".format(payload))
  hass.services.call("mqtt", "publish", service_data, False)