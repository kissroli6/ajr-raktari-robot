from setuptools import setup

package_name = 'navigation_manager'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kiss Roland',
    maintainer_email='kissroli02@gmail.com',
    description='A robot navigációs és célvezérlő rendszere',
    license='MIT',
    entry_points={
        'console_scripts': [
            'navigation_node = navigation_manager.navigation_node:main',
            'obstacle_publisher = navigation_manager.obstacle_publisher:main',
            'goal_subscriber = navigation_manager.goal_subscriber:main',
        ],
    },
)

