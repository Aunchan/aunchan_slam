#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from tf import transformations

def main():
    pub = rospy.Publisher("attitude", Imu, queue_size=10)
    rospy.init_node('test_imu_pub')
    rate = rospy.Rate(7)
    while not rospy.is_shutdown():
        msg = Imu()
        msg.header.frame_id = "imu_frame"
        msg.header.stamp = rospy.Time.now()
        quaternion = transformations.quaternion_from_euler(0.0,-0.2,0)
        msg.orientation.x = quaternion[0]
        msg.orientation.y = quaternion[1]
        msg.orientation.z = quaternion[2]
        msg.orientation.w = quaternion[3]
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass