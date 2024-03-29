from setuptools import setup
 
setup(
  name='expressvpn-tray',
  version='0.2',
  description='ExpressVPN tray icon written in Gtk3',
  author='Alexander Rogachev',
  author_email='sorryforbadname@gmail.com',
  url='https://github.com/cog1to/expressvpn-tray',
  scripts=['expressvpn-tray'],
  include_package_data=True,
  py_modules=['utils'],
  data_files=[
    ('share/expressvpn-tray/', ['expressvpn-tray-connected.png', 'expressvpn-tray-not-connected.png'])
  ],
  license='WTFPL'
)
