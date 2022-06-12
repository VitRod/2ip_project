import pprint
from twoip import TwoIP

# At  first  downloading to Pycharm module 2ip

# or install the module from PyPI:
# python3 -m pip install 2ip

# If using API key, provide it here
twoip = TwoIP(key = None)

# Run the lookup
provider = twoip.provider(ip = '8.8.8.8')

# Print the retrieved country code
pprint.pprint(provider)


# the  result  in console  is  following:

# {'as': '15169',
#  'ip': '8.8.8.8',
#  'ip_range_end': '134744319',
#  'ip_range_start': '134744064',
#  'mask': '24',
#  'name_ripe': 'Google Inc.',
#  'name_rus': '',
#  'route': '8.8.8.0',
#  'site': 'https://www.google.com/'}