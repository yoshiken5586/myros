#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('num')
pub = rospy.Publisher('num', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
	n =int(raw_input('input num:'))
	pub.publish(n)
	rate.sleep()
