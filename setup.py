from setuptools import find_packages, setup

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	('share/my_first_pkg/launch', ['launch/my_launch.py']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='hafidhghouilem@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'talker = my_first_pkg.talker:main',
		'listener = my_first_pkg.listener:main',
        ],
	'launch':[
		'my_launch = my_first_pkg.launch.my_launch.py'
	],
    },
)
