import obd

connection = obd.OBD()  # auto-connects to USB or RF port

c = obd.commands.RPM  # select an OBD command (sensor)

response = connection.query(c)  # send the command, and parse the response
print(response.value)

connection.close()
