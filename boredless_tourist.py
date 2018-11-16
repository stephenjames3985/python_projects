#!/usr/bin/env python3

'''
The following script is a Python project
that was an assignment of a codecademy.com
class
'''
# variable list of places
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'So Paulo, Brazil', 'Cairo, Egypt']

# traveler to use as a test variable for the functions
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_dest_index(dest):
  '''
  this function will return the destination
  index upon locating it in the
  destinations list object
  destination: str
  return: int
  '''
  dest_index = destinations.index(dest)
  return dest_index

#print(get_dest_index('Los Angeles, USA'))

# this next function was included and completely unnecessary
#def get_traveler_location(traveler):
#    '''
#    this func will return the location index of
#    the traveler
#    traveler: str
#    return: int
#    '''
#    traveler_dest = traveler[1]
#    traveler_dest_index = #get_dest_index(traveler_dest)
#    return traveler_dest_index

#test_destination_index = (get_traveler_location(test_traveler))

attractions = [[] for location in destinations]

def add_attraction(dest, attraction):
  '''
  this function will add attractions by destination to the list of lists
  dest: str
  attraction: str
  return:
  '''
  try:
    destination_index = get_dest_index(dest)

  except ValueError as err:
    print('Caught', err)

  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return attractions_for_destination

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# write function to help tourists find places they would like to go
def find_attractions(dest, interests):
  '''
  function to help tourists find places they
  would like to go.
  dest: str
  interests: list
  '''
  dest_index = get_dest_index(dest)
  attractions_in_city = attractions[dest_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if not interest in attraction_tags:
        continue
      else:
        attractions_with_interest.append(possible_attraction[0])

  return attractions_with_interest

# test the script so far and make sure it is working correctly
#la_arts = find_attractions('Los Angeles, USA', ['art'])
#print(la_arts)

def get_attractions_for_traveler(traveler):
  '''
  the function below will connect each of the
  travelers and match up interests with attractions
  traveler: list
  '''
  # destination
  traveler_dest = traveler[1]
  # interests
  traveler_interests = traveler[2]
  # find attractions for the traveler
  traveler_attractions = find_attractions(traveler_dest, traveler_interests)
  # greeting to print for the user
  interests_string = 'Hello, ' +  traveler[0] + ',' + ' we think you\'ll like these places around ' + traveler[1] + ': '
  for attraction in traveler_attractions:
    interests_string += '\n'
    interests_string += attraction

  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))
