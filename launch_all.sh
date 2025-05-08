#!/bin/bash

source install/setup.bash

xfce4-terminal --title="GUI Node" --hold --command="bash -c 'source ~/smart_warehouse_robot/install/setup.bash && ros2 run gui_interface gui_node'"
xfce4-terminal --title="Goal Subscriber" --hold --command="bash -c 'source ~/smart_warehouse_robot/install/setup.bash && ros2 run robot_control goal_subscriber'"
xfce4-terminal --title="Navigation Node" --hold --command="bash -c 'source ~/smart_warehouse_robot/install/setup.bash && ros2 run navigation_manager navigation_node'"
xfce4-terminal --title="Obstacle Publisher" --hold --command="bash -c 'source ~/smart_warehouse_robot/install/setup.bash && ros2 run navigation_manager obstacle_publisher'"
xfce4-terminal --title="Controller Node" --hold --command="bash -c 'source ~/smart_warehouse_robot/install/setup.bash && ros2 run robot_control controller_node'"
xfce4-terminal --title="Status Subscriber" --hold --command="bash -c 'source ~/smart_warehouse_robot/install/setup.bash && ros2 run gui_interface status_subscriber'"

