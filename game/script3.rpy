# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

init:

    define gizmo = Character('Гизмо', color="#eeeeee")
    define reo = Character('Рео', color="#eeeeee")
    define lorenzo = Character('Лоренцо', color="#eeeeee")
    define kutusha = Character('Кутуша', color="#eeeeee")

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
label kutusha_branch:

    scene foggy_house

    "Я всеми силами пытался сосредоточиться на своих ощущениях, но в голове гудело лишь одно слово - Кутуша"

    show gizmo 
    
    gizmo "Я, пожалуй, рискну и..."

    hide gizmo

    "Меня резко прервали."

    show lorenzo shoked at right

    lorenzo "Ты серьезно хочешь иметь дело с Кутушей? У тебя вместе с костью мозги выпали?"

    hide lorenzo

    show reo scared at right

    reo "Лоренцо! Следи за языком, это так грубо!"

    show reo at right

    reo "Если ты хочешь пойти к Кутуше, то я могу отправиться с тобой, Гизмо!"

    hide reo 

    "Я кивнул Лоренцо на прощание, и мы отправились за ответами к Кутуше."

    scene foggy_road with fade

    "Кутуша... Никто до конца не понимает, что это за сущность. Она находится в суперпозиции, снаружи всех измерений, внутри каждого из существующих мозгов."
    "Все побаиваются ее, но при этом не пытаюся от нее избавиться."
    "Лишь редкие отчаявшиеся готовы рискнуть и отправиться на ее поиски, чтобы задать вопрос."
    "Она знает ответы на все вопросы, но каждый ответ имеет свою цену."

    scene logovo with fade

    show reo at right


    reo "Гизмо, должно быть мы на месте..."
    
    show reo shoked at right

    with faster_dissolve

    reo "ШТУША-КУТУША-СТРАШНЫЙ-ЗВЕРЬ, ВЫХОДИ!!!!!"

    hide reo

    "Стены начали дрожать. Земля тоже."

    show kutusha at right

    kutusha "С чЕм ПоЖаЛоВаЛи, ГоСпОдА?"

    hide kutusha

    "Я в жизни не мог подумать, что увижу когда-либо такое неописуемо величественное существо."

    show gizmo upset at left

    gizmo "Госпожа Кутуша, до меня дошла весть, что вы знаете ответы на многие вопросы..."

    hide gizmo

    scene black with fade

    centered "Я в красках рассказал ей события последних дней."

    scene logovo with fade

    show kutusha at right

    kutusha "ШтОш, МоЙ дРуГб, МнЕ иЗвЕсТнО сУщЕе..."
    kutusha "Если серьезно, то твоя травма - ключ к избавлению от тумана. Идем, я всё покажу."

    hide kutusha

    scene pics with fade

    kutusha "Посмотри на это изображение. Я живу практически целую бесконечность здесь, в логове, но эти изображения - единственное, что появилось здесь раньше меня."
    kutusha "Серп разливается золотым светом на радостную землю... Но наше солнце больше не дарит улыбок, не правда ли, Гизмо?"

    show kutusha at right

    kutusha "Погляди внимательнее на свою вмятину. Она совершенно такая же, как серп на древней фреске. Что скажешь, а?"

    hide kutusha

    "Рео была поражена происходящим, был слышен лишь стук ее сердца, отскакивающий эхом от стен пещеры."

    show gizmo scared at left

    gizmo "Я верно понял всю эту аналогию с серпом, золотом и мною?"

    hide gizmo

    "Я твёрдо для себя решил, что буду делать дальше. Я взглянул на Рео."

    show gizmo upset at left

    gizmo "Рео, передай Лоренцо и всем остальным в деревушке, что всё в порядке."
    gizmo "Спасибо за всё, что ты для меня сделала..."

    hide gizmo

    show reo at right

    reo "Я никогда не забуду тебя, Гизмо. Лишь бы всё было не зря."

    hide reo

    "Я отвернулся и услышал звук удаляющихся лап. Я поднял глаза на Кутушу. Говорит ли она правду, или просто заманивает меня в ловушку? Боюсь, я уже никогда не узнаю."

    scene pics with fade

    "Последнее, что я вижу - рисунок серпа и резвые демонические клыки."

    scene black with fade

    centered "Хочется верить, что туман и вправду расступился над нашей деревней. Жаль, я не смогу об этом узнать."

    scene clear_sky with fade

    $ get_achievement("kutushas_adept", trans=achievement_transform)
    ""

    return
