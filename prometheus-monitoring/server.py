from flask import Flask
from prometheus_client import Counter
from prometheus_client import make_wsgi_app 
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)
#                        a metric name,     description about metric
request_count = Counter('http_requests_total', 'HTTP requests count')

@app.route('/ping')
def response():
    request_count.inc() #built in functio which will increase counter value on each http request to this endpoint
    return 'pong\n'

#Creating a '/metrics' endpoint from here prometheus scraper will scrape metrics
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {'/metrics': make_wsgi_app()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)