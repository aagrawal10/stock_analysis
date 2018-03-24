from nsetools import Nse
from stock import Stock

nse = Nse()
get_all_indices = nse.get_stock_codes()
for key in get_all_indices.keys():
  stock = Stock(key)

