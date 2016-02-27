# msg_test
独自形式のメッセージにマルチバイト文字のコメントが入っているとGUIの便利なツールが動かなかった  
rqt_bag：データが表示されない  
rosbag_to_csv：CSV変換がされない  

## エラー内容
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe3 in position 461: ordinal not in range(128)  
pythonの文字処理のあたりでつまずいてる模様

## ファイル構成
./msg : 独自メッセージ  
./scripts : 検証用データを作成したスクリプト  
./log : 記録したファイルとエラー内容のコピー  



# 対策
msgファイルに日本語のコメントを書いてはいけない（戒め）
