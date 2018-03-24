# Class that defines basic operations on a stock.
import os

import consts as consts
import googlefinance.client as client
import pandas as pd

class Stock(object):
  def __init__(self, stock_symbol, exchange = 'NSE', force_download=False):
    self.__stock_symbol = stock_symbol
    self.__exchange = exchange

    if (force_download):
      self.clean_up()
    
    # Load data frame
    self.get_price_data()

  def get_request_query(self):
    param = {
      'q': self.__stock_symbol,
      'x': self.__exchange,
      'i': '86400', # 1 day interval
      'p': '1Y'
    }
    return param

  def get_data_file_path(self):
    file_path = os.path.join(consts.DATA_DIR, self.__exchange,
                             self.__stock_symbol, consts.DATA_FILE_NAME)
    return file_path

  def get_price_data(self):
    file_path = self.get_data_file_path()
    if not os.path.exists(file_path):
      os.makedirs(os.path.dirname(file_path))
      print 'Querying and fetching stock rates'
      query = self.get_request_query()
      self.__dataframe = client.get_price_data(query)
      self.__dataframe.to_csv(file_path)
    else:
      print 'Using existing data'
      self.__dataframe = pd.read_csv(file_path)

  def clean_up(self):
    file_path = self.get_data_file_path()
    if os.path.exists(file_path):
      os.remove(file_path)

  def get_data_frame(self):
    return self.__dataframe

if __name__ == '__main__':
  stock = Stock('RBLBANK')
  print stock.get_data_frame()
