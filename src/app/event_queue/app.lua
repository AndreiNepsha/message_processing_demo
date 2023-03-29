queue = require 'queue'

box.cfg{}

queue:start()

event_queue = queue.tube.event_queue
if not event_queue then
    event_queue = queue.create_tube('event_queue', 'fifo')
end
