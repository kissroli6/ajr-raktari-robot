#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from custom_interfaces.msg import Goal

class GoalPublisher(Node):
    def __init__(self):
        super().__init__('goal_publisher')
        self.publisher_ = self.create_publisher(Goal, 'goal', 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.goal = Goal()
        self.goal.row = 1
        self.goal.shelf = 2

    def timer_callback(self):
        self.publisher_.publish(self.goal)
        self.get_logger().info(f"Kuldott cel: sor={self.goal.row}, polc={self.goal.shelf}")

def main(args=None):
    rclpy.init(args=args)
    node = GoalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

