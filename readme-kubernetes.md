## 1. Deploy container on an OKE cluster
### 1.1 Check for all nodes inside the OKE cluster
```
kubectl get nodes
```

### 1.2 Check for all namespaces inside the OKE cluster
```
kubectl get ns
```

### 1.3 Create ns-test namespace inside OKE cluster
```
kubectl create ns ns-test
```

### 1.3 Create secret inside OKE cluster in order to connet to container registry
```
kubectl -n ns-test create secret docker-registry my-ocirsecret --docker-server=<region-key> --docker-username='<namespace>/<username>' --docker-password='<auth-token>' --docker-email='user-email'
```

### 1.4 Check for all secrets in the current namespace
kubectl -n ns-test get secrets

### 1.5 Create the deployment YAML file (app-deployment.yaml) with following text
    ```
    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: helloapp-py
    spec:
    selector:
        matchLabels:
        app: helloapp-py
    replicas: 3
    template:
        metadata:
        labels:
            app: helloapp-py
        spec:
        containers:
        - name: helloapp-py
            image: <region-key>/<namespace>/project01/helloapp-py:v1
            imagePullPolicy: Always
            ports:
            - name: python-app
            containerPort: 5000
            protocol: TCP
        imagePullSecrets:
            - name: my-ocirsecret
    ```
### 1.6 Create the Deployment object for the helloapp-py
kubectl -n ns-test apply -f app-deployment.yaml

### 1.7 List the deployments inside the current namespace
kubectl -n ns-test get deployments

### 1.8 Create the service YAML file (svc-deployment.yaml) with following test
    ```
    apiVersion: v1
    kind: Service
    metadata:
    name: helloapp-py-lb
    labels:
        app: helloapp-py
    annotations:
        oci.oraclecloud.com/load-balancer-type: "lb"
        service.beta.kubernetes.io/oci-load-balancer-shape: "flexible"
        service.beta.kubernetes.io/oci-load-balancer-shape-flex-min: "10"
        service.beta.kubernetes.io/oci-load-balancer-shape-flex-max: "10"
    spec:
    type: LoadBalancer
    ports:
    - port: 5000
    selector:
        app: helloapp-py
    ```

### 1.9 Create the Service object for the svc-helloapp-py
```
kubectl -n ns-test apply -f svc-deployment.yaml
```

### 1.10 List the deployments inside the current namespace
```
kubectl -n ns-test get svc
```

### 1.11 See the details of the new Service
```
kubectl -n ns-test describe svc helloapp-py-lb
```

### 1.12 Test new deployment on OKE cluster in web browser
```
http://<load-balancer-ip>:5000
```