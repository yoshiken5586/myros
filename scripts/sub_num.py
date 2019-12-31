#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Int32

def cb(message):
    print(math.factorial(message.data))

if __name__ == '__main__':
	rospy.init_node('factorial')
	sub = rospy.Subscriber('num', Int32, cb)
	rospy.spin()
