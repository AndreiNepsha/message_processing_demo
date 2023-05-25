from dataclasses import dataclass
from typing import Any
import asynctnt


@dataclass
class QueueItem:
    id: int
    data: Any

class AsyncTarantoolQueueGateway:
    def __init__(self, host: str, port: int, queue: str) -> None:
        self.host = host
        self.port = port
        self.queue = queue
        self.connection = None

    async def connect(self):
        conn = asynctnt.Connection(host=self.host, port=self.port)
        await conn.connect()
        self.connection = conn
    
    async def disconnect(self):
        await self.connection.disconnect()

    async def __aenter__(self):
        await self.connect()
        return self
 
    async def __aexit__(self, *args):
        await self.disconnect()

    async def put(self, data):
        return await self.connection.call(f'{self.queue}:put', [data])
    
    async def take(self) -> QueueItem:
        raw = await self.connection.call(f'{self.queue}:take')
        return QueueItem(
            id=raw[0][0],
            data=raw[0][2]
        )
    
    async def ack(self, item_id: int):
        await self.connection.call(f'{self.queue}:ack', [item_id])
