from setuptools import setup

package_name = 'gui_interface'

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
    description='Egyszerű felület a raktárrobot célpontvezérléséhez',
    license='MIT',
    entry_points={
        'console_scripts': [
            'gui_node = gui_interface.gui_node:main',
            'goal_publisher = gui_interface.goal_publisher:main',
            'status_subscriber = gui_interface.status_subscriber:main',
            'obstacle_publisher = gui_interface.obstacle_publisher:main',
        ],
    },
)

