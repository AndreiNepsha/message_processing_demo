import asyncio
import asynctnt


async def main():
    conn = asynctnt.Connection(host='127.0.0.1', port=3301)
    await conn.connect()

    while True:
        tasks = await conn.call('event_queue:take')
        print('tasks:', tasks)

        for task in tasks:
            task_id = task[0]
            print(f'Ack {task_id}')
            await conn.call('event_queue:ack', [task_id])

        if not tasks:
            asyncio.sleep(0.1)

    await conn.disconnect()


asyncio.run(main())