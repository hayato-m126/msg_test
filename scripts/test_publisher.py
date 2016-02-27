#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from msg_test.msg import OkMessage #import original message
from msg_test.msg import NgMessage #import original message including multi byte charcters
import numpy as np

rospy.init_node('msg_test')
ok_pub = rospy.Publisher('okmsg', OkMessage, queue_size=10)
ok_pub_msg = OkMessage()
ng_pub = rospy.Publisher('ngmsg', NgMessage, queue_size=10)
ng_pub_msg = NgMessage()
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    time_now = rospy.Time.now()
    status = np.random.randint(3)
    ok_pub_msg.header.stamp = time_now
    ok_pub_msg.status = status
    ok_pub_msg.text_ok ="テキストは2byteおｋ"
    ok_pub.publish(ok_pub_msg)
    ng_pub_msg.header.stamp = time_now
    ng_pub_msg.status = status
    ng_pub_msg.text_ng ="テキストは2byteおｋ"
    ng_pub.publish(ng_pub_msg)
    rate.sleep()
