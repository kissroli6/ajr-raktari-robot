import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusSubscriber(Node):
    def __init__(self):
        super().__init__('status_subscriber')
        self.subscription = self.create_subscription(
            String,
            'navigation_status',
            self.listener_callback,
            10
        )
        self.get_logger().info('Status Subscriber Node started')

    def listener_callback(self, msg):
        self.get_logger().info(f'Status received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = StatusSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

