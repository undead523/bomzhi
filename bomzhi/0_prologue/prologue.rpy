label bomzhi_team:
    
    $ sunset_time()
    $ backdrop = "epilogue"
    $ new_chapter(-1, u"День ...")
    $ renpy.pause(3, hard=True)
    scene black with dissolve
    $ renpy.pause(2, hard=True)
    window show
    scene bg home_oleg with dissolve
    play music music_list["two_glasses_of_melancholy"] fadein 1

    "7 июля 2018 года."
    "Все хикканы собрались у Алеха что-то там отмечать."
    "И всё опять было по-старому: юноши накупили алкоголя, газировки, чипсов, а Ржавый додумался прикупить ещё и кольца кальмара."
    "Как говорится, same shit, different day..."
    "Все хикканы уже успели изрядно подвыпить..."
    "А это значит, что впереди их ожидает невиданное веселье." 
    
    show alc with dspr
    show pac at cright with dspr
    show zac at cleft with dspr
    show nic at left with dspr
    show klc at fleft with dspr
    show glc at fright with dspr
    
    gl "Ну чо, поцоны, наконец-то у Алеха закончилась сессия, ура-ура-ура!"
    za "!!!"
    al "Пацаны, я так рад, это пиздец, КЮЩ-БАРАНКЮЩ!"
    al "КЮЩ-БАРАНКЮЩ!"
    al "КЮЩ-БАРАНКЮЩ!"
    al "КЮЩ-БАРАНКЮЩ!"
    ni "БЛЯЯЯЯЯ!!!"
    pa "I agree. {w}Please, shut the fuck up."
    al "Да ладно вам, дрыщаны, КЮЩ-БАРАНКЮЩ!"
    al "КЮЩ-БАРАНКЮЩ!"
    al "КЮЩ-БАРАНКЮЩ!"
    
    kl "Некет прав: ты слишком уж продолжительно говоришь это."
    al "Слышь, Ржавый, чё там вякнул, ну-ка дуло своё залепил!"
    
    play sound kl_error
    
    kl "А-а-а-а..."
    kl "*CONNECTION_ERROR_666*"
    
    stop sound
    
    za "АХАХАХАХАХАХАУХУХУХУХУХУХУХААХА, ОРУУУУУ!"
    gl "Ржавый, ну не скупись ты на оперативку подороже, ей-богу, сам же видишь, что из этого получается..."
    al "Увы, он никогда тебя не послушает..."
    
    play sound kl_error
    
    kl "*An exception occured in the script...*"
    
    stop sound 
    
    za "ООЙ НЕ МОГУ, АХААХХАХАХААХАХАХАХХАА!"
    ni "Бля, да хватит вам уже... {w}Го лучше в футбол поиграем."
    pa "Я за, пошли."
    
    hide alc
    hide glc
    hide nic
    hide pac
    hide klc
    hide zac
    stop music fadeout 3
    
    "/bomzhi/ team выдвинулась к полю при ШДП."
    
    window hide 
    scene bg bomzhi_football with dissolve
    $ renpy.pause(2, hard=True)
    
    za "Дыа-а-а, щётка любет футбо-о-л..."
        
    scene bg home_oleg with dissolve
    play music music_list["two_glasses_of_melancholy"] fadein 1
    show alc 
    show pac at cright
    show zac at cleft
    show nic at left
    show klc at fleft
    show glc at fright
    
    pa "Нет, дома сидим."
    ni "Эх..."
    pa "Алех, не клади свои ноги мне на голову, заебал уже."
    al "А-э-а, извене..."
    ni "Hey, Kolia..."
    kl "Yeah?"
    ni "Why did you go to jail?"
    
    play sound kl_error
    
    kl "*THERE IS NO WORD *JAIL* IN MY BRAIN... TRYING TO SEARCH IT IN FILES...*"
    
    stop sound 
    
    gl "Бля вам ещё не надоело этой фигнёй заниматься?"
    ni "It's always interesting and funny!"
    
    play sound kl_error
    
    gl "Чё???"
    
    stop sound
    
    pa "I agree. {w}It's really funny."
    al "Чё, го пиццу закажем, парни."
    ni "Я не скидываюсь, пошли на хуй, опять мне все по косарю будете должны, ну его на хер..."
    al "Как хочешь..."
    al "Ладно, давайте посмотрим, что сайт домино пицца предлагает."
    al "Чё, может, гавайскую?"
    kl "Да-а-а, да-а-а, говайскоя очень вкусноя, согласен, феноменально, восхитительно!"
    pa "Да ты угораешь что ли, Ржавый, ну на хуй, давайте четыре сыра, маргариту и пепперрони."
    gl "Ну чё, мне нравится, классно."
    al "Да, вполне пойдёт, что думаешь, Щётка?"
    za "РОССИЯ В ПОЛУФИНАЛЕ!!!"
    al "Щётка солнечный удар получал..."
    ni "А Алех спал..."
    al "Нет, Алех бодрствовал..."
    ni "Jawohl, kein Problem..."
    al "Короче, всё, заказываем, я нажимаю кнопку."
    pa "Press the button and suck my dick..."
    ni "It's about to go down!"
    gl "О, парни, хотите, я включу вам новую песню Wildways?"
    pa "Нет, петушиный вокал никому не нужен."
    ni "Ну, конечно, все должны Borealis - Midnight City сто лет слушать..."
    ni "И ещё Pearl Kyoudai - Kimi no Corona ni Tsutsumaretai."

    play sound kl_error
    
    kl "*CAN'T FIND SONG *Pearl Kyoudai - Kimi no Corona ni Tsutsumaretai* IN MEMORY...*"
    
    stop sound
    
    ni "Конечно, ты её не вспомнишь, Ржавый, ты же её ни разу не слушал." 
    pa "Rjaviy failed... {w}AGAIN..."
    ni "Oh, Rjaviy, always such a disappointment... Why do we bother?.."
    ni "But you hear it... {w}DON'T YOU???"
    
    play sound kl_error
    
    kl "???"
    
    stop sound
    
    ni "Ладно, ну тебя на хуй, это бесполезно, ничего не знаешь..."
    al "В МИРЕ ХУЖЕ НЕТ ПОКА ФАКУЛЬТЕТА ВМК!!"
    za "АХАХАХАХААХАХАХУХУХУХОХОХОХОООО!! ДААААА, ВМК ГОВНОООО!!"
    za "!!!"
    "Ржавый не стал ничего отвечать и молча продолжил пить свою Елаху."
    "/bomzhi/team с каждыми пятнадцатиминутками становилась всё пьянее и пьянее."
    "Их рассудок терял форму и превращался в нечто вроде киселя."
    "Говоря простым языком, учудить сейчас они могли всё, что угодно."
    "Время было два часа ночи."
    "Пашок предложил досмотреть Kei'Jo, но остальным хикканам было не до аниме, и, в конечном итоге, было принято решение выйти на улицу."
    
    stop music fadeout 7
    
    "Оставив Денчика одного дрочить в квартире, наша фантастическая шестёрка еле выползла из квартиры, кое-как влезла в лифт, а после вышла из подъезда."
    
    scene bg no_bg with dissolve
    play music music_list["goodbye_home_shores"] fadein 2
    
    "*БЭКГРАУНД ОКОЛО ПОДЪЕЗДА АЛЕХА.*"
    za "Ха-ха-а-а, я пё-ё-ёрну-у-ул!.."
    al "Блть, Щётк, ты мдак, ну нхуя ты эт сдлал?.."
    za "Не держи в себе, хы-ы-ы..."
    ni "I suppose, we won't survive..."
    pa "Of course, unfortunately..."
    gl "Вы заепали, гаворите уже п-руске!!..."
    kl "Чёо, кда пдём щас?"
    al "Ща решым, Ржовый, не ачькуй..."
    gl "Давайте в центр... {w}...на автобусе... {w}А то мы даже до Крымской... ...не дойдём..."
    ni "Атличн идейа... {w}Там сто пудв настранцы уже гляют..."
    pa "*бульк*"
    al "Гэйлав, тагда види да астановке..."
    gl "Хршо, впрёд, дрщи!.."
    play music winter_warm fadein 2
    
    "Четверь часа спустя пьяные в стельку юноши вышли к автобусной остановке."
    "На улице было достаточно тепло, поэтому ребятам было всё равно, когда приедет какой-нибудь транспорт. {w}Тем не менее, пока не было даже малейших признаков о прибывающем в скором времени автобусе или трамвае."
    "Всё-таки, есть прелесть в этом всём... {w}Встречи друзей, общение..."
    "Всё это разбавляет однообразную ежедневную рутину, и жизнь приобретает новые красочные оттенки."
    "Парни сидели на лавочке на остановке."
    "Некет мечтательно смотрел на восход солнца и курил сигарету."
    "Алех думал о чём-то своём."
    "Пощок залип и смотрел в одну точку."
    ni "Ура, ребзя, мы джили да лета..."
    al "Как ж б я хател, шоб оно не заканчивалось ваапще..."
    "А Пощок всё молчал и продолжал залипать вникуда."
    "Голов, Ржавый и Щётка пытались донести друг другу свои мысли, но у них это едва получалось."
    "По крайней мере, братья были вместе."
    "Не так много нужно для счастья, на самом-то деле."
    "Но счастье всегда временно."
    "Из глубоких раздумий парней вывел внезапно подъезжающий к остановке автобус."
    
    "*БЭКГРАУНД АВТОБУС СНАРУЖИ У ОСТАНОВКИ*"
    play sound sfx_ikarus_arrive 
    
    "Автобус под номером 410 остановился. {w}Выглядел он достаточно странно."
    "Нормальный человек бы сейчас задался вопросом, а ходят ли сейчас такие вообще."
    
    stop sound fadeout 5
    play sound_loop sfx_bus_idle fadein 3
    
    al "Мужики, пошли... Это наш!"
    "Автобус был будто из совка, но нашим пьяницам в таком состоянии было плевать, и ничего подозрительного во внешности автобуса они не нашли, потому без раздумий вошли внутрь."
    
    stop music fadeout 1
    stop sound_loop fadeout 2
    $ renpy.pause(1, hard=True) 
    "*БЭКГРАУНД ОТКРЫТЫЕ ДВЕРИ АВТОБУСА*"
    play sound sfx_intro_bus_door_open
    $ renpy.pause(7, hard=True)
    "*БЭКГРАУНД АВТОБУС ЕДЕТ*"
    $ renpy.pause(6, hard=True)
    stop sound 
    "*БЭКГРАУНД САЛОН АВТОБУСА*"
    play sound_loop sfx_bus_interior_moving
    $ renpy.pause(1, hard=True)
    
    "Пьяные в срань суканы еле дошли до сидений в автобусе и буквально плюхнулись в них."
    "Лишь один Некет побеспокоился, на тот ли автобус они сели." 
    ni "Бляя, дрыщ-щи, куда мы вообще едем, а-а-а?"
    "Ответа не последовало."
    ni "А, ну и хуй с вами! {w}С нами Бог!"
    "Благо в автобусе не было никого, кроме их шестерых, поэтому кричащего на весь салон Некета никто не мог заткнуть и вызвать полицию вследствие его девиантного поведения."
    "Так сильно хикканы давно не нажирались."
    "И, ясен хуй, сейчас им было абсолютно до фонаря на то, что с ними могло бы случиться."
    "По сути, это и есть самый существенный плюс алкогольного опьянения. {w}Человек в этом состоянии забывает обо всех своих проблемах, которые терзают его изнутри."
    "Но за такую роскошь, конечно же, плату никто не отменял: постепенный ущерб здоровью, а также совсем спонтанные действия, последствия которых вполне могут поставить крест на всей жизни человека."
    "Тем временем автобус ехал, а пацанов в тепле неумолило одолевал сон."
    al "Чёрт, блять, неет, не спааать..."
    
    stop sound_loop fadeout 3
    show blink
    $ renpy.pause(3, hard=True)
    scene black
    window hide
    
    jump char_choice
    
