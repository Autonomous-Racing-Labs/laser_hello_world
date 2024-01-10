
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os
import yaml

def generate_launch_description():
    ld = LaunchDescription()

    hello_world_node = Node(
        package='hello_world',
        executable='hello_world',
        output='screen',
        name='hello_world',
        parameters=[]
    )


    # finalize
    ld.add_action(hello_world_node)

    return ld
