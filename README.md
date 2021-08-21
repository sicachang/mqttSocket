# mqttSocket
mqttSocket

## Function

1. 追蹤訂閱 

- `[case1]`
.client 1 已線上訂閱
訂閱名單:  ['client1']
目前共1人連線
[client1]:  hi Server my name is client1
.[client1]:  hi Server my name is client1

- `[case2]`
.client 2 已線上訂閱
訂閱名單:  ['client1', 'client2']
目前共2人連線

2. 追蹤取消訂閱

- `[case1]` 
2021-08-21 18:54:59.504017 client2 已退出訂閱
['client1']
目前共1人連線


3. Broker 傳送訊息 timestamp

多使用收接收相同訊息
- `[client1]`
2021-08-21 18:55:08.998702[localhost] say: hi client1

- `[client2]`
2021-08-21 18:55:08.998702[localhost] say: hi client2 # got the same timestamp as client1

