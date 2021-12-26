#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def publishMethod():
    rospy.init_node('pubsub') 
    pub = rospy.Publisher('/rk_bot/rear_wheels_controller/command', Float64, queue_size=10)
    rate = rospy.Rate(10)
    rospy.loginfo("Data is being sent")  
    while not rospy.is_shutdown():
        twist = Float64()
        twist.data=10
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        publishMethod()
    except rospy.ROSInterruptException: 
        pass