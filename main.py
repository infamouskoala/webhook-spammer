import requests
import threading

url = input("url: ")
payload = """
```
I like big tits and i cannot lie fr
join us
```
@everyone https://discord.gg/fNfgrsvx
"""

def function():
    requests.post(url,json={'content': payload})

while True:
    t = threading.Thread(target=function)
    t.start()