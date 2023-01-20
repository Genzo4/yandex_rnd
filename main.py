import argparse

from ya_music_rnd import YandexMusicRnd


version = '1.0.0.3'


def parse_args():
    parser = argparse.ArgumentParser(
        prog='ya_music_rnd',
        description='Yandex Music Rnd v.%s' % version + ' (c) 2023 Genzo',
        add_help=False
        )

    parser.add_argument(
        '-max',
        '--max_index',
        type=int,
        default=10000000,
        metavar='max_artist_index',
        help='Максимальный индекс для поиска артиста. По умолчанию: 10000000.')

    parser.add_argument(
        '-no',
        '--dont_open_in_browser',
        action='store_true',
        help='Не открывать найденный результат в браузере, но вывести его на экран'
    )

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        help='Показать версию',
        version='%(prog)s v.{}'.format(version)
    )

    parser.add_argument(
        '-h', '-?',
        '--help',
        action='help',
        help='Показать помощь и выйти из программы'
    )

    args = parser.parse_args()

    if args.max_index < 1:
        parser.exit(1, 'Error: max_index должен быть >= 1')

    return args


def main():
    args = parse_args()

    ya_rnd = YandexMusicRnd(max_int=args.max_index, open_url=not(args.dont_open_in_browser))
    site = ya_rnd.get_artist()

    if args.dont_open_in_browser:
        print(site)


if __name__ == '__main__':
    main()
