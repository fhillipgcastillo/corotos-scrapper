class ProductModelBase:
  def __init__(self, title="", price="", listingPath="", fullUrl="", hashId=""):
    self.hashId = hashId
    self.title = title
    self.price = price
    self.listingPath = listingPath
    self.fullUrl = fullUrl
  
  def __str__(self):
    return self.hashId+" "+self.title

 
