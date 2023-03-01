import rclpy as ros
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import sensor_msg.msg as msgs
class ReadLaser(Node):
    def __init__(self):
        super().__init__('lidar_controller_node')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.laser_callback,
            10
        )
    def laser_callback(self,msg):
        self.get_logger().info("I heard this: %f" %msg.data[100])

def main(args=None):
    print("oh hi")
    ros.init()
    reading_laser = ReadLaser()
    ros.spin(reading_laser)

if __name__ == '__main__':
    main()
    