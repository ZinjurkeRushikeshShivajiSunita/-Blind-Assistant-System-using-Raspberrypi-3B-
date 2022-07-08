import nexmo
client = nexmo.Client(key='64b6336a',secret='sgQCWqBvMeM2j2co')
client.send_message({'from': 'Nexmo', 'to': '9834535692', 'text': 'Hello world'})