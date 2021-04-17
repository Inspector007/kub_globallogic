
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
    # list_of_method_corev1api = [func for func in dir(core_v1) if callable(getattr(core_v1, func))]
    list_of_method_corev1api_final = list(map(lambda b:b[0],list_of_method_corev1api))
    print(f'{list_of_method_corev1api_final}')
    print(f'Total count of method is :{len(list_of_method_corev1api_final)}')


if __name__ == '__main__':
    # main()
    list_of_all_method_from_corev1api()