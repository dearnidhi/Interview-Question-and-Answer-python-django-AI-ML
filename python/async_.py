import asyncio

# Example 1: Simple Async Function
async def simple_async_function():
    print("Start")
    await asyncio.sleep(2)  # Simulate a non-blocking operation
    print("End")

# Run the asynchronous function in an event loop
asyncio.run(simple_async_function())

# Example 2: Concurrent Tasks
async def task_one():
    print("Task One started")
    await asyncio.sleep(5)
    print("Task One completed")

async def task_two():
    print("Task Two started")
    await asyncio.sleep(2)
    print("Task Two completed")

async def main_concurrent_tasks():
    # Run tasks concurrently
    await asyncio.gather(task_one(), task_two())

# Run the main asynchronous function in an event loop
asyncio.run(main_concurrent_tasks())


# Example 3: Asynchronous HTTP Requests
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main_async_http_request():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    data = await fetch_data(url)
    print(f"Data: {data}")

# Run the main asynchronous function in an event loop
asyncio.run(main_async_http_request())


# Example 4: Asynchronous File I/O
async def write_to_file(filename, content):
    async with open(filename, 'w') as file:
        await file.write(content)

async def read_from_file(filename):
    async with open(filename, 'r') as file:
        return await file.read()

async def main_async_file_io():
    filename = "async_file.txt"
    await write_to_file(filename, "Hello, Asyncio!")
    result = await read_from_file(filename)
    print(result)

# Run the main asynchronous function in an event loop
asyncio.run(main_async_file_io())


# Example 5: Asynchronous Web Scraping
async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def scrape_website(url):
    html = await fetch_html(url)
    # Perform asynchronous web scraping operations here
    print(f"Scraped content: {html[:100]}...")

async def main_async_web_scraping():
    website_url = "https://example.com"
    await scrape_website(website_url)

# Run the main asynchronous function in an event loop
asyncio.run(main_async_web_scraping())


# Example 6: Asynchronous Task Timeout
async def long_running_task():
    print("Task started")
    await asyncio.sleep(10)
    print("Task completed")

async def main_async_task_timeout():
    try:
        # Set a timeout of 3 seconds for the task
        await asyncio.wait_for(long_running_task(), timeout=3)
    except asyncio.TimeoutError:
        print("Task timed out")

# Run the main asynchronous function in an event loop
asyncio.run(main_async_task_timeout())
