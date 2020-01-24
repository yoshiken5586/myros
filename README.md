# myros
## 概要
入力した数値をPublishして、別のノードでSubscribeし、入力された数値の階乗の数値を表示する

## インストール方法  
`catkin_ws/src/`内で下記コマンドを実行

```
$ git clone https://github.com/yoshiken5586/myros.git
```

## 実行方法
端末１  
`$ roscore`  
端末２  
`$ rosrun myros pub_num.py`  
端末３  
`$ rosrun myros sub_num.py`  
## デモ動画  
https://youtu.be/V6kgHzI18EE
## LICENSE  
This repository is licensed under the GPLv3 license, see COPYING.  
