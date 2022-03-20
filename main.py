from glob import glob
import argparse
from os import rename


def dongdongiscat():
    files = glob(f'*.{args.extension}')
    if not files:
        print('file list empty.')
    print('file list below')
    print(files)
    print('='*15)
    template = '{title} s{season:02d}e{episode:02d}{subtitle}.{extension}'
    
    for file in files:
        new_name = template.format(
                title=args.title,
                season=args.season,
                episode=args.episode,
                subtitle=args.subtitle,
                extension=args.extension
            )
        if not args.dry_run:
            rename(file, new_name)
        print(f'{file} -> {new_name}')
        args.episode += 1


parser = argparse.ArgumentParser(description='a')
parser.add_argument('title', metavar='T', type=str,
                    help='Title')
parser.add_argument('season', metavar='S', type=int,
                    help='season start with')
parser.add_argument('episode', metavar='E', type=int,
                    help='episode start with')
parser.add_argument('extension', metavar='EXT', type=str,
                    help='files extension')
parser.add_argument('--subtitle', required=False, metavar='SUB', type=str,
                    default='', help='subtitle language')
parser.add_argument('--dry-run', required=False, metavar='DRYRUN', type=bool,
                    default=False, help='dry-run')


args = parser.parse_args()

if __name__ == '__main__':
    # print(args)
    dongdongiscat()