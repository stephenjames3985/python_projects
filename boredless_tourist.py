#!/usr/bin/env python3

destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_dest_index(dest):
  '''
  this function will return the destination
  index upon locating it in the
  destinations list object
  destination: str
  '''
  dest_index = destinations[dest]
  return dest_index

print(get_dest_index('Los Angeles, USA'))
