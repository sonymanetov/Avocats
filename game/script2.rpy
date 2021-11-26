# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

init:

    define gizmo = Character('Гизмо', color="#eeeeee")
    define reo = Character('Рео', color="#eeeeee")
    define lorenzo = Character('Лоренцо', color="#eeeeee")

    $ bio_points = 0
    $ kutusha_points = 0
    $ stranger_points = 0


# Reo
image reo scared = "reo_scared.png"
image reo shoked = "reo_shoked.png"

# Gizmo
image gizmo shoked = "gizmo_shoked.png"
image gizmo scared = "gizmo_scared.png"
image gizmo upset = "gizmo_upset.png"

# Lorenzo
image lorenzo shoked = "lorenzo_shoked.png"
image lorenzo happy = "lorenzo_happy.png"

# Игра начинается здесь:
label bio_branch:

    scene foggy_house

    gizmo "Это звучит интересно"

    return