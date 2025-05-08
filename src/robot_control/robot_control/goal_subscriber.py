#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from custom_interfaces.msg import Goal

class GoalSubscriber(Node):
    def __init__(self):
        super().__init__('goal_subscriber')
        self.subscription = self.create_subscription(
            Goal,
            'goal',
            self.goal_callback,
            10
        )
        self.get_logger().info('Goal Subscriber Node started')

    def goal_callback(self, msg):
        self.get_logger().info(f'Received goal: row={msg.row}, shelf={msg.shelf}')

def main(args=None):
    rclpy.init(args=args)
    node = GoalSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

