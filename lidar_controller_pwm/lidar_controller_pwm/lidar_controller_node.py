import rclpy as ros
from sensor_msgs.msg import LaserScan

g_node = None
def laser_callback(message):
    global g_node
    g_node.get_logger().info(
        "Recieved: %s" % message.data[100] 
    )

def main(args=None):
    global g_node
    print("WOW")
    ros.init(args=args)
    g_node = ros.create_node('lidar_subscriber')
    subscription = g_node.create_subscription(LaserScan,'scan',laser_callback,10)
    subscription
    while ros.ok():
        ros.spin_once(g_node)
    g_node.destroy_node()
    ros.shutdown()


if __name__ == '__main__':
    diditwork = True
    main()
    