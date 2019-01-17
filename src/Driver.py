import os

from pixiv_pixie import PixivPixie

requests_kwargs = {
   'proxies': {
     'https': 'http://127.0.0.1:8888',
   },
   'verify': False,       # PAPI use https, an easy way is disable requests SSL verify
}

USERNAME = "userbay"
PASSWORD = "userpay"

def main():
    pixie = PixivPixie()
    pixie.login(USERNAME,PASSWORD)

    ranking = pixie.ranking()

    counter = 1
    for illust in ranking:
        pixie.download(illust,directory='downloadtest')
        print('{:4}'.format(counter),'{:8}'.format(illust.illust_id),illust.title,sep=' | ',)
        counter = counter + 1







if __name__ == '__main__':
    main()