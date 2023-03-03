import requests


origem=<ramalorigem>


url='https://app.nuvemfone.com.br/nf-api/v10/clicktocall.php?origem=$origem&destino=<numerodestino>&keyaction=<keyaction>'


response = requests.post(url, verify=False)


print(response.content)


