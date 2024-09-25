import os
import collections
import re

Location = collections.namedtuple('Location', ['id', 'title'])

def locations():
  output = os.popen("expressvpn list").read().strip().split("\n")
  separator_index = _first(output, _starts_with_prefix("---"))
  if separator_index >= 0:
    output = output[separator_index + 2 : len(output) - 2]
  locations = list(map(_location, output))
  return locations

def status():
  ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
  status_raw = ansi_escape.sub('', os.popen('expressvpn status').read().strip())
  
  if status_raw.startswith('A new version is available'):
    lines = status_raw.split('\n')
    status_raw = lines[2]
  elif len(status_raw) == 0:
    status_raw = 'Not running'
  elif not status_raw.startswith('Not connected'):
    m = re.search('(Connected to .*\n)', status_raw)
    if m:
      status_raw = m.group(1)
  vpn_status = status_raw
  
  return vpn_status

# Private helpers

def _starts_with_prefix(prefix):
  def func(str):
    return str.startswith(prefix)
  return func

def _first(arr, cond):
  for i in range(len(arr)):
    if cond(arr[i]):
      return i
  return -1

def _location(inp):
  splitted = inp.split('\t')
  return Location(splitted[0], splitted[len(splitted) - 1])

