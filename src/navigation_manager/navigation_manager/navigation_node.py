import rclpy
from rclpy.node import Node
from custom_interfaces.msg import Goal
from std_msgs.msg import String, Bool

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.goal_sub = self.create_subscription(
            Goal,
            'goal',
            self.goal_callback,
            10
        )
        self.obstacle_sub = self.create_subscription(
            Bool,
            'obstacle_detected',
            self.obstacle_callback,
            10
        )
        self.status_pub = self.create_publisher(String, 'navigation_status', 10)
        self.obstacle_present = False
        self.get_logger().info('Navigation Node started')

    def obstacle_callback(self, msg):
        self.obstacle_present = msg.data
        if self.obstacle_present:
            self.get_logger().warn('Obstacle detected!')

    def goal_callback(self, msg):
        self.get_logger().info(f'Received goal: row={msg.row}, shelf={msg.shelf}')

        status_msg = String()
        if self.obstacle_present:
            status_msg.data = 'failed'
            self.get_logger().warn('Navigation failed: Obstacle in the way.')
        else:
            status_msg.data = 'success'
            self.get_logger().info('Navigation successful.')

        self.status_pub.publish(status_msg)

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

