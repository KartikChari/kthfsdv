#!/usr/bin/env python
# Written by: Kartik Chari
# Date: 02 Sept 2018
# This is a subscriber node B that receives the message from node A and divides it by 0.15 before publishing
# the output with the toic /kthfs/result

# Imorting dependencies and required message types
import rospy
from std_msgs.msg import Float32
#from std_msgs.msg import Int32
Q = Float32()
MESSAGE = None

# Callback function
def msg_recd(k):
	global MESSAGE
	MESSAGE=k.data

# Main Function definition
def start():
	global Q 
	# node initialization
	rospy.init_node("Receive")
	# subscriber definition
	rospy.Subscriber("Chari",Float32,msg_recd)
	# creating a publisher object
	K_pub = rospy.Publisher("/kthfs/result",Float32,queue_size=1)
	# setting the broadcasting frequency to 0.05 Hz
	R = rospy.Rate(0.05)
	# variable initialization and assignment
	q = 0.15
	# Condition for the loop
	while not rospy.is_shutdown() :
		while not rospy.is_shutdown() and MESSAGE:
			Q.data = MESSAGE / q
			K_pub.publish(Q)
			R.sleep()

# Main function call
start()