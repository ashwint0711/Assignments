import requests
import time

# Server endpoints
servers = [
    {"url": "http://flask-server:5000/ping", "name": "Server 1"},
    {"url": "http://no-flask-server:5001/ping", "name": "Server 2"},
]

def check_server_throughput(server, total_requests):
    success_count = 0
    failure_count = 0

    start_time = time.time()
    
    for i in range(total_requests) : 
        response = requests.get(server["url"], timeout = 2)
        try:
            if response.status_code == 200:
                success_count += 1
            else :
                failure_count += 1
        except requests.excepttions.RequestException as e:
            print(f"Error accessing {server['name']} ({server['url']})")

    end_time = time.time()
    total_time = end_time - start_time
    average_time_per_request = total_time / total_requests


    print(f"{server['name']} Results:")
    print(f"Total Requests : {total_requests}")
    print(f"Successful Responses : {success_count}")
    print(f"Failed Responses : {failure_count}")
    print(f"Total time taken : {total_time:.2f}")
    print(f"Average time per request: {average_time_per_request:.2f}\n")


# Run the throughput check for both servers
if __name__ == "__main__":
    total_requests = 20
    for server in servers:
        check_server_throughput(server, total_requests)
