﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

init:

    define gizmo = Character('Гизмо', color="#eeeeee")
    define reo = Character('Рео', color="#eeeeee")
    define lorenzo = Character('Лоренцо', color="#eeeeee")

    $ bio_points = 0
    $ kutusha_points = 0
    $ stranger_points = 0


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.

# Игра начинается здесь:
label start:

    scene start_background

    show reo at right

    reo "Эй, братишка..."

    show reo_scared at right

    reo "Гизмо, ты меня слышишь?"
    reo "Мы искали тебя два солнца подряд! Прошу вставай..."

    scene start_background

    menu:
        "Это... Рео? Почему так болит всё тело?" 
        "Сказать Рео о боли": 
            "Я сам испугался своего шипяще-хрипящего голоса"
            gizmo "Я не уверен, что в состоянии сейчас встать."
            show reo at right
            reo "Давай помогу"
        "Молчаливо собраться с мыслями":
            pass                  

    show reo_shoked at right

    reo "Т-т-ты... т-твоя..."

    "Рео смотрела на меня с ужасом, застывшим в её глазах. Я никогда не видел её такой напуганной"

    scene start_background

    "Плавно опустив глаза вниз я осознал ужасное..."

    show gizmo_shoked at left

    gizmo "Моя кость?! Где моя косточка?!"
    gizmo "Рео? Где мы?!"

    show gizmo_scared at left

    gizmo "Я ничего не понимаю, а еще ничего не помню!"

    scene start_background 

    "Я почувствовал боль и пустоту одновременно. Невыносимое ощущение диссонанса."
    "Рео всё также с ужасом и удивлением рассматривала меня"

    show reo_shoked at right
    with dissolve

    reo "Гизмо, братец, давай лучше уйдём отсюда. Надо быстрее найти остальных, они тоже тебя ищут."


    scene foggy_avovillage
    with fade

    show reo at right
    reo "Лоренцо, я нашла его!"

    scene foggy_avovillage

    show lorenzo at right
    lorenzo "Ну наконец-то, где ты был, Гизмо?"

    show lorenzo_shoked at right

    scene foggy_avovillage

    "Всё-таки он сумел разглядеть меня сквозь толщу тумана."
    "Молчит..."
    menu:
        "Видимо, стоит первому начать диалог" 
        "Молчишь, потому что не знаешь, что сказать, или потому что говорить нечего?":
            show lorenzo at right
            "Его лицо тут же приняло привычный вид."
            lorenzo "Опять шуточки шутишь по поводу и без? Кто это тебя так?"
        "Что произошло два солнца назад?":
            show lorenzo at right
            lorenzo "Я надеялся, ты сможешь дать ответ на этот вопрос... Но, похоже, ты и сам знаешь не больше, чем мы."
            
    scene foggy_avovillage

    show reo_shoked at right

    reo "Я помню, что в тот день туман был особо наэлектризован, а небо висело почти над самой головой."
    reo "Я была в лесу, когда начался шторм. Когда я добежала до деревни, там были все, кроме тебя, Гизмо."

    show lorenzo at right

    lorenzo "Да, мы решили, что опасно будет посылать кого-либо за тобой, поэтому просто ждали, пока погода утихомирится."
    lorenzo "На моей памяти ни разу не было ветров. Туман всегда стоял неподвижной липкой стеной, прямо как сейчас."

    scene foggy_avovillage

    show gizmo_upset at left

    gizmo "Ты когда-нибудь видел что-то подобное?"

    scene foggy_avovillage

    "Произнес я, указывая на углубление в своём животе."
    "Лоренцо лишь отрицательно покачал головой. Жаль."

    scene foggy_road

    "Мы шли молча, лишь изредко Рео ловила мой взгляд и печально улыбалась мне."
    "С каждым шагом казалось, будто дыра во мне увеличивается, и живого от меня остается всё меньше и меньше."

    show gizmo_upset at left

    menu:
        "Меня всю дорогу мучил вопрос..." 
        "В этом тумане нет никого, кроме нас. Откуда мы вообще здесь взялись?":
            "Я, Рео, Лоренцо, другие жители деревни... Мы как будто бы всегда тут были, но ведь Солнце же когда-то не светило?"
            "Почему я раньше об этом не задумывался? Почему туман в моей голове такой же густой, как вокруг неё?"
            $ bio_points += 1
        "Кто мог бы знать, что со мной произошло?":
            "Может, я вообще могу прямо сейчас умереть, но даже не подозреваю этого?"
            "Не могу поверить в то, что я первый, кто столкнулся с этим..."
            $ kutusha_points += 1
        "Что за чертовщина с этим туманом?":
            "Я не помню не единого дня, чтобы тумана не было. Он совершенно неподвижен."
            "Интересно, что скрывается за ним? Я слышал, что из него можно вернуться обратно в деревню, либо же не вернуться никогда..."
            $ stranger_points += 1

    scene foggy_house

    show lorenzo at right

    lorenzo "Так, давай осмотрим твое ранение, щербатый. Оно болит?"
    lorenzo "Хотя, дурацкий вопрос, по твоей морде видно, что болит. Лучше опиши, какая это боль?"

    show gizmo upset at left

    gizmo "Болит все тело..."

    menu:
        "На что же похожа эта боль?" 
        "Чувствуется очень интенсивно. Острая боль при ходьбе, а при бездействии - ноющая":
            $ bio_points += 1
        "Во мне как будто разбилась стеклянная ваза, а ее осколки впились в меня.":
            $ kutusha_points += 1
        "Мне сложно подобрать хорошее крепкое слово, Лоренцо.":
            $ stranger_points += 1



    return
