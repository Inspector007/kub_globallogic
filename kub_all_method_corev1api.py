
def main():
    from kubernetes import client, config
    # config.load_incluster_config()
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))



def list_of_all_method_from_corev1api():
    # config.load_incluster_config()
    # from kubernetes.client import Configuration
    '''
        Notice that getmembers returns a list of 2-tuples. 
        The first item is the name of the member, 
        the second item is the value.
    '''
    import inspect
    from kubernetes import config
    from kubernetes.client.api import core_v1_api
    config.load_kube_config()
    core_v1 = core_v1_api.CoreV1Api()
    list_of_method_corev1api = inspect.getmembers(core_v1, predicate=inspect.ismethod)
    print(f'Total count of method is :{len(list_of_method_corev1api)}')
    print(f'{list_of_method_corev1api}')


if __name__ == '__main__':
    # main()
    list_of_all_method_from_corev1api()