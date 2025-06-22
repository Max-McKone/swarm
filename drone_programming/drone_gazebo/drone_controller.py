#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def main():
    rospy.init_node('drone_controller', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        cmd = Twist()
        cmd.linear.x = 1.0  # Move forward
        cmd.angular.z = 0.5  # Rotate
        pub.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass 