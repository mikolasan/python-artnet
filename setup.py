from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
	name = "python-artnet",
	version = "0.1",
	
	include_package_data	= True,
	zip_safe				= False,
	packages				= find_packages('src'),
	package_dir				= {'': 'src'},
	
	entry_points	= {
		'setuptools.file_finders'	: [
			'git = setuptools_git:gitlsfiles',
		],
		'console_scripts': [
			'artnet = artnet.scripts:main',
		]
	},
	
	install_requires = requirements
)
