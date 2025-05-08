from setuptools import setup

package_name = 'robot_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kiss Roland',
    maintainer_email='kissroli02@gmail.com',
    description='Robot motion control node',
    license='MIT',
    entry_points={
        'console_scripts': [
    	'controller_node = robot_control.controller_node:main',
    	'goal_publisher = robot_control.goal_publisher:main',
    	'goal_subscriber = robot_control.goal_subscriber:main',
	],
    },
)

