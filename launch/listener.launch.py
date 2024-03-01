from launch import LaunchDescription
from launch_ros.actions import Node

def generateLaunchDescription():
    return (
        LaunchDescription(
            [
                Node(
                    package='demo_nodes_cpp',
                    executable='listener',
                ),
            ]
        )
    )