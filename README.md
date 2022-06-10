# Task 3

### HTTP client POST requests
```shell
curl -X POST http://127.0.0.1:8000/facade_service -H 'Content-Type: application/json' -d '{"msg": "msg1"}'
curl -X POST http://127.0.0.1:8000/facade_service -H 'Content-Type: application/json' -d '{"msg": "msg2"}'
curl -X POST http://127.0.0.1:8000/facade_service -H 'Content-Type: application/json' -d '{"msg": "msg3"}'
curl -X POST http://127.0.0.1:8000/facade_service -H 'Content-Type: application/json' -d '{"msg": "msg4"}'
curl -X POST http://127.0.0.1:8000/facade_service -H 'Content-Type: application/json' -d '{"msg": "msg5"}'
curl -X POST http://127.0.0.1:8000/facade_service -H 'Content-Type: application/json' -d '{"msg": "msg6"}'
curl -X POST http://127.0.0.1:8000/facade_service -H 'Content-Type: application/json' -d '{"msg": "msg7"}'
curl -X POST http://127.0.0.1:8000/facade_service -H 'Content-Type: application/json' -d '{"msg": "msg8"}'
curl -X POST http://127.0.0.1:8000/facade_service -H 'Content-Type: application/json' -d '{"msg": "msg9"}'
curl -X POST http://127.0.0.1:8000/facade_service -H 'Content-Type: application/json' -d '{"msg": "msg10"}'
```


### Logging-service 1 logs
```shell
* Running on http://127.0.0.1:8001 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 722-947-759
[2022-06-10 06:31:56,801] INFO in service: msg1
127.0.0.1 - - [10/Jun/2022 06:31:56] "POST / HTTP/1.1" 200 -
[2022-06-10 06:31:56,882] INFO in service: msg3
127.0.0.1 - - [10/Jun/2022 06:31:56] "POST / HTTP/1.1" 200 -
[2022-06-10 06:31:56,904] INFO in service: msg4
127.0.0.1 - - [10/Jun/2022 06:31:56] "POST / HTTP/1.1" 200 -
[2022-06-10 06:31:57,037] INFO in service: msg10
127.0.0.1 - - [10/Jun/2022 06:31:57] "POST / HTTP/1.1" 200 -
```

### Logging-service 2 logs
```shell
* Running on http://127.0.0.1:8002 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 722-947-759
[2022-06-10 06:31:56,953] INFO in service: msg6
127.0.0.1 - - [10/Jun/2022 06:31:56] "POST / HTTP/1.1" 200 -
[2022-06-10 06:31:56,974] INFO in service: msg7
127.0.0.1 - - [10/Jun/2022 06:31:56] "POST / HTTP/1.1" 200 -
[2022-06-10 06:31:57,016] INFO in service: msg9
127.0.0.1 - - [10/Jun/2022 06:31:57] "POST / HTTP/1.1" 200 -
```

### Logging-service 3 logs
```shell
* Running on http://127.0.0.1:8003 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 722-947-759
[2022-06-10 06:31:56,861] INFO in service: msg2
127.0.0.1 - - [10/Jun/2022 06:31:56] "POST / HTTP/1.1" 200 -
[2022-06-10 06:31:56,931] INFO in service: msg5
127.0.0.1 - - [10/Jun/2022 06:31:56] "POST / HTTP/1.1" 200 -
[2022-06-10 06:31:56,995] INFO in service: msg8
127.0.0.1 - - [10/Jun/2022 06:31:56] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2022 06:34:53] "GET / HTTP/1.1" 200 -
```

### HTTP client GET requests
```shell
(venv) (base) admin@Volodymyr-Fedynyak microservices-ucu % curl http://127.0.0.1:8000/facade_service
msg5 msg1 msg7 msg4 msg10 msg8 msg6 msg9 msg2 msg3 static
(venv) (base) admin@Volodymyr-Fedynyak microservices-ucu % curl http://127.0.0.1:8000/facade_service
msg5 msg1 msg7 msg4 msg10 msg8 msg6 msg9 msg2 msg3 static
(venv) (base) admin@Volodymyr-Fedynyak microservices-ucu % curl http://127.0.0.1:8000/facade_service
msg5 msg1 msg7 msg4 msg10 msg8 msg6 msg9 msg2 msg3 static
(venv) (base) admin@Volodymyr-Fedynyak microservices-ucu % curl http://127.0.0.1:8000/facade_service
<!doctype html>
<html lang=en>
  <head>
    <title>requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=8003):
```
After killing some Hazelcast nodes the message list is still consistent until the missing logging-service instance is requested