label char_choice:
    
    play music char_select fadein 2
    
    "Выберите персонажа, от лица которого Вы бы хотели переживать индивидуальные события."
    
    call screen vib_menu_bomzhi_team
        
screen intro_ni_screen:
    
    add "intro_ni" xalign 0.0 yalign 0.0
    
screen intro_pa_screen:
    
    add "intro_pa" xalign 0.0 yalign 0.0
    
screen intro_al_screen:
    
    add "intro_al" xalign 0.0 yalign 0.0
    
screen intro_gl_screen:
    
    add "intro_gl" xalign 0.0 yalign 0.0
    
screen intro_za_screen:
    
    add "intro_za" xalign 0.0 yalign 0.0
    
screen intro_kl_screen:
    
    add "intro_kl" xalign 0.0 yalign 0.0    
                   
screen vib_menu_bomzhi_team:
    
    tag menu
    modal False
    imagemap:
        ground "intro_transparent1"
        hotspot ((0, 0, 1280, 540)):
            hovered [Show("intro_ni_screen", transition=Dissolve(0.5))] #neket
            unhovered [Hide("intro_ni_screen", transition=Dissolve(1.0))]
            action [Hide("intro_ni_screen", transition=Dissolve(0.5)), Jump("ni_chosen")]
        hotspot ((640, 0, 640, 540)):
            hovered [Show("intro_pa_screen", transition=Dissolve(0.5))] #poshok
            unhovered [Hide("intro_pa_screen", transition=Dissolve(1.0))]
            action [Hide("intro_pa_screen", transition=Dissolve(0.5)), Jump("pa_chosen")]
        hotspot ((1280, 0, 640, 540)):
            hovered [Show("intro_al_screen", transition=Dissolve(0.5))] #aleh
            unhovered [Hide("intro_al_screen", transition=Dissolve(1.0))]
            action [Hide("intro_al_screen", transition=Dissolve(0.5)), Jump("al_chosen")]
        hotspot ((0, 540, 1280, 540)):
            hovered [Show("intro_gl_screen", transition=Dissolve(0.5))] #gaylov
            unhovered [Hide("intro_gl_screen", transition=Dissolve(1.0))]
            action [Hide("intro_gl_screen", transition=Dissolve(0.5)), Jump("gl_chosen")]
        hotspot ((640, 540, 640, 540)):
            hovered [Show("intro_za_screen", transition=Dissolve(0.5))] #schyotka
            unhovered [Hide("intro_za_screen", transition=Dissolve(1.0))]
            action [Hide("intro_za_screen", transition=Dissolve(0.5)), Jump("za_chosen")]
        hotspot ((1280, 540, 640, 540)):
            hovered [Show("intro_kl_screen", transition=Dissolve(0.5))] #rjaviy
            unhovered [Hide("intro_kl_screen", transition=Dissolve(1.0))]
            action [Hide("intro_kl_screen", transition=Dissolve(0.5)), Jump("kl_chosen")]   

