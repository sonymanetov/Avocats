transform achievement_transform:
    on show:
        xalign .98 
        yalign -.3 
        linear 0.4 xalign .98 yalign .02
    on hide:
        linear 0.4 xalign 1.9 yalign .02

transform update_achievement_transform:
    on show:
        xalign .98 
        yalign -.3 
        linear 0.4 xalign .98 yalign .20
    on hide:
        linear 0.4 xalign 1.9 yalign .20


screen scr_achievement_get(title, a_text, icon, trans=achievement_transform):
    timer 2.4 action Hide("scr_achievement_get")
    window:
        at trans
        background "#333333cc"
        xalign .98
        yalign .02
        xysize (450, 100)
        hbox:
            vbox:
                spacing 10
                image icon
            vbox:
                xoffset 10
                xsize 330
                text title:
                    size 28
                    id title
                text a_text:
                    size 22
                    id a_text

screen scr_achievement_update(title, a_text, icon, cur_prog, max_prog, trans=update_achievement_transform):
    timer 2.4 action Hide("scr_achievement_update")
    window:
        at trans
        background "#333333cc"
        xalign .98
        yalign .02
        xysize (450, 100)

        #

        hbox:
            vbox:
                spacing 10
                image icon
                text "{0}/{1}".format(cur_prog, max_prog):
                    xcenter 0.5 
                    ycenter 0.2
            vbox:
                xoffset 10
                xsize 330
                text title:
                    size 28
                    id title
                text a_text:
                    size 22
                    id a_text


                



init python:
    def get_achievement(ach_id, trans=achievement_transform):
        ach = persistent.achievements_dict[ach_id]
        if ach["unlocked"] is False:
            achievement.grant(ach_id)
            ach["unlocked"] = True
            renpy.show_screen(_screen_name='scr_achievement_get', title=ach['title'],
                              a_text=ach['text'], icon=ach['icon'], trans=trans)
            update_achievement("all_endings")

    def update_achievement(ach_id, to_add=1, trans=update_achievement_transform):
        persistent.achievements_dict[ach_id]["cur_prog"] += to_add
        ach = persistent.achievements_dict[ach_id]

        achievement.progress(ach_id, to_add)
        if ach['cur_prog'] > ach['max_prog']:
            persistent.achievements_dict[ach_id]["cur_prog"] = ach['max_prog']
            ach = persistent.achievements_dict[ach_id]

        if ach['cur_prog'] == ach['max_prog']:
            ach["unlocked"] = True

        renpy.show_screen(_screen_name='scr_achievement_update', title=ach['title'], a_text=ach['text'],
                          icon=ach['icon'], cur_prog=ach['cur_prog'], max_prog=ach['max_prog'], trans=trans)





    # Define your achievements here
    if not persistent.achievements_dict:
        persistent.achievements_dict = {"little_seed": {"type": 0, 
                                                 "title": "Что дальше?",
                                                 "text": "Зависит от меня.",
                                                 "icon": "images/achievements/little_seed.png",
                                                 "unlocked": False
                                                },
                                        "kutushas_adept": {"type": 0, 
                                                 "title": "Адепт Кутуши",
                                                 "text": "Пожертвуйте своим бренным телом ради ясного будущего ваших близких.",
                                                 "icon": "images/achievements/kutushas_adept.png",
                                                 "unlocked": False
                                                },
                                        "smile_of_farewell": {"type": 0, 
                                                 "title": "Улыбка прощанья",
                                                 "text": "Примите и приласкайте собственную пустоту.",
                                                 "icon": "images/achievements/smile_of_farewell.png",
                                                 "unlocked": False
                                                },
                                        "all_endings": {"type": 1, 
                                                 "title": "Суперавакотик",
                                                 "text": "Открыть все концовки.",
                                                 "icon": "images/achievements/super_avocat.png",
                                                 "cur_prog": 0,
                                                 "max_prog": 3,
                                                 "unlocked": False
                                                }
                                        }
                                        

        for i, a in persistent.achievements_dict.items():
            if a['type'] == 0:
                achievement.register(i, steam=a['title'])
            if a['type'] == 1:
                achievement.register(i, steam=a['title'], stat_max=a['max_prog'])
