from setuptools import setup
from pykospacing import __version__


setup(name='1.0.0',
      version=__version__,
      url='https://github.com/koomook/PyKoSpacing',
      license='GPL-3',
      author='Heewon Jeon',
      author_email='madjakarta@gmail.com',
      description='Python package for automatic Korean word spacing.',
      packages=['pykospacing', ],
      long_description=open('README.md', encoding='utf-8').read(),
      zip_safe=False,
      include_package_data=True,

      install_requires=[
      ],

      entry_points={
          'console_scripts': [
              'pykos = pykospacing.pykos:main',
          ],
      },
      )
