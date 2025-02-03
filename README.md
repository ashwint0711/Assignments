# Assignments Repository

This repository contains three assignments:
1. CORS
2. API thorughput logging
3. Prometheus monitoring

# CORS (Cross-Origin Resource Sharing)
### Description

This assignment demonstrates CORS policies by implementing servers in `python` and `Go` that restrict or allow specific origins. And only works for GET requests. It includes handling preflight requests when custom headers are used.

### Installation & Setup

Running Python Server
> cd CORS/cors-python/
> python3 data-server.py

Running the Client for Python data server
> cd CORS/cors-python/
> python3 -m http.server 7000

Running Go server
> cd CORS/cors-go/cmd/server
> go build data-server.go
> ./data-server


Running the Client for Go data server
> cd CORS/cors-go/static
> python3 -m http.server 9000

---

# API Throughput Logging (Using a Middleware)

### Description
In this assignment i ran two python servers one is `ping-pong-flask.py` and second one is `ping-pong-no-flask.py`, in this i aimed to see what difference it makes if we don't use Flask library for creating a server.
I ran these two python servers in a docker container along with a middleware script also in another docker container, I sent 20-20 requests to both servers one after another, and logged their throughput on the container log which includes:
* Total requests
* Successful responses
* Failed responses
* Total time taken to run 20 requests
* Average time taken by each request

### Installation & Setup
As this assignment contains pushing more than one file to the docker so i used `Docker-Compose` to simplyfy the process of installation.

> cd api-throughput
> docker-compose up --build

This will create 3 containers 2 running python server and one running middleware script.
After running the `docker-compose` command the middleware script will make http requests to both the servers and will print the throughput of servers onto log of container.

---

# Prometheus Monitoring
### Description

Wrote a simple ping-pong server with `/metrics` endpoint open for scraping metrics from the server, to achieve this in python i used pythons built-in `prometheus_client` library, and the `Make_wsgi_app()` to open the `/metrics` endpoint from where prometheus's scraper will scrape metrics.</br>
I followed a structure where `Python server`, `Prometheus` and `Grafana`, all are running in separate docker containers following the 'One Task Per container' approach of Docker.</br>
In this server I created a metrics named `http_requests_total` using the `Counter` class provided by `prometheus_client` library, which will tell the total number of HTTP requests made to this server.

### Installation & Steup
#### Start Python Server, Prometheus and Grafana in Docker
> cd prometheus-monitoring

> docker build -t prom-testing-image .

> docker run -d --name=docker-testing-container -p 8000:8000 prom-testing-image

> docker run -d --name=prometheus -p 9090:9090 bitnami/prometheus

> docker run -d --name=grafana -p 3000:3000 grafana/grafana

#### Access Prometheus UI
Open: http://localhost:9090

On this webpage there will be scraped metrics in text format.

#### Access Grafana UI
Open: http://localhost:3000
 * Default login (id / password): admin, admin
 * Go to connections and Add new connection
 * Select prometheus
 * Give URL : http://localhost:9090 (From this URL grafana will scrape Metrics of our server)


#### Checking Metrics through Grafana Dashboard
The metric i've made is `total_http_requests`, so to check total number of HTTP requests, `prometheus_total_http_requests` query can be used inside Grafana, this will show total number of requests in a time series data format under the `table-view` section.
