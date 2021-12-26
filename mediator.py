#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

pub_right = rospy.Publisher('/rk_bot/right_wheel_controller/command', Float64, queue_size=10) 
pub_left = rospy.Publisher('/rk_bot/left_wheel_controller/command', Float64, queue_size=10)
pub_move = rospy.Publisher('/rk_bot/rear_wheels_controller/command', Float64, queue_size=10) 
twist = Float64()


def straight(data):
    rospy.loginfo(rospy.get_caller_id() + "data received %f", data.data)
    pub_move.publish(data.data)


def turn(data):
    rospy.loginfo(rospy.get_caller_id() + "data received %f", data.data)
    pub_left.publish(data.data)
    pub_right.publish(data.data)


def listener():
 
    rospy.init_node('controller_manager', anonymous=True)

    rospy.Subscriber("move_straight", Float64, straight)
    rospy.Subscriber("turn", Float64, turn)

    rospy.spin()
 
if __name__ == '__main__':
    listener()