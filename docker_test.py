#git token - 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
import docker
client = docker.APIClient(base_url='unix://var/run/docker.sock')
AUTH_CODE = {'username':'inspector007','password':'Deep@1234'}
try:
	client.login(username="inspector007",password="Deep@1234",registry="https://index.docker.io/v1/")
	import pdb;pdb.set_trace()
	container = client.create_container('inspector007/hello-world-testing1:0.9', detach=True)
	response_text = client.commit(container=container,repository="inspector007/hello-world-testing1:0.9",tag='0.10')
	print(response_text)
	client.push(repository='inspector007/hello-world-testing1:0.9',tag='0.10',auth_config = AUTH_CODE)
except Exception as e:
	print(f'error occured {e}')

