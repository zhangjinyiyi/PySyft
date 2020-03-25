import torch
import syft

from syft.workers.websocket_server import WebsocketServerWorker

class WebsocketServerWorkerGood(WebsocketServerWorker):

    def set_obj(self, obj: object):
        self._objects[obj.id] = obj
        self._objects[obj.id].owner = self


# Hook and start server
hook = syft.TorchHook(torch)
server_worker = WebsocketServerWorkerGood(id="good",
                                          host="localhost",
                                          port=8778,
                                          hook=hook)

test_data = torch.tensor([1, 2, 3]).tag("test")
server_worker.set_obj(test_data)

print("Good server started.")
server_worker.start()
