from setuptools import setup

package_name = 'sensor_processing'

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
    description='Szenzoradatok feldolgozása a raktárrobot számára',
    license='MIT',
    entry_points={
        'console_scripts': [
            'sensor_node = sensor_processing.sensor_node:main',
        ],
    },
)

