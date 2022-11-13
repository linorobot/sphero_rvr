import os
from glob import glob
from setuptools import setup

package_name = 'sphero_rvr'

setup(
    name=package_name,
    version='0.0.1',
    packages=[
        package_name
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Juan Miguel jimeno',
    maintainer_email='jimenojmm@gmail.com',
    description='Sphero RVR ROS2 Package',
    license='Apache 2.0',
    entry_points={
        'console_scripts': [
            'sphero_node = sphero_rvr.sphero_node:main'
        ],
    },
)