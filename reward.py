import numpy as np

def reward(seq, query):
   '''
   seq: sequence of words in listing
   query: search query

   takes every word in listing and checks if it is in query 
   (length of listing has minimal impact)
   '''

   return np.mean([1 if word in query.split() else 0 for word in seq.split()]) # One-liner!!!

# Test out both good and bad English translations of inputted Spanish query
queries = [
   { # Good
      'eng': 'bright yellow rain boots',
      'esp': 'botas de lluvia amarillas brillantes'
   }, { # Bad
      'eng': 'boots from brilliant yellow rain',
      'esp': 'botas de lluvia amarillas brillantes'
   }
] 

# Top 3 listings from searches on ebay for each translated-to-English query 
# (translated to Spanish with Google)
listings_good = [
   {
      'eng': 'Resist Bright Yellow Water Resistant Lug Sole 5" Chunky Block Heels Knee Boots',
      'esp': 'Resist botas hasta la rodilla con suela gruesa resistente al agua de color amarillo brillante de 5\"'
   }, {
      'eng': 'Okabashi Toddler Kendall Bright Yellow Machine Washable Rain Boots Size 8 B293',
      'esp': 'Okabashi Toddler Kendall Amarillo brillante Botas de lluvia lavables a máquina Tamaño 8 B293'
   }, {
      'eng': 'Seven7 Womens Dover Bootie Chelsea Rain Boots Yellow Black Rubber Pull On 9 New',
      'esp': 'Seven7 Mujeres Dover Bootie Chelsea Botas de lluvia Amarillo Negro Caucho Pull On 9 Nuevo'
   }
]

listings_bad = [
   {
      'eng': 'Shoes Women\'s Rain Boots Rubber Pull On Garden 8 Colors Size 6-11',
      'esp': 'Zapatos Botas De Lluvia De Mujer Caucho Pull On Garden 8 Colores Talla 6-11'
   }, {
      'eng': 'New Women\'s Waterproof Short Ankle Rubber Rain Boots',
      'esp': 'Novedades Botas impermeables de lluvia de goma tobilleras cortas para mujer'
   }, {
      'eng': 'Seven7 Womens Dover Bootie Chelsea Rain Boots Yellow/Black Rubber Pull On 8 New',
      'esp': 'Seven7 Mujeres Dover Bootie Chelsea Botas de lluvia Amarillo Negro Caucho Pull On 9 Nuevo'
   }
]


# Note: case matching not specified, other preprocessing unspecified 
# Note: No tokenization? Simple word matching seems a bit naive, especially if extrapolating to other languages
# Green text indicates passing the 90% constraint, red text indicates being filtered out
for listing in listings_good:
   color = '\033[1;32m' if np.mean([word in listing['eng'].lower().split() for word in queries[0]['eng'].split()]) > 0.9 else '\033[1;31m'
   print(f"{color}[90% check]\033[0m [Good Translation] \n\tRecall: {reward(listing['esp'].lower(), queries[0]['esp'])}\n\tQuery: {queries[0]['esp']}\n\tListing: {listing['esp']}")
for listing in listings_bad:
   color = '\033[1;32m' if np.mean([word in listing['eng'].lower().split() for word in queries[1]['eng'].split()]) > 0.9 else '\033[1;31m'
   print(f"{color}[90% check]\033[0m [Bad Translation] \n\tRecall: {reward(listing['esp'].lower(), queries[1]['esp'])}\n\tQuery: {queries[1]['esp']}\n\tListing: {listing['esp']}")

# Problems with this approach:
#  - query translation qualtiy seems to have little impact as long as it is close enough; basically, this 
#    might be overzealous in what is acceptable, because at the end of the day, you can get yellow rain 
#    boots in the worst case here. However, it does make for an extremely high quality dataset
#  - since listings are going to be very different anyway, we aren't expecting 
#    very good scores (consider biasing values)

# What comes next?
#  - these recall scores are used as a reward for training in reinforcement learning

# Questions, then Live demo of how it actually works if time permits

##########
# Live Demo
######

# Pick a query in any non-English language
query = ''

# Translate query to English
query_eng = ''

# Search query on Ebay, then translate the top results back into non_English. Collect clicked listing
listing_eng = ''
listing = ''

# Print results (ucomment print)
color = '\033[1;32m' if np.mean([word in listing_eng.lower().split() for word in query_eng.split()]) > 0.9 else '\033[1;31m'
# print(f"\n{color}[90% check]\033[0m Recall: {reward(listing.lower(), query)}\n\tQuery: {query}\n\tListing: {listing}")