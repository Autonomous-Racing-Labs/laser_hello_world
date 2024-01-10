from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'hello_world'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.xacro')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.rviz')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Philip Wette',
    maintainer_email='philip.wette@hsbi.de',
    description='Hello World for laser scanner',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_world = hello_world.hello_world:main',
        ],
    },
)