label ni_chosen:
    
    $ ni_route = True;
    show intro_ni with dissolve
    
    "Вы выбрали НЕКЕТА."
    
    stop music fadeout 5
    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(2, hard=True)
    
    jump camp_arrival_day1
    
label pa_chosen:
    
    $ pa_route = True;
    show intro_pa with dissolve
    
    "Вы выбрали ПОЩКА."
    
    stop music fadeout 5
    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(2, hard=True)
    
    jump camp_arrival_day1
    
label al_chosen:
    
    $ al_route = True;
    show intro_al with dissolve
    
    "Вы выбрали АЛЕХА."
    
    stop music fadeout 5
    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(2, hard=True)
    
    jump camp_arrival_day1
    
label gl_chosen:
    
    $ gl_route = True;
    show intro_gl with dissolve
    
    "Вы выбрали ГЕЙЛОВА."
    
    stop music fadeout 5
    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(2, hard=True)
    
    jump camp_arrival_day1

label za_chosen:
    
    $ za_route = True;
    show intro_za with dissolve
    
    "Вы выбрали ЩЁТКУ."
    
    stop music fadeout 5
    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(2, hard=True)
    
    jump camp_arrival_day1

label kl_chosen:
    
    $ kl_route = True;
    play sound kl_error
    show intro_kl with dissolve
    
    "Вы выбрали РЖАВОГО."
    
    stop sound
    stop music fadeout 5
    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(2, hard=True)
    
    jump camp_arrival_day1
    
    