import requests

#send request
result=requests.get('{url}')

#save file
open('{file}','wb').write(result.content)