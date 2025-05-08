#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.get_logger().info("Sensor Node elindult")

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

