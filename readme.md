# 1. Container Image Creation
## 1.2 App coding in Python (app.py) within app folder
    ```
    from flask import Flask
    import os
    import socket

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        html = ('<h2 style="font-family: Consolas, monaco, monospace">' +
                '    Hello from Flask, {name}! (Python)' +
                '</h2>' +
                '<h3 style="font-family: Consolas, monaco, monospace">' +
                '    Hostname:' +
                '</h3>' +
                '<h3 style="font-family: Consolas, monaco, monospace">' +
                '    {hostname}' +
                '</h3>')
        return html.format(name=os.getenv("NAME", "World"), hostname=socket.gethostname())

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=int("5000"), debug=True)
    ```

## 1.3 Create Dockerfile on root Workspace
    ```
    FROM python:3.9-slim-buster
    WORKDIR /
    COPY app .
    RUN pip3 install Flask
    EXPOSE 5000
    ENV NAME "Tech Beer Team"
    CMD [ "python3", "app.py" ]
    ```

## 1.4 Image creation
```
docker build -t helloapp-py .
```

## 1.5 Run a new container
```
docker run --rm -dp 80:5000 helloapp-py:latest
```

## 1.6 Test new container in web browser
http://localhost

## 1.7 Create OCIR repository on OCI
repo_name: project01/helloapp-py
image_path: <region-key>/<namespace>/project01/helloapp-py:v1

## 1.8 Connect to the new OCIR repository
```
docker login <region-key>
username: <namespace>/oracleidentitycloudservice/<username>
pass (Auth-Token): <auth-token>
```

## 1.9 Change the image tag to create a copy image
## 1.10 docker tag <source-image>:<tag> <new-image-path>:<tag>
```
docker tag helloapp-py <region-key>/<namespace>/project01/hello-py-app:v1
```

## 1.11 Push that copy into the OCIR repository on OCI
```
docker push <region-key>/<namespace>/project01/hello-py-app:v1
```

# 2 Run the container on an OCI compute instance
# 2.1 Connect to the OCI instance via SSH
```
ssh opc@<instance-ip> -i sshkey
```

# 2.2 Login to the container image registry
```
docker login <region-key>
username: <namespace>/oracleidentitycloudservice/<username>
pass (Auth-Token): <auth-token>
```

# 2.3 Pull image from an OCI instance (From terminal instance)
```
docker pull <region-key>/<namespace>/project01/hello-py-app:v1
docker images
```

# 2.4 Run a new container from the pulled image
```
sudo docker run --rm -p 80:5000 <region-key>/<namespace>/project01/hello-py-app:v1
```

# 2.5 Test new container on OCI instance in web browser
http://<oci-instance-ip>