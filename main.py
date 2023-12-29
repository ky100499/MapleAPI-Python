import MapleAPI

def main():
    import sys

    name = sys.argv[1]

    print(MapleAPI.character.stat(name))

    print(MapleAPI.utils.power(name))

    # name1 = sys.argv[1]
    # name2 = sys.argv[2]
    # pow1 = MapleAPI.utils.power(name1)
    # pow2 = MapleAPI.utils.power(name2)

    # print(f'{name1} = {round(pow1/pow2, 2)} {name2}')

if __name__=='__main__':
    main()
