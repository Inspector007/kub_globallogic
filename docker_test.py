#git token - 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
import docker
client = docker.APIClient(base_url='unix://var/run/docker.sock')
AUTH_CODE = {'username':'inspector007','password':'Deep@1234'}
try:
	client.login(username="inspector007",password="Deep@1234",registry="https://index.docker.io/v1/")
	client.push(repository='inspector007/hello-world-testing1',tag='0.4',auth_config = AUTH_CODE)
except Exception as e:
	print(f'error occured {e}')
