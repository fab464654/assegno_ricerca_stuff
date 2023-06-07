from setuptools import setup

package_name = 'ti_mmwave_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fab',
    maintainer_email='fab@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ti_mmwave_ros2_node = ti_mmwave_ros2.ti_mmwave_ros2_node:main'
        ],
    },
)
