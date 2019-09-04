from setuptools import setup
 
setup(
  name='expressvpn-tray',
  version='0.1',
  description='ExpressVPN tray icon written in Gtk3',
  author='Alexander Rogachev',
  author_email='sorryforbadname@gmail.com',
  scripts=['expressvpn-tray'],
  include_package_data=True,
  py_modules=None,
  data_files=[
    ('share/expressvpn-tray/', ['expressvpn-tray-connected.png', 'expressvpn-tray-not-connected.png'])
  ]
)
