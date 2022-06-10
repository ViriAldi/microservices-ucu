# Task 4

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

### Messenges-service 1 logs
```shell
* Running on http://127.0.0.1:8004 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 722-947-759
[2022-06-10 07:16:36,365] INFO in service: Consumed msg1
[2022-06-10 07:16:36,386] INFO in service: Consumed msg2
[2022-06-10 07:16:36,450] INFO in service: Consumed msg5
[2022-06-10 07:16:36,470] INFO in service: Consumed msg6
[2022-06-10 07:16:36,533] INFO in service: Consumed msg9
[2022-06-10 07:16:36,553] INFO in service: Consumed msg10
```

### Messenges-service 2 logs
```shell
* Running on http://127.0.0.1:8005 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 722-947-759
[2022-06-10 07:16:36,407] INFO in service: Consumed msg3
[2022-06-10 07:16:36,428] INFO in service: Consumed msg4
[2022-06-10 07:16:36,491] INFO in service: Consumed msg7
[2022-06-10 07:16:36,512] INFO in service: Consumed msg8
```

### Logging-service 1 logs
```shell
* Running on http://127.0.0.1:8001 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 722-947-759
[2022-06-10 07:16:36,447] INFO in service: Received msg5
127.0.0.1 - - [10/Jun/2022 07:16:36] "POST / HTTP/1.1" 200 -
[2022-06-10 07:16:36,531] INFO in service: Received msg9
127.0.0.1 - - [10/Jun/2022 07:16:36] "POST / HTTP/1.1" 200 -
```

### Logging-service 2 logs
```shell
* Running on http://127.0.0.1:8002 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 722-947-759
[2022-06-10 07:16:36,426] INFO in service: Received msg4
127.0.0.1 - - [10/Jun/2022 07:16:36] "POST / HTTP/1.1" 200 -
[2022-06-10 07:16:36,489] INFO in service: Received msg7
127.0.0.1 - - [10/Jun/2022 07:16:36] "POST / HTTP/1.1" 200 -
[2022-06-10 07:16:36,510] INFO in service: Received msg8
127.0.0.1 - - [10/Jun/2022 07:16:36] "POST / HTTP/1.1" 200 -
```

### Logging-service 3 logs
```shell
* Running on http://127.0.0.1:8003 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 722-947-759
[2022-06-10 07:16:36,362] INFO in service: Received msg1
127.0.0.1 - - [10/Jun/2022 07:16:36] "POST / HTTP/1.1" 200 -
[2022-06-10 07:16:36,384] INFO in service: Received msg2
127.0.0.1 - - [10/Jun/2022 07:16:36] "POST / HTTP/1.1" 200 -
[2022-06-10 07:16:36,405] INFO in service: Received msg3
127.0.0.1 - - [10/Jun/2022 07:16:36] "POST / HTTP/1.1" 200 -
[2022-06-10 07:16:36,469] INFO in service: Received msg6
127.0.0.1 - - [10/Jun/2022 07:16:36] "POST / HTTP/1.1" 200 -
[2022-06-10 07:16:36,552] INFO in service: Received msg10
127.0.0.1 - - [10/Jun/2022 07:16:36] "POST / HTTP/1.1" 200 -
```

### HTTP client GET requests
```shell
(venv) (base) admin@Volodymyr-Fedynyak microservices-ucu % curl http://127.0.0.1:8000/facade_service
msg5 msg2 msg3 msg10 msg6 msg4 msg7 msg1 msg8 msg9 msg4 msg8% 
(venv) (base) admin@Volodymyr-Fedynyak microservices-ucu % curl http://127.0.0.1:8000/facade_service
msg5 msg2 msg3 msg10 msg6 msg4 msg7 msg1 msg8 msg9 msg2 msg6 msg10
(venv) (base) admin@Volodymyr-Fedynyak microservices-ucu % curl http://127.0.0.1:8000/facade_service
msg5 msg2 msg3 msg10 msg6 msg4 msg7 msg1 msg8 msg9 msg4 msg8
(venv) (base) admin@Volodymyr-Fedynyak microservices-ucu % curl http://127.0.0.1:8000/facade_service
msg5 msg2 msg3 msg10 msg6 msg4 msg7 msg1 msg8 msg9 msg4 msg8%
```