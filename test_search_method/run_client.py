import torch
import syft as sy
from syft.workers.websocket_client import WebsocketClientWorker
from syft.exceptions import ObjectNotFoundError

if __name__ == "__main__":

    hook = sy.TorchHook(torch)
    bad = WebsocketClientWorker(id="bad",
                                port=8777,
                                host="localhost",
                                hook=hook)

    good = WebsocketClientWorker(id="good",
                                 port=8778,
                                 host="localhost",
                                 hook=hook)

    # When staring server, we already register a tensor
    # object with tab "test" in the server worker

    try:
        print("Search test with bad")
        data_pt = bad.search("test")
    except ObjectNotFoundError:
        print("Error: test is not found with bad worker!!!")

    print("Search test with good")
    data_pt = good.search("test")
    print("Test is found with good worker!!!")
    print("Here is the test data")
    print(data_pt[0].copy().get())

    # Reason:
    # search the tensor object on server worker with tensor tag
    # via the local client worker returns ERROR because
    # set_obj() on the server side does not assign the owner attribute on
    # the object.
    # This leads to the fact that, when.search() is called,
    # it tries to search the object with remote obj_id on local worker.

    # a possible solution is assigning self to owner attribute when calling set_obj()
    # or register_obj()
