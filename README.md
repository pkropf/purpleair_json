# purpleair_json
Convert the json from purpleair's api to something more usable

The json returned from purpleair's api is not all that useful for many json tools as there are two arrays within the jason that contain the data, the fields and data arrays. They're a 1-to-1 mirror where the fields provides the names and the data provides the values. Because of this, it's difficult to say something like:

`temperature = json['temperature']`

Here's a sample of the json as received from the api:

`{'version': '7.0.4', 'fields': ['ID', 'pm', 'age', 'pm_0', 'pm_1', 'pm_2', 'pm_3', 'pm_4', 'pm_5', 'pm_6', 'conf', 'pm1', 'pm_10', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'Humidity', 'Temperature', 'Pressure', 'Elevation', 'Type', 'Label', 'Lat', 'Lon', 'Icon', 'isOwner', 'Flags', 'Voc', 'Ozone1', 'Adc', 'CH'], 'data': [[37123, 10.1, 1, 10.1, 8.8, 6.1, 4.9, 4.1, 7.1, 10.6, 100, 6.9, 10.7, 1430.7, 406.0, 56.9, 4.1, 1.0, 0.6, 61, 53, 1021.75, 9, 0, 'Actual Name on Record', 37.850136, -122.29151, 0, 0, 0, None, None, 0.0, 3]], 'count': 1}`

purpleair_json transforms the json to  to:

`{"ID": 37123, "pm": 19.8, "age": 1, "pm_0": 19.8, "pm_1": 21.9, "pm_2": 25.1, "pm_3": 23.6, "pm_4": 12.3, "pm_5": 9.0, "pm_6": 10.7, "conf": 100, "pm1": 13.1, "pm_10": 21.1, "p1": 2378.7, "p2": 692.4, "p3": 125.3, "p4": 8.8, "p5": 1.8, "p6": 0.6, "Humidity": 55, "Temperature": 56, "Pressure": 1027.24, "Elevation": 9, "Type": 0, "Label": "Actual Name on Record", "Lat": 37.850136, "Lon": -122.29151, "Icon": 0, "isOwner": 0, "Flags": 0, "Voc": null, "Ozone1": null, "Adc": 0.0, "CH": 3, "version": "7.0.4"}`

