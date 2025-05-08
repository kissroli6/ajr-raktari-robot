#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from custom_interfaces.msg import Goal
from std_msgs.msg import String
import tkinter as tk
from threading import Thread

class GuiNode(Node):
    def __init__(self, gui_callback):
        super().__init__('gui_node')
        self.publisher = self.create_publisher(Goal, 'goal', 10)
        self.subscription = self.create_subscription(
            String,
            'navigation_status',
            self.status_callback,
            10
        )
        self.gui_callback = gui_callback
        self.get_logger().info('GUI Node started')

    def publish_goal(self, row, shelf):
        msg = Goal()
        msg.row = row
        msg.shelf = shelf
        self.publisher.publish(msg)
        self.get_logger().info(f"Goal sent: row={row}, shelf={shelf}")
        self.gui_callback("Goal sent")

    def status_callback(self, msg):
        self.get_logger().info(f"Status received: {msg.data}")
        self.gui_callback(f"Status: {msg.data}")

def start_ros2_node(gui_callback, gui_node_ref):
    rclpy.init()
    node = GuiNode(gui_callback)
    gui_node_ref["node"] = node  
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

def main():
    root = tk.Tk()
    root.title("Smart Warehouse GUI")

    tk.Label(root, text="Row:").grid(row=0, column=0)
    tk.Label(root, text="Shelf:").grid(row=1, column=0)

    row_entry = tk.Entry(root)
    shelf_entry = tk.Entry(root)
    row_entry.grid(row=0, column=1)
    shelf_entry.grid(row=1, column=1)

    status_label = tk.Label(root, text="Status: Waiting...")
    status_label.grid(row=3, column=0, columnspan=2)

    # Placeholder, will be replaced after ROS node init
    gui_node_ref = {"node": None}

    def update_status(text):
        status_label.config(text=text)

    def send_goal():
        try:
            row = int(row_entry.get())
            shelf = int(shelf_entry.get())
        except ValueError:
            update_status("Invalid input")
            return
        gui_node_ref["node"].publish_goal(row, shelf)

    tk.Button(root, text="Send Goal", command=send_goal).grid(row=2, column=0, columnspan=2)

    # Start ROS 2 node in background
    ros_thread = Thread(target=start_ros2_node, args=(update_status, gui_node_ref),daemon=True)
    ros_thread.start()

    # Wait a moment for the node to initialize and store reference
    def wait_for_node():
        import time
        while not hasattr(start_ros2_node, "node"):
            time.sleep(0.1)

    # Start GUI
    root.mainloop()

if __name__ == '__main__':
    main()

