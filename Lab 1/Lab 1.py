import asyncio
import aiohttp


async def fetch_data(url):
    print(f"Fetching data from {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                print(f"Data fetched from {url}")
                return f"Data from {url}"
            else:
                print(f"An error occured when accessing {url}")
                return "No Data"


async def main():
    # Run multiple asynchronous tasks concurrently
    tasks = [
        fetch_data("https://dummy.restapiexample.com/api/v1/employees"),
        fetch_data("https://google.com"),
        fetch_data("https://chat.openai.com")
    ]
    results = await asyncio.gather(*tasks)
    print("All tasks completed:")
    for result in results:
        print(result)

# Run the main asynchronous function
asyncio.run(main())
