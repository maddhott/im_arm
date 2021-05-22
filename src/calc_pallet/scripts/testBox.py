#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt16MultiArray, String

import sys

def main(args):
    #ic = selectBox()
    rospy.init_node('selectBox', anonymous=True)
    pub = rospy.Publisher('/box_position', String, queue_size = 10)
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish("sibal")
        r.sleep()

if __name__ == "__main__":
    main(sys.argv)
