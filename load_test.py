import asyncio
import aiohttp
import matplotlib.pyplot as plt

# Defining the number of requests and server instances
NUM_REQUESTS = 10000
NUM_SERVERS = 3

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def run_load_test():
    url = "http://localhost:5000/{path}}"
    request_counts = [0] * NUM_SERVERS
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(NUM_REQUESTS):
            tasks.append(fetch(session, url))
        
        responses = await asyncio.gather(*tasks)
        
        for response in responses:
            for i in range(NUM_SERVERS):
                if f"Server: {i+1}" in response:
                    request_counts[i] += 1
                    break
    
    # Plot the results
    servers = [f"Server {i+1}" for i in range(NUM_SERVERS)]
    plt.bar(servers, request_counts)
    plt.xlabel('Server Instances')
    plt.ylabel('Number of Requests Handled')
    plt.title('Requests Handled by Each Server Instance')
    plt.show()

# Run the load test
asyncio.run(run_load_test())
