import datetime

class Source(object):
  def __init__(self,
                author="Unknown Author",
                publisher="Unknown Publisher",
                date=datetime.date(year=1970,month=1,day=1),
                url=""):
    self.author = author
    self.publisher = publisher
    self.date = date
    self.url = url

