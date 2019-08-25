class ProductModelBase:
  def __init__(self, title="", price="", listingPath="", fullUrl="", hashId="", thumbnailUrl="", category=""):
    self.hashId = hashId
    self.title = title
    self.price = price
    self.listingPath = listingPath
    self.fullUrl = fullUrl
    self.thumbnailUrl = thumbnailUrl
    self.category = category

  def __str__(self):
    return self.hashId+" "+self.title

  def getJsonString(self):
    return "{title:"+self.title+", price:"+self.price+", hashId:"+self.hashId+", listingPath:"+self.listingPath+", fullUrl:"+self.fullUrl+", thumbnailUrl:"+self.thumbnailUrl+" }"
