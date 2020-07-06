#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
#from sensor_msgs.msg import range
def move():
	rospy.init_node('nodes_practical')
	empty= Empty()
	takeoff =rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
	land =rospy.Publisher('/drone/land', Empty, queue_size=1)
	takeoff.publish(empty)
	land.publish(empty)	
if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException: pass
