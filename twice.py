/*Copyright (c) makoto nanzai. All Rights Reserved.*/
#!/usr/bin/env python2

import rospy
from std_msgs.msg import Int32

n = 0

def cd(massage):
    global n
    n = massage.data*2



rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cd)
pub = rospy.Publisher('twice', Int32, queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
	pub.publish(n)
	rate.sleep()
