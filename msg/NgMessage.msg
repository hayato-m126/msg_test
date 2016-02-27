# コメントに2byte文字を入れると、rosbag_to_csvでうまく動かない
Header header #std_msgs/Header
int8 status #ロボットの状態を表す　例：0：スタンバイ 1：起動中 2：エラー
string text_ng #テキスト
