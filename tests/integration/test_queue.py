import pytest
import pytest_asyncio

from src.infra.gateway.tarantool_queue import AsyncTarantoolQueueGateway

@pytest_asyncio.fixture
async def queue():
    async with AsyncTarantoolQueueGateway(
        host='127.0.0.1',
        port=3301,
        queue='event_queue'
    ) as queue:
        yield queue


@pytest.mark.asyncio
async def test_put_and_take(queue: AsyncTarantoolQueueGateway):
    await queue.put("hello")
    item = await queue.take()
    await queue.ack(item_id=item.id)
    assert "hello" == item.data
    