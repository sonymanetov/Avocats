# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

init:

    define gizmo = Character('Гизмо', color="#eeeeee")
    define reo = Character('Рео', color="#eeeeee")
    define lorenzo = Character('Лоренцо', color="#eeeeee")
    define bite = Character('Байт', color="#eeeeee")

    $ bio_points = 0
    $ kutusha_points = 0
    $ stranger_points = 0


# Reo
image reo scared = "reo_scared.png"
image reo shoked = "reo_shoked.png"

# Gizmo
image gizmo shocked = "gizmo_shoked.png"
image gizmo scared = "gizmo_scared.png"
image gizmo upset = "gizmo_upset.png"

# Lorenzo
image lorenzo shoked = "lorenzo_shoked.png"
image lorenzo happy = "lorenzo_happy.png"

# Игра начинается здесь:
label bio_branch:

    scene foggy_house

    "Лоренцо и странно Рео переглянулись."

    show lorenzo at right

    lorenzo "Байт слишком хотел тебя видеть, и он, кажется, отправился бродить по городу в поисках тебя."

    lorenzo "Советую сейчас отправиться к нему."

    hide lorenzo

    "Я встал c мягких одеял."

    show gizmo at left

    gizmo "Я сам до него дойду. Спасибо, Лоренцо."

    hide gizmo

    scene foggy_avovillage with fade

    show gizmo upset at left

    gizmo "Вроде бы я не так давно общался с Байтом, но, такое чувство, будто мы не виделись сотни Солнц."

    show gizmo shocked at left
    with faster_dissolve

    gizmo "Байт! Привет! Подойди сюда!"

    hide gizmo 

    show bite shocked at right 

    bite "Гизмо! Я как раз хотел бы с тобой пообщаться! Пойдем ко мне."

    hide bite

    scene bites_home with fade

    show bite at right 

    bite "Ты - единственный в своем роде экземпляр. Я считаю, что мы должны провести исследование, но они меня даже слушать не хотят!"
    bite "Они говорят, что я свихнулся, но я не свихнулся. Я, кажется, начал понимать, кто мы."

    hide bite  

    show gizmo at left

    gizmo "Стоп-стоп-стоп... Давай по-порядку. По дороге ты говорил, что мы должны подойти с научной точки зрения к вопросу..."

    hide gizmo 

    show bite shocked at right 

    bite "Да, поэтому начнем с теории. Ты же понимаешь, что ты потерял?"

    hide bite  

    show gizmo scared at left

    gizmo "Ну да, косточку, практически треть своего тела, Байт, что за вопросы?"

    hide gizmo 

    show bite shocked at right 

    bite "В том-то и дело! Ты потерял семечко, щербатый! А это значит, что скоро из него вырастет дерево!"

    hide bite  

    "Он продолжает свою безумную речь. В моей голове крутится с библиейской скоростью по слогам лишь одно слово - семечко. Я его посеял?"

    show gizmo scared at left

    gizmo "Байт, остановись. Лучше пойдем, я хочу вернуться на то место, где я очнулся несколько Солнц назад."

    scene start_background with fade

    "Кругом туман, он стелется под ногами, проникает под кожу, завязывает глаза."
    "Едва залитая солнцем скала - место, где я проснулся. Только сейчас я ощутил себя дураком."
    "Как я раньше не додумался вернуться сюда и осмотреться?"
    "Я был так поражен собственной болью, что отказался от того, чтобы дать себе шанс увидеть."

    scene seed with fade 

    "Я едва ли получy ответ на свои вопросы, но здесь есть место чему-то большему. Увидеть и принять, предвосхитить восхождение чего-то нового."
    "Пусть оно даже и не является больше частью меня..."

    scene black with fade
    $ get_achievement("little_seed", trans=achievement_transform)
    centered "Что дальше? Зависит от меня."

    return
