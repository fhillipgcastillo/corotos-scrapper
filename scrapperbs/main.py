from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bsoup
from productModelBase import ProductModelBase
import re
import requests


def getHtmlContentWithUrlOpen(url):
  #open connection and reads content
  client = uReq(url)
  print("Requesting url", url)
  content = client.read()
  print("Reading content")

  # close connection
  client.close()
  return content

def getHtmlContentWithRequests(url):
  # using requests lib
  headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
  }
  content = ""
  try:
    req = requests.get(url, headers=headers, timeout=10)
    if req.status_code == 200:
      content = req.text
  except Exception as ex:
      print(str(ex))
  finally:
      print("finished with requests lib")

  return content

def Main():
  url = "https://www.corotos.com.do"
  # content = getHtmlContentWithUrlOpen(url)
  
  # More faster that UrlOpen
  content = getHtmlContentWithRequests(url)

  # parse content to soup
  soupedContent = bsoup(content, "html.parser")
  print("Parsing content")

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
  print("Parsing data")
  
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
    
    # print(productObject)
    # print(thumbnailUrl)
    # print("thumbnail", dir(thumbnailDiv["style"]))
    # print(fullLink)
    
    # load more button " button data-name="load_more""
  print("finished")
  
def splitListingUrl(listingUrl):
  return listingUrl.split("/")

def getHashId(listingUrl=""):
  # /listings/category/hash-id/title
  # for example: 
  # /listings/celulares-y-tabletas-186/25c04925-8643-4156-a7e9-b3b35491f211/iphone-8-plus-64gb-factory
  
  _, listingStr, category, hashId, title = splitListingUrl(listingUrl)
  return hashId or ""

Main()
# sleep for x time and re-run
