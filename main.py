import argparse

from ya_music_rnd import YandexMusicRnd


version = '1.1.0'


def parse_args():
    parser = argparse.ArgumentParser(
        prog='ya_music_rnd',
        description='Yandex Music Rnd v.%s' % version + ' (https://github.com/Genzo4/yandex_rnd) (c) 2024 Genzo',
        add_help=False
        )

    parser.add_argument(
        '-ha',
        '--have_albom',
        type=str,
        choices=['yes', 'no', 'all'],
        default='all',
        help='Искать исполнителя, у которого есть альбомы. По умолчанию: all'
    )

    parser.add_argument(
        '-hs',
        '--have_similar',
        type=str,
        choices=['yes', 'no', 'all'],
        default='all',
        help='Искать исполнителя, у которого есть похожие. По умолчанию: all'
    )

    parser.add_argument(
        '-hc',
        '--have_clips',
        type=str,
        choices=['yes', 'no', 'all'],
        default='all',
        help='Искать исполнителя, у которого есть клипы. По умолчанию: all'
    )

    parser.add_argument(
        '-c',
        '--clear',
        type=str,
        choices=['yes', 'no', 'all'],
        default='no',
        help='Искать исполнителя, у которого нет произведений. Имеет приоритет над -ha, -hs, -hc. По умолчанию: no'
    )

    parser.add_argument(
        '-max',
        '--max_index',
        type=int,
        default=10000000,
        metavar='max_artist_index',
        help='Максимальный индекс для поиска артиста. По умолчанию: 10000000.'
    )

    parser.add_argument(
        '-long',
        '--max_iterations',
        type=int,
        default=60,
        help='Максимальное количество итераций поиска. По умолчанию: 60. Каждая итерация занимает примерно 2 сек.'
    )

    parser.add_argument(
        '-no',
        '--dont_open_in_browser',
        action='store_true',
        help='Не открывать найденный результат в браузере, но вывести его на экран'
    )

    parser.add_argument(
        '-np',
        '--no_progress',
        action='store_true',
        help='Не выводить прогресс поиска'
    )

    parser.add_argument(
        '-q',
        '--quiet',
        action='store_true',
        help='Ничего не выводить на экран'
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
        parser.exit(1, 'Error: параметр max_index должен быть >= 1')

    if args.max_iterations < 1:
        parser.exit(2, 'Error: параметр max_iterations должен быть >= 1')

    return args


def main():
    args = parse_args()

    ya_rnd = YandexMusicRnd(
        max_index=args.max_index,
        open_url=not args.dont_open_in_browser,
        max_iterations=args.max_iterations,
        find_clear=args.clear,
        find_have_albom=args.have_albom,
        find_have_similar=args.have_similar,
        find_have_clips=args.have_clips,
        show_progress=not args.no_progress,
        quiet=args.quiet
        )

    site = ya_rnd.get_artist()

    if not args.quiet:
        print(site)


if __name__ == '__main__':
    main()
