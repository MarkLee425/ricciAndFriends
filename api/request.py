import http.client
import json

async def httpRequest(url: str, method: str, apikey: str, body) -> str:
    connection = await http.client.HTTPConnection("developers.cathaypacific.com")
    body = {
        
    }
    connection.request(method.upper(), url, headers= {apikey}, body=json.dumps(body))
    response = await connection.getresponse()
    data = await response.read()
    return data.decode("utf-8")