import asyncio
import asynctnt


async def main():
    conn = asynctnt.Connection(host='127.0.0.1', port=3301)
    await conn.connect()
    task_data = "tasssk"
    res = await conn.call('event_queue:put', [task_data])
    print(res)
    await conn.disconnect()


asyncio.run(main())