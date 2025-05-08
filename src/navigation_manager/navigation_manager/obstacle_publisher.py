import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import time

class ObstaclePublisher(Node):
    def __init__(self):
        super().__init__('obstacle_publisher')
        self.publisher = self.create_publisher(Bool, 'obstacle_detected', 10)
        timer_period = 5.0
        self.timer = self.create_timer(timer_period, self.publish_obstacle)
        self.toggle = True
        self.get_logger().info('Obstacle Publisher started')

    def publish_obstacle(self):
        msg = Bool()
        msg.data = self.toggle
        self.publisher.publish(msg)
        self.get_logger().info(f'Published obstacle_detected = {self.toggle}')
        self.toggle = not self.toggle

def main(args=None):
    rclpy.init(args=args)
    node = ObstaclePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

