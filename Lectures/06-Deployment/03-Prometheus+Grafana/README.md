## Part 3: Prometheus + Grafana


### Pre-requisities

```shell
pip install prometheus-fastapi-instrumentator
```

### 0. Make some folders

Before anything, let's clean things.  Let's put everything related to the fastapi into a directory called `app`.  In addition, please create a directory named `prometheus` and another directory named `grafana`.

The structure looks like this:

    .github  #for github actions
    app
        ml
        +-- classifier.py
        +-- train.py
        +-- iris_v1.joblib
        schema
        +-- iris.py
        app.py
        Dockerfile
        requirements.txt
    prometheus
        +-- prometheus.yml #will create shortly
    grafana
        +-- datasource.yaml #will create shortly
        +-- config.monitoring #will create shortly
    docker-compose.yaml  #will create shortly

### 1. Expose endpoints for prometheus 

In `app.py`, add the endpoints as

```python
#put this in the beginning
from prometheus_fastapi_instrumentator import Instrumentator 

#you can put this at the last line of the file
Instrumentator().instrument(app).expose(app)  
```

For more details how to use this instrumentator, read https://github.com/trallnag/prometheus-fastapi-instrumentator

### 2. Add prometheus-fastapi-instrumentator to your requirement.txt

Now, my `requirement.txt` looks like this:

    fastapi==0.78.0
    numpy==1.23.1
    scikit_learn==0.24.2
    starlette==0.19.1
    uvicorn==0.18.2
    joblib==0.17.0
    pydantic==1.9.1
    prometheus-fastapi-instrumentator

### 3. Define the configuration - `prometheus.yml` under the directory `prometheus`

```yml
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).
# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"
# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'
    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.
    static_configs:
    - targets: ['localhost:9090']
  - job_name: 'app'
    dns_sd_configs: #automatic service discovery
      - names: ["app"]
        port: 8000
        type: A  #<--DNS A Record
        refresh_interval: 5s
```

For more details:  read https://prometheus.io/docs/prometheus/latest/configuration/configuration/



### 4. Define the docker compose file

Since we now have many services, it is good practice to run all of them together in a docker-compose file.  

Before we create the `docker-compose.yaml` file, let's remove the port number from the `Dockerfile`:

```dockerfile
FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y python3-dev build-essential

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD uvicorn --host 0.0.0.0 app:app
```

Now create a `docker-compose.yaml` as follows:

```yaml
version: "3.8"

services:
  app:
    build: .  #<---simply build the current directory Dockerfile
    restart: unless-stopped
    container_name: app
    ports:
      - 8000:8000
    networks:
      example-network:
        ipv4_address: 172.16.238.10

  prometheus:
    image: prom/prometheus:latest
    restart: unless-stopped
    container_name: prometheus
    ports:
      - 9090:9090
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
    networks:
      example-network:
        ipv4_address: 172.16.238.11

networks: #a common network where all the service resides
  example-network:
    name: example-network
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.16.238.0/24
```

Now that we set up the endpoints and the yml file, let's run the compose file (you don't have to run the Dockerfile first):

```shell
docker compose up
```

### 5. Check whether everything is running fine.

Fast API: Go to http://localhost:8000/docs

Prometheus:  Go to http://localhost:9090

Try put this in the execution box of prometheus:

`http_requests_total`  which will list the total number of requests.

If you want to try other metrics or add custom metrics, see https://github.com/trallnag/prometheus-fastapi-instrumentator

We can shut down all services again:

```shell
docker compose down
```

### 6. Grafana

As you can see, prometheus is not really a good visualizer.  It's more like a metric gatherer.  Grafana is commonly used together with Prometheus.

To set grafana, we have to create two files: the `datasource.yaml` specifying where is the datasource for grafana to visualize, and `config.monitoring` which specifies very basic configurations for grafana like password.

Let's start with the `datasource.yml` under the directory `grafana`.

```yml

# config file version
apiVersion: 1

# list of datasources to insert/update depending
# on what's available in the database
datasources:
  # <string, required> name of the datasource. Required
- name: Prometheus
  # <string, required> datasource type. Required
  type: prometheus
  # <string, required> access mode. direct or proxy. Required
  access: proxy
  # <string> url
  url: http://prometheus:9090

```

Create a `config.monitoring` file inside the grafana directory:

    GF_SECURITY_ADMIN_PASSWORD=pass@123
    GF_USERS_ALLOW_SIGN_UP=false

### 7. Modify the docker compose file to include grafana:

```yaml
version: "3.8"

services:
  app:
    build: ./app  #<---simply build the current directory Dockerfile
    restart: unless-stopped
    container_name: app
    ports:
      - 8000:8000
    networks:
      example-network:
        ipv4_address: 172.16.238.10

  prometheus:
    image: prom/prometheus:latest
    restart: unless-stopped
    container_name: prometheus
    ports:
      - 9090:9090
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
    networks:
      example-network:
        ipv4_address: 172.16.238.11

  grafana:
    image: grafana/grafana:latest
    restart: unless-stopped
    user: "472"  #<--default user ID of grafana
    container_name: grafana
    depends_on:
      - prometheus
    ports:
      - 3000:3000
    volumes:
      - ./grafana/datasource.yaml:/etc/grafana/provisioning/datasources/datasource.yaml
    env_file:
      - ./grafana/config.monitoring
    networks:
      example-network:
        ipv4_address: 172.16.238.12

networks:
  example-network:
    name: example-network
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.16.238.0/24
```

Run

```shell
docker compose up
```

Now, go to http://localhost:3000

username is `admin` and password is `pass@123` as you specified in `config.monitoring`.

Now you can try Explore or Add Dashboard to suit your needs.

What is cool here is that even you restart your docker, all dashboards will still be persisted.

Read more here:  https://grafana.com/tutorials/grafana-fundamentals/?utm_source=grafana_gettingstarted

Next part, we shall deploy to AWS EC2.