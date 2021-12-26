#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def publisher():
    rospy.init_node('commander')
    forward = rospy.Publisher('move_straight', Float64, queue_size=10)
    turn = rospy.Publisher('turn', Float64, queue_size=10)
    rate = rospy.Rate(10) 
    rospy.loginfo("Data is being sent")
    while not rospy.is_shutdown():
        twist = Float64()
        twist.data = 10
        forward.publish(twist)
        twist.data = 0.5
        turn.publish(twist)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException: 
        pass