import os

from pixiv_pixie import PixivPixie

requests_kwargs = {
    # You may need to use proxies.
    # 'proxies': {
    #     'https': 'http://127.0.0.1:8888',
    #  },
    # PixivPy's PAPI use https, an easy way is disable requests SSL verify.
    # 'verify': False,
}


def print_illusts(illusts, limit=10):
    try:
        for idx, illust in enumerate(illusts):
            if limit is not None and idx >= limit:
                break
            print(
                '{:4}'.format(idx),
                '{:8}'.format(illust.illust_id),
                '{:>4}×{:<4}'.format(illust.width, illust.height),
                illust.title,
                sep=' | ',
            )
    except Exception as e:
        print(e)


def main():
    pixie = PixivPixie(**requests_kwargs)

    # You MUST login first.
    # Replace it with your own account.
    pixie.login('userbay', 'userpay')

    # Fetch single illust
    illust = pixie.illust(63808518)
    print_illusts([illust])

    # Fetch following users' new illusts
    print_illusts(pixie.my_following_illusts())

    # Fetch user's illusts
    print_illusts(pixie.user_illusts(2188232))

    # Fetch ranking illusts
    print_illusts(pixie.ranking())

    # Search illusts
    print_illusts(pixie.search('オリジナル'), limit=50)

    # Fetch related illusts
    print_illusts(pixie.related_illusts(63808518), limit=50)

    # Download illust
    pixie.download(illust, directory='download')

    # Download ugoira and manually convert it
    illust = pixie.illust(64421170)
    pixie.download(
        illust, directory='download', name='ugoira{ext}',
        convert_ugoira=False,
    )
    pixie.convert_zip_to_gif(
        input_file=os.path.join('download','ugoira.zip'),
        frame_delays=illust.frame_delays,
        output_file='ugoira.gif'
    )


if __name__ == '__main__':
    main()