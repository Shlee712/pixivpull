#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from pixivpy3 import *

_USERNAME = "userbay"
_PASSWORD = "userpay"
_PIXIVID = 6622945
#IVID = 12904278


_REQUESTS_KWARGS = {
  # 'proxies': {
  #   'https': 'http://127.0.0.1:8888',
  # },
  # 'verify': False,       # PAPI use https, an easy way is disable requests SSL verify
}

def main():
    aapi = AppPixivAPI(**_REQUESTS_KWARGS)
    
    aapi.login(_USERNAME, _PASSWORD)
    
    # grabs the first 30 pictures of the pixivid's most recent bookmarks
    json_result = aapi.user_bookmarks_illust(_PIXIVID,restrict='public');

    directory = "dl"
    directory2 = "gridman"
    tag = False
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    if not os.path.exists(directory2):
        os.makedirs(directory2)

    for illust in json_result.illusts[:None]:
        tag = False
        image_url = illust.meta_single_page.get('original_image_url', illust.image_urls.large)
        
        print("%s: %s" % (illust.title, image_url))
        # aapi.download(image_url)
        thislist = illust.tags
        url_basename = os.path.basename(image_url)
        extension = os.path.splitext(url_basename)[1]
        name = "illust_id_%d_%s%s" % (illust.id, illust.title, extension)
        name = name.replace("/","_")
        
        for dic in thislist[:None]:
            if  dic.name == "SSSS.GRIDMAN":
                aapi.download(image_url, path=directory2, name=name)
                tag = True
                break
        if  tag == False:
            aapi.download(image_url, path=directory, name=name)
        
        
    #moves on to the next 30 most recent bookmarks
    next_qs = aapi.parse_qs(json_result.next_url)
    if  next_qs != None:
        json_result = aapi.user_bookmarks_illust(**next_qs)
        downloadImages(aapi,json_result,directory)
        
    else:
        print("\nNo more images to be found")
        
        
    
def downloadImages(aapi,json_result,directory):
    for illust in json_result.illusts[:None]:
        image_url = illust.meta_single_page.get('original_image_url', illust.image_urls.large)
        print("%s: %s" % (illust.title, image_url))
        # aapi.download(image_url)
        url_basename = os.path.basename(image_url)
        extension = os.path.splitext(url_basename)[1]
        name = "illust_id_%d_%s%s" % (illust.id, illust.title, extension)
        aapi.download(image_url, path=directory, name=name)
        
if __name__ == '__main__':
    main()
        