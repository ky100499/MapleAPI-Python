import MapleAPI

def main():
    import sys

    for name in sys.argv[1:]:
        for skill in MapleAPI.character.skill(name)['data']['character_skill']:
            if skill['skill_name'] == "연합의 의지":
                print(f'{name}: O')
                break
        else:
            print(f'{name}: X')

    # print(MapleAPI.character.stat(name))

    # print(MapleAPI.utils.power(name))

    # name1 = sys.argv[1]
    # name2 = sys.argv[2]
    # pow1 = MapleAPI.utils.power(name1)
    # pow2 = MapleAPI.utils.power(name2)

    # print(f'{name1} = {round(pow1/pow2, 2)} {name2}')



if __name__=='__main__':
    main()
