from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name='biketrauma_elk',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='http://github.com/LauraElKaim.git',
  author='ElKaimLaura',
  author_email='laura.el-kaim@etu.umontpellier.fr',
  license='MIT',
  packages=['biketrauma','biketrauma.io', 'biketrauma.preprocess', 'biketrauma.vis'],
  zip_safe=False
)
