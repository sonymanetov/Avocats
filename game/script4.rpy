init:

    define gizmo = Character('Гизмо', color="#eeeeee")
    define reo = Character('Рео', color="#eeeeee")
    define lorenzo = Character('Лоренцо', color="#eeeeee")

# Gizmo
image gizmo shocked = "gizmo_shoked.png"
image gizmo scared = "gizmo_scared.png"
image gizmo upset = "gizmo_upset.png"

# Lorenzo
image lorenzo shoked = "lorenzo_shoked.png"
image lorenzo happy = "lorenzo_happy.png"

# Игра начинается здесь:
label stranger_branch:

    "Мне не давала моя боль - физическая и душевная. Мне также не давал покоя туман - туман в моей голове и за её пределами."

    show gizmo at left

    gizmo "Лоренцо, Рео, я, наверное, пройдусь по деревне. Душновато в помещении."

    hide gizmo

    scene foggy_avovillage with fade

    "Домики... Я был в каждом из них. Они остаются прежними, хотя Солнца проходят тысячами."
    "Однажды Андреа пытался покинуть деревню, ушел в туман, но вернулся спустя много Солнц изможденный, голодный и шокированный тем фактом, что он вернулся туда, откуда вышел."
    "Сейчас он занимается изготовлением ржаных лепешек и не любит вспоминать эту историю. Забавно."

    scene foggy_road with fade

    "Мне больше нечего терять. Я ощущаю себя таким же пустым и липким, будто туман. Туман снится мне по ночам, не дает мне спокойно жить."
    
    scene foggy_house with fade

    show gizmo at left

    gizmo "Лоренцо, я должен покинуть деревню ненадолго, я чувствую это."

    hide gizmo

    show lorenzo at right

    lorenzo "Как знал, что ты вернёшься и выдашь вот это вот."

    hide lorenzo

    "Мы несколько минут сверлили друг друга взглядами"

    show lorenzo at right

    lorenzo "Если чувствуешь, что тебя оттуда кличут - иди. Но не смей забывать то, откуда ты пришёл."

    hide lorenzo

    "Лоренцо с мокрыми глазами обнял по-отцовски меня. Я обнял его в ответ."

    show gizmo at left

    gizmo "Где Рео?"

    hide gizmo

    show lorenzo at right

    lorenzo "Ушла за эдельвейсами для новой порции настойки. Не ищи её, не делай больно."

    hide lorenzo

    "Я вышел из домика Лоренцо. Не оглядываясь свернул с кирпичной тропинки прямо в гущу тумана."

    scene black with fade

    show lorenzo happy

    "Мне мерещились их улыбки."

    hide lorenzo

    show reo

    "Они будут улыбаться мне в моих воспоминаниях до конца моих дней."

    hide reo

    scene external_fogg with fade

    "Лишь приняв внутреннюю пустоту, я смог ощутить невесомость. Стать туманом, росой на лютиках, пением птицы. Всё это было во мне - в авокотике без косточки."

    scene sun with fade
    $ get_achievement("smile_of_farewell", trans=achievement_transform)

    "Примирение со стихией внутри себя - единственная сила, способная обуздать стихию вокруг себя."

    return