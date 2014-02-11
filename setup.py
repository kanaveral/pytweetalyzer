try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Analyzing twitter trending hashtag origins'
	'author': 'Anders E'
	'url': 'http://www.ellmo.se'
	'download_url': 'https://github.com/kanaveral/pytweetalyzer'
	'author_email': 'anders@ellmo.se'
	'version': '0.1'
	'install_requires': ['nose']
	'packages': ['NAME']
	'scripts': []
	'name': 'pytweetalyzer'
}

setup(**config´)