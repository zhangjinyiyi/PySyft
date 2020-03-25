import torch
import syft

from syft.workers.websocket_server import WebsocketServerWorker

# Hook and start server
hook = syft.TorchHook(torch)
server_worker = WebsocketServerWorker(id="bad",
                                      host="localhost",
                                      port=8777,
                                      hook=hook)

test_data = torch.tensor([1, 2, 3]).tag("test")
server_worker.set_obj(test_data)

print("Bad server started.")
server_worker.start()
