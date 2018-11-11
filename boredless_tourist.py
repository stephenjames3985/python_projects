#!/usr/bin/env python3

destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  '''
  this function will return the destination
  index upon locating it in the
  destinations list object
  destination: str
  '''
  destination_index = destinations[destination]
  return destination_index

print(get_destination_index)
