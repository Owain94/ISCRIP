import re


def fen2grid(fen: str, empty='*') -> str:
    return '\n'.join([''.join([empty * int(y) if y.isdigit() else y for y in x]) for x in fen.split('/')]).strip()


def grid2fen(grid: str, empty='*') -> str:
    return '/'.join(re.sub('\\{}+'.format(empty), lambda x: str(len(x.group(0))), '\n'.join([x.strip() for x in grid.split('\n')])).split('\n'))


def main() -> None:
    print(fen2grid('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'))
    print()
    print(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', '.'))
    print()
    print(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '+'))
    print()

    rooster = '''rnbqkbnr
                 pppppppp
                 ********
                 ********
                 ********
                 ********
                 PPPPPPPP
                 RNBQKBNR'''

    print(grid2fen(rooster))
    print()
    print(grid2fen(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR')))
    print()
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '.'), '.'))
    print()
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R', '+'), '+'))
    print()


if __name__ == '__main__':
    main()
