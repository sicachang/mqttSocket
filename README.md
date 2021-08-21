# mqttSocket
mqttSocket

## 角色
- Broker (`socketBroker.py`)：Broker伺服器，預設監聽埠`9000`，負責接收`Publish`訊息與發送訊息給 `Subsclipt`
- Publisher (`socketPub.py`)：傳訊者，ID為`0000000000`(不支持修正其他`ID`)，傳送訊息給訂閱Subsclipter。
- Subsclipter (`socketSub1.py`、`socketSub1.py`)：收訊者，預設兩組收訊者ID為`0000000001`(`socketSub1.py`)與`0000000002`(`socketSub2.py`)
  - 可自行透過增列建立其他收訊者(建立`socketSub1.py`副本，內文ID修正為其他`0`-`9`, `xxxxxxxxxx`數字)
## 使用教學
1. 啟動 Broker (`socketBroker.py`) 腳本：
啟動後首行將出現以下提醒字串：
```
<font color=#008000>Server started listening on socket 127.0.0.1:9000</font>
```
3. 啟動 Publisher (`socketPub.py`) 腳本：
啟動後首行將出現以下提醒字串：
```
Establishing socket connection to 127.0.0.1:9000
Connection established successfully
2021-08-22 01:32:26.731373 the 0 message(s) from Publisher
```
此外，`socketBroker.py`顯示：
```
.client 0 已線上訂閱
訂閱名單:  ['client0']
目前共1人連線
[client0]:  2021-08-22 01:32:26.731373 the 0 message(s) from Publisher
.[client0]:  2021-08-22 01:32:27.816793 the 1 message(s) from Publisher
```
5. 分別啟動 Subsclipter (`socketSub1.py`、`socketSub1.py`) 腳本：
各`Subsclipter`啟動後首行將出現以下提醒字串：
```
Establishing socket connection to 127.0.0.1:9000
Connection established successfully
```
且各` Subsclipter`會收到`Publisher`寄出之相同之時間戳記與訊息...
```
2021-08-22 01:35:07.444973 the 51 message(s) from Publisher
2021-08-22 01:35:08.535752 the 52 message(s) from Publisher
2021-08-22 01:35:09.629465 the 53 message(s) from Publisher
```
## 其他可擴增之功能
1. `Publisher`隱藏訊息輸出
2. `Publisher`修正time.sleep(1)參數，調整訊息發送頻率 (` Subsclipter` 同步修正 `if (abs(time_now - prev_call) > 1)`)
3. `Publisher` 的 `sock.sendData(data)` 前加入 input(data)，可自由傳送自選字串。

