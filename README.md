# kub_globallogic
test kubernates working env

1.       Download python SDK either from github (https://github.com/kubernetes-client/python) or pip install kubernetes

2.       Get the list of all methods exposed by kubernetes for CoreV1Api

3.       Write a program to initialize a pod container

	a.       Container name – <>

	b.       Image to use – <>

4.       Write a program to check if the pod name “interview” is running on namespace "<>" or not, and if not then create it.


Sol - 
 1-  python -m venv kub_env
 2- git clone --recursive https://github.com/kubernetes-client/python.git
 3- cd python
 4- python setup.py install
 5- UserWarning: The version specified ('17.0.0-snapshot') is an invalid version, 
 	this may not work as expected with newer versions of setuptools,pip, and PyPI.
 6- error: supposed package directory 'kubernetes\config' exists, but is not a directory
 7- pip install kubernates
 8- pip install freeze
	Output:
			cachetools==4.2.1
			certifi==2020.12.5
			chardet==4.0.0
			google-auth==1.29.0
			idna==2.10
			kubernetes==12.0.1
			oauthlib==3.1.0
			pyasn1==0.4.8
			pyasn1-modules==0.2.8
			python-dateutil==2.8.1
			PyYAML==5.4.1
			requests==2.25.1
			requests-oauthlib==1.3.0
			rsa==4.7.2
			six==1.15.0
			urllib3==1.26.4
			websocket-client==0.58.0
 9 - gcloud components install kubectl
 10 - sudo apt-get install kubectl
 11 - kubectl version --client
 12 - kubectl cluster-info
 13 -  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
 	   sudo install minikube-linux-amd64 /usr/local/bin/minikube
14 - minikube start
15 - https://minikube.sigs.k8s.io/docs/start/
16 - 
	kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.4
	kubectl expose deployment hello-minikube --type=NodePort --port=8080

	kubectl create deployment globallogic --image=image.globallogic.com/interview
	kubectl expose deployment globallogic --type=NodePort --port=8080

17 - kubectl delete service globallogic
18 - kubectl delete pods <name>
19 - kubectl delete service <name>
20 - kubectl apply -f pod.yaml
21 - kubectl apply -f pod_service.yaml

