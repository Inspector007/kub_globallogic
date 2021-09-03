#git token - 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
import docker
from flask import jsonify
client = docker.DockerClient(base_url='unix://var/run/docker.sock')
AUTH_CODE = {'username':'inspector007','password':'Deep@1234'}
try:
	client.login(username="inspector007",password="Deep@1234",registry="https://index.docker.io/v1/")
	import pdb;pdb.set_trace()
	container = None
	try:
		#container = client.containers.run('inspector007/hello-world-testing1:0.9', detach=True)
		for container_obj in client.containers.list(all = True):
			#if container_obj.id == 'e8da7eafe1fb':
			container = container_obj
			break 
	except Exception as e:
		print(f'container exception as {e}')
	try:
		image_created = container.commit(repository="inspector007/hello-world-testing1:0.9",tag='')
	except Exception as e:
		print(f'commit exception as {e}')
	print(image_created)
	client.api.push('inspector007/hello-world-testing1:0.9')
except Exception as e:
	print(f'error occured {e}')

