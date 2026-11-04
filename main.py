from character import Character
def main():
    hero = Character("Knight", 30, 5)
    enemy1 = Character("Goblin", 20, 3)
    enemy2 = Character("Orc", 25, 4)
    enemies = [enemy1, enemy2]

    print(hero)
    for enemy in enemies:
        print(enemy)
    print()

    while hero.is_alive() and any(e.is_alive() for e in enemies):
        # hero โจมตีศัตรูตัวแรกที่ยังมีชีวิตอยู่
        for enemy in enemies:
            if enemy.is_alive():
                hero.attack(enemy)
                break

        # ศัตรูที่ยังรอดทุกตัวโจมตีกลับ (ถ้า hero ยังไม่ตาย)
        for enemy in enemies:
            if enemy.is_alive() and hero.is_alive():
                enemy.attack(hero)

        print(hero)
        for enemy in enemies:
            print(enemy)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("The enemies win!")


if __name__ == "__main__":
    main()