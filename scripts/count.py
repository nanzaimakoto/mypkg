/*Copyright (c) makoto nanzai. All Rights Reserved.*/
#!/usr/bin/env python2


import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
	n += 1
	pub.publish(n)
	rate.sleep()
