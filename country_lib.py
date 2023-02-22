import httpx
from pprint import pprint as print

url = 'https://restcountries.com/v3.1/name/{}?fullText=true'


# Head class
class Country:
	# Init function
	def __init__(self, name: str) -> None:
		self.name = name
		self.response = httpx.get(url.format(self.name)).json()

	# Returns Different types of names
	def country_name(self, common_name=True, official_name=False, short_name=False):
		# Store the country name
		list_: list = []

		# If common name is True
		if common_name:
			list_.append((self.response[0]['name']['common']))

		# If official name is True
		if official_name:
			list_.append((self.response[0]['name']['official']))

		# If short name is True
		if short_name:
			list_.append((self.response[0]['altSpellings'][0]))

		# Else nothing given
		if common_name == False and official_name == False and short_name == False:
			return None

		# Return the information
		return tuple(i for i in list_)

	# Reply answers that is... questions
	def is_(self, independent=True, landlocked=False, un_member=False):
		# Answer collection
		list_ = []

		# Check for is independent
		if independent:
			list_.append(self.response[0]['independent'])

		# Check for is landlocked
		if landlocked:
			list_.append(self.response[0]['landlocked'])

		# Check for is United Nation's member
		if un_member:
			list_.append(self.response[0]['unMember'])

		# Return if nothing chosen
		if len(list_) == 0:
			return None

		# Return the answer
		return tuple(i for i in list_)

	# Currency information
	def currencies(self, currency=True, name=False, symbol=False):
		# Answer collection
		list_ = []

		# Show short name of the currency
		if currency:
			for i in self.response[0]['currencies'].keys():
				list_.append(i)

		# Show name of the currency
		if name:
			for i in self.response[0]['currencies'].values():
				list_.append(i['name'])

		# Show symbol of the currency
		if symbol:
			for i in self.response[0]['currencies'].values():
				list_.append(i['symbol'])

		# Return None if no currency information
		if len(list_) == 0:
			return None

		# Return the answer
		return tuple(i for i in list_)

	# Phone number
	def phone(self, root=True, suffix=False):
		# Answer collector
		list_ = []

		# Show root of the phone
		if root:
			list_.append(self.response[0]['idd']['root'])

		# Show suffix of the phone
		if suffix:
			list_.append([i for i in self.response[0]['idd']['suffixes']])

		# Return None if no answer
		if len(list_) == 0:
			return None

		# Return the answer
		return tuple(i for i in list_)

	# Languages
	def languages(self):
		# Answer collector
		list_ = []

		# Get the answer
		for i in self.response[0]['languages'].values():
			list_.append(i)

		# Return the answer
		return tuple(i for i in list_)

	# Maps
	def maps(self, g_map=True, borders=False):
		# Answer collector
		list_ = []

		# Google maps
		if g_map:
			list_.append(self.response[0]['maps']['googleMaps'])

		# Border countries
		if borders:
			for i in self.response[0]['borders']:
				list_.append(i)

		# Return none if there are no infos asked
		if len(list_) == 0:
			return None

		# Return answer
		return tuple(i for i in list_)

	# Domain name
	def domain_name(self):
		# Answer collector
		list_ = []
		list_.append(self.response[0]['tld'][0])

		return tuple(i for i in list_)

	# Capital city
	def capital_city(self):
		return tuple(i for i in self.response[0]['capital'])

	# Flag
	def flag(self):
		return (self.response[0]['flags']['png'],)

	# Car of the country
	def car(self, signs=True, side=False):
		list_ = []

		if signs:
			list_.append([i for i in self.response[0]['car']['signs']][0])

		if side:
			list_.append(self.response[0]['car']['side'])

		if len(list_) == 0:
			return None

		return tuple(i for i in list_)

	# Time zones
	def time_zone(self):
		return tuple(i for i in self.response[0]['timezones'])

	# Continent
	def continent(self, continent=True, sub_continent=False):
		list_ = []

		if continent:
			list_.append(self.response[0]['region'])

		if sub_continent:
			list_.append(self.response[0]['subregion'])

		if len(list_) == 0:
			return None

		return tuple(i for i in list_)

	# Coat of arms
	def coat_of_arms(self):
		return (self.response[0]['coatOfArms']['png'],)

	# Start of week
	def start_week(self):
		return (self.response[0]['startOfWeek'],)


c1 = Country('united states of america')
# print(c1.country_name(official_name=True, short_name=True))
# print(c1.is_(independent=False, un_member=True))
# print(c1.currencies(symbol=True))
# print(c1.phone(suffix=True))
# print(c1.languages())
# print(c1.maps(borders=True))
# print(c1.domain_name())
# print(c1.capital_city())
# print(c1.flag())
# print(c1.car(signs=False))
# print(c1.time_zone())
# print(c1.continent(sub_continent=True))
# print(c1.coat_of_arms())
# print(c1.start_week())
