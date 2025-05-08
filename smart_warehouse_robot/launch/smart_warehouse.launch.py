from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gui_interface',
            executable='gui_node',
            name='gui_node',
            output='screen'
        ),
        Node(
            package='navigation_manager',
            executable='navigation_node',
            name='navigation_node',
            output='screen'
        ),
        Node(
            package='navigation_manager',
            executable='obstacle_publisher',
            name='obstacle_publisher',
            output='screen'
        ),
        Node(
            package='robot_control',
            executable='controller_node',
            name='controller_node',
            output='screen'
        ),
        Node(
            package='gui_interface',
            executable='status_subscriber',
            name='status_subscriber',
            output='screen'
        ),
        Node(
            package='robot_control',
            executable='goal_subscriber',
            name='goal_subscriber',
            output='screen'
        )
    ])

