from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bsoup
from productModelBase import ProductModelBase
import re

def Main():
  url = "https://www.corotos.com.do"

  #open connection and reads content
  client = uReq(url)
  content = client.read()

  # close connection
  client.close()

  # parse content to soup
  soupedContent = bsoup(content, "html.parser")

  # to find
  # soupedContent.findAll("<tagname>", {"property":"value"})
  #for example
  # soupedContent.findAll("div", {"class":"item"})

  # using parse, tag["property"] = value
  # soupedContent.div.div["property"]
  # example:
  # soupedContent.div.img["src"]

  # container class "div", {"class":"_3_VJn _2h9MX"}
  # container = soupedContent.find("div", {"class":"_3_VJn _2h9MX"})
  # print(dir(container))
  products = soupedContent.findAll("div", {"class":"DbXTC _2pm69 _1JgR4 QF_XG"})
  print("Found products ", len(products))
  # print("thumbnail", dir(products[0].a.div.find("div", {"class":"_1xvFo"})["style"]))
  # /listings/celulares-y-tabletas-186/25c04925-8643-4156-a7e9-b3b35491f211/iphone-8-plus-64gb-factory

  productObjects = []

  for product in products:
    # href format
    # /listings/<category-<id>>/<publication id>/<posible title -<id>
    href = product.a["href"]
    fullLink = url + href
    hashId = getHashId(href)
    category = splitListingUrl(href)[2] or ""

    thumbnailDiv = product.a.div.find("div", {"class":"_1xvFo"})
    thumbailStyle = thumbnailDiv["style"]
    thumbnailUrl = ""

    found = re.search('background-image:url\((.*)\)', thumbailStyle, re.IGNORECASE)
    if found:
      thumbnailUrl = found.group(1)

    infoDiv = product.a.div.find("div", {"class":"_32PML"})
    priceTag = infoDiv.find("span",{"data-name":"price"})
    titleTag = infoDiv.find("h2",{"data-name":"ad-title"})

    productObject = ProductModelBase(titleTag.string, priceTag.string, href, fullLink, hashId, thumbnailUrl, category)
    
    print(productObject)
    # print(thumbnailUrl)
    # print("thumbnail", dir(thumbnailDiv["style"]))
    # print(fullLink)
    
    # load more button " button data-name="load_more""

def splitListingUrl(listingUrl):
  return listingUrl.split("/")

def getHashId(listingUrl=""):
  # /listings/category/hash-id/title
  # for example: 
  # /listings/celulares-y-tabletas-186/25c04925-8643-4156-a7e9-b3b35491f211/iphone-8-plus-64gb-factory
  
  _, listingStr, category, hashId, title = splitListingUrl(listingUrl)
  return hashId or ""

Main()