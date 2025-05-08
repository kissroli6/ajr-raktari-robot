import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        self.subscription = self.create_subscription(
            String,
            'navigation_status',
            self.status_callback,
            10
        )
        self.get_logger().info('Controller Node started')

    def status_callback(self, msg):
        if msg.data == 'success':
            self.get_logger().info('Goal reached. Transporting box to exit...')
            # Simulated action
            self.get_logger().info('Box delivered to exit.')
        elif msg.data == 'failed':
            self.get_logger().info('Navigation failed. Box not delivered.')

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

