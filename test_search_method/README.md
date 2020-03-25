## Bug report

*This may be a bug, or the same functionality can be achieved alternatively.*

### Bug description

A tensor object with tag is added to websocket server worker when staring the server worker. When using search method via websorket client worker, the object can be found and returns `ObjectNotFoundError`. 

During debugging, I found that the `search` method succeeds to found the object id on server worker, but this object has no attribute `owner`. When creating PointTensor with the server object id, since its `owner` attribute is `None`, the object owner is assigned to local worker by default. Sa a result, the error arises when the program tries to find an object on local worker with a remote object id.

### Bug reproduction

In order to reproduce the error, clone the files in this folder, run the code in terminal as follows

```bash
$ python start_server_bad.py &
$ python start_server_good.py &
$ python run_client
```

