
define nikita = Character('Никита Сергеевич', color="#A5274E")
define dima = Character('Дима', color='#272FA5')
define dad = Character('Папа', color='#A5274E')
define mom = Character('Мама', color='#A5274E')
define t1 = Character('Наталья Алексеевна', color='#A5274E')
define t2 = Character('Ольга Валерьевна', color='#A5274E')
define t3 = Character('Марина Владимировна', color='#A5274E')
define vlad = Character('Влад', color='#A5274E')
define womancom = Character('Алиса', color='#A5274E')
define olddima = Character('Дима', color='#A5274E')
define prepodone = Character('Преподаватель Сергей Владимирович', color='#A5274E')
define prepodtwo = Character('Преподаватель Мария Николаевна', color='#A5274E')
define teamlead = Character('Максим', color='#A5274E')
define razrab = Character('Саня', color='#A5274E')
define diz = Character('Мария', color='#A5274E')
define analit = Character('Григорий', color='#A5274E')
define aloboss = Character('Владимир Алексеевич', color='#A5274E')


default dima_characteristic = None
default package_size = None
default number_alph = None
default code_phano = None
default count_right_answers = 0
label start:

    scene bg kitchen with fade
    "Каким же будет Дима?"
    menu:
        "Спортсмен":
            $dima_characteristic = "Спортсмен"
            jump first_scene
        "Волонтер":
            $dima_characteristic = "Волонтер"
            jump first_scene
        "Обычный парень":
            $dima_characteristic = "Обычный парень"
            jump first_scene

label first_scene:

    scene bg kitchen with fade
    "В доме была напряженная атмосфера, Дима уже предвкушал тот самый разговор после собрания..."
    show mom
    show dima at right
    mom "Опять возвращаемся к тому же разговору!"
    mom "Сколько раз нам еще тебе говорить... Долго ты еще будешь заниматься этой фигней?"

    dima "Вы не понимаете современных тенденций, то что я хочу это вполне реально!"
    dima "Мне нравится компьютер и другого мне не надо. Все вот эти ваши уроки у Натальи Зиновишной не дадут мне ничего полезного."
    hide dima

    show mom
    mom "Леша-а, ну скажи ему!"
    hide mom

    "Папа прокашлялся."
    show dad
    dad "Мама ведь правильно говорит: игрушки это так, несерьезное дело - баловство."
    hide dad

    "Все мечты и планы о киберспорте с каждым словом родителей рушились все сильнее и сильнее."

    show dima
    dima "Я вам еще докажу, что это все не пустой звук."
    "Дима выбегает из комнаты, не обращая внимания на дальнейшие фразы родителей."
    hide dima with moveoutleft

    show mom
    mom "Ну кто вырастет из игромана и неуча..."
    hide mom
    jump second_scene

label second_scene:
    scene bg classroom

    show dima at left
    dima "Любимый кабинет..."

    show teacher with moveinright
    nikita "Всем здравствуйте! Ну, готовы решать 26 и 27 задания?"

    "В классе особое желание не проявилось."

    dima "Сложновато будет... но главное-то желание!"

    nikita "Тут-то ты прав, Дима, от тебя одного на моих уроках энтузиазм."

    "Класс мельком оглянул Никиту Сергеевича и Диму."
    hide dima
    hide teacher
    "Все разбрелись по классу и уселись за компьютеры."
    show dimawithlaptop at left
    "Дима приготовился усердно решать."

    "Задача: Напишите программу, которая будет находить сумму четных чисел от 1 до N включительно."

    $ N = 10
    
    menu:
        "1. sum = 0\nfor i in range(1, N+1):\n    if i %% 2 == 0:\n        sum += i":
            $chosen_answer = "1"
            jump check_solution
        "2. sum = 0\nfor i in range(1, N):\n    if i %% 2 == 0:\n        sum += i":
            $chosen_answer = "2"
            jump check_solution
        "3. sum = 0\nfor i in range(2, N+1, 2):\n    sum += i":
            $chosen_answer = "3"
            jump check_solution

label check_solution:

    "Проверяем ваш ответ..."

    # Предположим, что переменная N уже определена в вашем сценарии
    $correct_answer = sum(range(2, N+1, 2))  # Правильный ответ для примера

    if chosen_answer == "1":
        $user_result = sum(i for i in range(1, N+1) if i % 2 == 0)
    elif chosen_answer == "2":
        $user_result = sum(i for i in range(1, N) if i % 2 == 0)
    elif chosen_answer == "3":
        $user_result = sum(range(2, N+1, 2))
    else:
        $user_result = None

    if user_result == correct_answer:
        "Верно! Дима написал правильный код."
    else:
        "Неправильно. Давайте попробуем еще раз."

    jump third_scene

label third_scene:

    show teacher at right
    nikita "Получается?"

    dima "В принципе да."

    nikita "Вижу попытки есть. Подправь еще тут... Так, вот здесь еще."
    nikita "Вот! Другое дело!"

    dima "Спасибо за помощь. На самом деле только вы в меня верите..."
    "Тут в голове Димы возникли злые, мрачные, словно дышашие огнем образы учителей."
    hide teacher

    show teacher1 at right
    t1 "Да ты ничтожество, самый худший ученик!"
    hide teacher1 with moveouttop

    show teacher2 at right
    t2 "Да кто тебя такого на работу возьмет, ты же ничего не умеешь, кроме как в своих компухтерах зависать сутками!"
    hide teacher2 with moveouttop

    show teacher3 at right
    t3 "Кем ты вырастешь, кем ты станешь!? Ты ничего не добьешься в жизни!!!"
    hide teacher3 with moveouttop

    "Тут образы резко оборвались теплым голосом Никиты Сергеевича, которого так сильно уважал Дима."
    "Учитель информатики был всеми любим: он всегда мог прийти на помощь, закрыть глаза на пропуски, подправить оценки в конце четверти."
    
    show teacher at right
    nikita "Слушай, не думай о плохом. Твои увлечения нужно направить в нужное русло, а там и в ВУЗ поступишь, тогда-то и уделаешь всем нос."
    nikita "Я в тебе не сомневаюсь."

    dima "Я вам благодарен..."
    hide dimawithlaptop
    hide teacher
    "После этого разговора Дима всерьез занялся программированием и изучением сферы IT. Каждый день подготовки все более завлекал и увлекал Диму."
    "В итоге Дима принял для себя решение, что будет сдавать на ЕГЭ профильную математику и информатику."
    jump fourth_scene

label fourth_scene:

    scene russiancabinet
    show dima
    "Дима очень переживал, так как русский был самым первым экзаменом."
    "На удивление, русский не оказался затруднительным для Димы, так как он обладал 'врожденной грамотностью'."
    dima "Ну вроде бы не было так трудно, как я представлял. Буду надеяться на хороший балл."
    hide dima

    scene mathcabinet
    show dima
    "Вот и время второго экзамена, самого трудного, самого непредсказуемого."
    "Волнующий день, волнующий момент входа в аудиторию."
    "'Заполняем графу ФИО, как указано в паспорте' - прозвучало в аудитории."
    "4 часа прошли довольно быстро, Дима был вымотан."
    dima "Страшновато за результаты..."
    hide dima

    scene itcabinet
    show dima
    "Конец июня - тот момент, когда силы были на исходе."
    "Дима на все 100 был готов к данному предмету, поэтому он совершенно не переживал и был уверен в своем успехе."

    jump first_exersice

label first_exersice:

    scene itcabinet
    """Прибор автоматической фиксации нарушений правил дорожного движения делает цветные фотографии размером 1920×1080 пикселей,
    используя палитру из 4096 цветов. Для передачи снимки группируются в пакеты по 68 штук. Определите размер одного пакета фотографий в Кбайт.
    В ответе запишите только число."""
    menu:
        "a) 777 Кбайт":
            $package_size = 777
            jump check_first_answer
        "b) 37257923 Кбайт":
            $package_size = 37257923
            jump check_first_answer
        "c) 206550 Кбайт":
            $package_size = 206550
            jump check_first_answer
        "d) 83295236 Кбайт":
            $package_size = 83295236
            jump check_first_answer

label check_first_answer:

    $correct_first_answer = 206550

    if package_size == correct_first_answer:
        "Правильно! Размер одного пакета фотографий - 206550 Кбайт."
        $count_right_answers += 1
    else:
        "Неправильно. Правильный ответ: 206550 Кбайт."

    jump second_exersice

label second_exersice:

    scene itcabinet
    """Все 5-буквенные слова, составленные из букв Щ, Р, Ю, И, записаны в алфавитном порядке и пронумерованы.
    Вот начало списка:
    1. ИИИИИ
    2. ИИИИР
    3. ИИИИЩ
    4. ИИИИЮ
    5. ИИИРИ
    6. ИИИРР
    ...
    Под каким номером идёт последнее слово, которое начинается на букву Щ и заканчивается на букву И?"""
    menu:
        "a) 204":
            $number_alph = 204
            jump check_second_answer
        "b) 881":
            $number_alph = 881
            jump check_second_answer
        "c) 483":
            $number_alph = 483
            jump check_second_answer
        "d) 765":
            $number_alph = 765
            jump check_second_answer

label check_second_answer:

    $correct_second_answer = 765

    if number_alph == correct_second_answer:
        "Правильно! Номер последнего слова - 765."
        $count_right_answers += 1
    else:
        "Неправильно. Правильный ответ: 765."

    jump third_exersice

label third_exersice:

    scene itcabinet
    """Для кодирования некоторой последовательности, состоящей из букв Л, М, Н, П, Р, решили использовать неравномерный двоичный код, удовлетворяющий условию,
    что никакое кодовое слово не являетсяначалом другого кодового слова.
    Это условие обеспечивает возможность однозначной расшифровки закодированных сообщений.
    Для букв Л, М, Н использовали соответственно кодовые слова 00, 01, 11.
    Для двух оставшихся букв П и Р кодовые слова неизвестны.Укажите кратчайшее возможное кодовое слово для буквы П, при котором код будет удовлетворять указанному условию.
    Если таких кодов несколько, укажите код с наименьшим числовым значением."""
    menu:
        "a) 1":
            $code_phano = 1
            jump check_third_answer
        "b) 100":
            $code_phano = 100
            jump check_third_answer
        "c) 11":
            $code_phano = 11
            jump check_third_answer
        "d) 000":
            $code_phano = 000
            jump check_third_answer


label check_third_answer:

    $correct_second_answer = 100
    
    if code_phano == correct_second_answer:
        "Правильно! Кратчайшее кодовое слово - 100."
        $count_right_answers += 1
        jump result_inf
    else:
        "Неправильно. Правильный ответ: 100."
        jump result_inf

label result_inf:

    scene homecabinet
    if count_right_answers == 3:
        "Дима набрал 100 баллов! Поздравляем!"
    if count_right_answers == 2:
        "Дима набрал 90 баллов! Поздравляем!"
    if count_right_answers == 1:
        "Дима набрал 85 баллов! Поздравляем!"
    if count_right_answers == 0:
        "Дима набрал 80 баллов! Поздравляем!"

    jump fifth_scene

init:
    $answer_mobile_dev = False
    $answer_city = False

label fifth_scene:

    scene itcabinet
    show dima
    "Ну я даже не сомневаюсь, что все будет окей. Теперь надо думать над направлением и вузом."
    hide dima

    scene homecabinet
    show dima
    "Дима включил компьютер и принялся просматривать множество сайтов, посвященных поступлению."
    dima "Блин... Как же много вузов, направлений... Кем вообще мне хочется быть..."
    dima "Хм... А вот УрФУ очень привлекателен. Сейчас глянем, какие там направления есть."
    "Это лето выдалось не таким, как раньше. Диме предстояло выбрать подходящее направление. Он приступил к анализу своих интересов."
    jump choose_way

label choose_way:
    scene homecabinet
    menu:
        "Я бы хотел заниматься анализом данных.":
            "Дима оказался не особо увлечен анализом данных. Не самое подходящее направление для него."
            jump choose_way
        "Я бы хотел заниматься бизнесом." :
            "Бизнес слишком сложный и рискованный для Димы."
            jump choose_way
        "Меня манит металлургия.":
            "Металлургия не покорила Диму. Не самое подходящее направление для него."
            jump choose_way
        "Меня влечет мобильная разработка.":
            "Дима выбрал мобильную разработку. Отличный выбор!"
            $answer_mobile_dev = True
            "Теперь Дима сталкивается с дополнительными выборами и вопросами в своем путешествии."
            jump choose_city
        "Мне интересно 3D-моделирование.":
            "3D-моделирование не входит в круг интересов Димы. Не самое подходящее направление для него."
            jump choose_way

    jump choose_way

label choose_city:
    scene homecabinet
    menu:
        "Да, мне идеально подходит это направление, осталось определиться с городом."
        "Какой город мне выбрать?"
        "Казань":
            "Диме будет тяжело найти новых знакомых."
            jump choose_city
        "Екатеринбург":
            "Дима выбрал Екатеринбург. Идеальный выбор!"
            $answer_city = True
            jump dop_fifth_scene
        "Москва":
            "Москва слишком далеко для Димы, родители его не отпустят."
            jump choose_city
    jump choose_city

label dop_fifth_scene:
    scene homecabinet
    show dima
    "Выбор Димы пал на программную инженерию в УрФУ."
    "Сделав выбор, Дима отправился в приемную коммисию."
    hide dima
    jump sixth_scene

label sixth_scene:

    scene priem
    show dima
    show womancom at right
    womancom "Данное направление дает студенту глубокие практические навыки в разработке, тестировании и сопровождения программного обеспечения (ПО) и программ в целом."
    womancom "Программная инженерия рассматривает подход к разработке программного обеспечения как формальный процесс, который используется в традиционной инженерии."
    dima "Ого, очень интересно."
    "Дима подал документы и счастливый отправился домой."
    hide dima
    jump seventh_scene

label seventh_scene:

    scene homecabinet
    show dima
    "И вот на дворе 7 августа."
    "Дима, просматривая списки поступивших, нашел себя."
    if dima_characteristic == "Обычный парень":
        show image "result_two.jpg":
            xpos 0 ypos 0
    else:
        show image "result_one.jpg":
            xpos 0 ypos 0
    "Счастью не было предела."
    dima "Ура!!!"
    hide dima
    jump eighth_scene

label eighth_scene:

    scene urfu
    show dima
    "1 сентября: начало нового, сложного и тернистого этапа жизни Димы."
    "В процессе обучения он знакомится с новыми друзьями и сталкивается с различными трудностями, связанными с учебой и жизнью в большом городе."
    "Упорство и труд позволили Диме успешно справится со всеми возникающими испытаниями и стать одним из лучших студентов курса."
    jump first_course

label first_course:

    scene cafedraone

    show prepodone at left
    show dima at right
    prepodone "Так. Всем здравствуйте! Сегодня начинается курс лекций по разработке мобильных приложений."
    prepodone "Думаю, стоит начать с небольшого ознакомительного опроса."
    "Дима сразу приготовился, он хотел показать и зарекомендовать себя."
    prepodone "Итак, первый вопрос: кто же такой мобильный разработчик?"
    menu:
        "Мобильный разработчик — это тот, кто разрабатывает программы для мобильных устройств.":
            "Мобильные игры и развлекательные приложения — огромная интересная индустрия."

    prepodone "Совершенно верно, но стоит дополнить, что мобильные устройства — это не только наши любимые гаджеты, носимая электроника, \r\n\
    но и различные научные аппараты, компоненты исследовательских систем на базе гаджетов, компоненты интернета вещей."

    prepodone "Какие требования предъявляются к мобильному разработчику?"

    menu:
        "Знание структур и алгоритмов, знание принципов ООП, понимание принципов дизайна и проектирования мобильных приложений, знание сетевых протоколов, знание SQL.":
            "Навыки работы с App Store и Google Play, безусловно."

    prepodone "Да, вы правы. Знание Android SDK, Java, Kotlin, Scala (в меньшей степени), Rest/SOAP, различные API, SQLite."

    prepodone "Как вы думаете какая вилка зарплат у данных специалистов?"

    menu:
        "Многоооо.":
            "Очень много."

    prepodone "От 26000 на стажировке до 200000 на уровне lead-разработчика"
    jump second_course

label second_course:

    scene cafedratwo
    show prepodtwo at right
    show dima at left
    prepodtwo "Здравствуйте, уважаемые студенты! Сегодня у нас практика, разберем задачки повышенной сложности."
    prepodtwo "Для начала проведем небольшой тестик, чтобы вы взбодрились, к первой паре как никак!"

    jump ex_first

default ans_exone = None
label ex_first:

    scene cafedratwo

    show image "exone.png":
        xpos 0 ypos 0
    menu:
        "a) for i in range(1, x)":
            $ans_exone = 1
            jump check_exone_ans
        "b) x.sort()":
            $ans_exone = 2
            jump check_exone_ans
        "c) break":
            $ans_exone = 3
            jump check_exone_ans
        "d) print(x)":
            $ans_exone = 4
            jump check_exone_ans

label check_exone_ans:

    # Выбор правильного ответа
    $correct_first_ex = 4

    # Вывод результата
    if ans_exone == correct_first_ex:
        "Верно!"
    else:
        "Неверно. Правильный ответ: print(x)"

    jump ex_second

default ans_extwo = None
label ex_second:

    scene cafedratwo

    show image "extwo.png":
        xpos 0 ypos 0
    menu:
        "a) count":
            $ans_extwo = 1
            jump check_extwo_ans
        "b) open":
            $ans_extwo = 2
            jump check_extwo_ans
        "c) sort()":
            $ans_extwo = 3
            jump check_extwo_ans
        "d) ничего":
            $ans_extwo = 4
            jump check_extwo_ans

label check_extwo_ans:

    $correct_second_ex = 2

    if ans_extwo == correct_second_ex:
        "Верно!"
    else:
        "Неверно. Правильный ответ: open"

    jump ex_third

default ans_exthree = None
label ex_third:

    scene cafedratwo

    show image "exthree.png":
        xpos 0 ypos 0
    menu:
        "a) i in range":
            $ans_exthree = 1
            jump check_exthree_ans
        "b) while":
            $ans_exthree = 2
            jump check_exthree_ans
        "c) if":
            $ans_exthree = 3
            jump check_exthree_ans
        "d) else":
            $ans_exthree = 4
            jump check_exthree_ans

label check_exthree_ans:

    $correct_third_ex = 1

    if ans_exthree == correct_third_ex:
        "Верно!"
    else:
        "Неверно. Правильный ответ: i in range"

    jump ex_four

default ans_exfour = None
label ex_four:

    scene cafedratwo

    show image "exfour.png":
        xpos 0 ypos 0
    menu:
        "a) def":
            $ans_exfour = 1
            jump check_exfour_ans
        "b) list":
            $ans_exfour = 2
            jump check_exfour_ans
        "c) while":
            $ans_exfour = 3
            jump check_exfour_ans
        "d) elif":
            $ans_exfour = 4
            jump check_exfour_ans

label check_exfour_ans:

    $correct_four_ex = 1

    if ans_exfour == correct_four_ex:
        "Верно!"
    else:
        "Неверно. Правильный ответ: def"

    jump ex_fife

default ans_exfife = None
label ex_fife:

    scene cafedratwo

    show image "exfive.png":
        xpos 0 ypos 0
    menu:
        "a) sort()":
            $ans_exfife = 1
            jump check_exfive_ans
        "b) reverse()":
            $ans_exfife = 2
            jump check_exfive_ans
        "c) append":
            $ans_exfife = 3
            jump check_exfive_ans
        "d) add()":
            $ans_exfife = 4
            jump check_exfive_ans

label check_exfive_ans:

    $correct_five_ex = 3

    if ans_exfife == correct_five_ex:
        "Верно!"
    else:
        "Неверно. Правильный ответ: append"

    jump second_course_dop

label second_course_dop:

    scene cafedratwo
    show prepodtwo at right
    show dima at left
    prepodtwo "Ну молодцы, в целом неплохо справились. Можно, конечно, постараться во время семестра... и у некоторых студентов пробелов не будет."

    jump third_course

default name_company = None
label third_course:

    scene internship

    "Уже наступила середина третьего курса, Дима определенно продвинулся в изучении алгоритмов, программирования и, разумеется, мобильной разработке."
    show olddima
    olddima "Что ж... пора себя испытать в какой-нибудь крупной компании. У меня довольно обширный выбор."

    menu:
        "Пунктир":
            $name_company = "Пунктир"
        "Газфон":
            $name_company = "Газфон"
        "Тынтекс":
            $name_company = "Тынтекс"
        "ТиньОн":
            $name_company = "ТиньОн"

    olddima "Отлично! Тут-то и можно начать свою IT карьеру."
    olddima "А вот и моя команда на ближайшее время."

    hide olddima

    show teamlead
    "Максим, 25 лет, учился в УрФУ, ответственный, справедливый, полностью погружен в свое дело, благодаря чему построил отличную карьеру."
    hide teamlead

    show razrab
    "Саня, 28 лет, учился на прогаммной инженерии УрФУ, усидчивый, общительный, senior-разработчик, ключевое звено команды."
    hide razrab

    show diz
    "Мария, 24 года, училась в УГИ на направлении дизайн, работает, непокладая рук."
    hide diz

    show analit
    "Григорий, 43 года, учился в УрФУ, любит свое дело и относится к любому делу серьезно."
    hide analit

    "Дима быстро поладил со всей командой, но больше общего у него было с Александром. Александр стал ему наставником, объяснял ему тонкости профессии."

    show razrab at left
    show olddima at right
    razrab "У тебя огромный потенциал, ты уже многое знаешь, но тебе нужно больше практики. Тогда ты реализуешься по максимуму."
    olddima "Спасибо большое, но мне еще многому надо научиться, чтобы достичь вашего уровня."
    hide razrab
    "Слова Александра напомнили ему доброе отношение Никиты Сергеевича."
    "Дима и Саня очень хорошо понимали друг друга и чуть ли не сутками сидели за разработкой игры."
    "Дима увидел изнутри весь процесс создания такого крупного проекта и был очень впечатлен."
    olddima "Я обязательно после окончания ВУЗа также стану разработчиком мобильных приложений."
    hide olddima
    jump fourth_course

default name_game = None
label fourth_course:

    scene workplace
    show olddima at left
    "Вот настал и финальный этап этого жизненного пути, 4 курс."
    "Дипломная работа сначала сильно волновала Диму, но он решил делать то, что умеет лучше всего - создание игр."

    olddima "Теперь останется выбрать концепцию, сюжет, поработать с графикой, выгрузкой на платформы и однозначно будет успех. Я сделаю это!"

    menu:
        "Go and Shoot":
            "Оффлайн шутер с 2d графиков против зомби."
            $name_game = "Go and Shoot"
        "CatSimulator":
            "В этой игре вы можете почувствовать себя кошкой или котом, познавая все прелести беззаботной жизни."
            $name_game = "CatSimulator"
        "Village -> City":
            "В этой деревне ваша цель развить свою деревню до мегаполиса."
            $name_game = "Village -> City"
        "War of coalitions":
            "Стратегия, в которой вы разиваете свою страну, вступаете в альянсы, воюете с другими."
            $name_game = "War of coalitions"

    "Дима усердно в течение всего года занимался дипломной работой и успешно защитил ее. Для Димы это стало лучшим событием в жизни!"
    jump ninth_scene

label ninth_scene:

    scene radik
    "И вот конец 4 курса."
    show olddima
    show vlad at right
    vlad "Ну что, Димон, куда теперь пойдешь?"
    olddima "Не знаю пока, хочу рискнуть и податься в крупную компанию, ну или буду работать самостоятельно."
    vlad "О, прикольно. Я бы тоже хотел себя испытать так. Давай, если что я рядом."
    olddima "Давай, брат, до встречи!"
    hide olddima
    hide vlad

    jump main_way

label main_way:
    scene workplace
    show olddima
    "Выпустившись из университета, Дима обладал множеством знаний, но он не хотел оставаться на месте, поэтому перед ним встал выбор. Возможно, главный выбор в жизни."
    menu:
        "Пойти на собеседование в крупную компанию, такую как SUPERWELL.":
            jump sobes_way
        "Пойти по собственному пути разработки.":
            jump alone_way

default count_sobes = 0
label sobes_way:

    scene superwell
    "Сегодня очень важный для Димы день: у него назначено собеседование в самой крупной российской компании SUPERWELL. Дима переживает."
    show dima at left
    show aloboss at right
    jump first_sobes

default expe = None
label first_sobes:

    scene superwell
    show dima at left
    show aloboss at right
    aloboss "Какой у вас опыт работы?"
    menu:
        "1-2":
            $expe = 1
            jump check_first_sobes
        "Нет опыта":
            $expe = 2
            jump check_second_answer
        "Более трех лет":
            $expe = 3
            jump check_first_sobes

label check_first_sobes:

    $correct_first_sobes = 3

    if expe == correct_first_sobes:
        "Так, хорошо."
        $count_sobes += 1
    else:
        "Хм, интересно."
    jump second_sobes

default lang = None
label second_sobes:

    scene superwell
    show dima at left
    show aloboss at right
    aloboss "Какие языки программирования вы знаете?"
    menu:
        "Python, C#, C++":
            $lang = 1
            jump check_second_sobes
        "Java, C#, Kotlin":
            $lang = 2
            jump check_second_sobes
        "Kotlin, Python, Basic":
            $lang = 3
            jump check_second_sobes

label check_second_sobes:

    $correct_second_sobes = 2

    if lang == correct_second_sobes:
        "Отлично."
        $count_sobes += 1
    else:
        "Понял вас."
    jump third_sobes

default skills = None
label third_sobes:

    scene superwell
    show dima at left
    show aloboss at right
    aloboss "Какие ваши лучшие качества?"
    menu:
        "Коммуникабельность, ответственность, трудолюбие.":
            $skills = 1
            jump check_third_sobes
        "Отзывчивость, доброта, усидчивость":
            $skills = 2
            jump check_third_sobes
        "Дисциплинированность, педантичность, целеустремленность":
            $skills = 3
            jump check_third_sobes

label check_third_sobes:

    $correct_third_sobes = 1

    if skills == correct_third_sobes:
        "Так держать."
        $count_sobes += 1
    else:
        "Учту."
    jump four_sobes

default sale = None
label four_sobes:

    scene superwell
    show dima at left
    show aloboss at right
    aloboss "Каковы ваши ожидания по зарплате?"
    menu:
        "50-70 тыс. руб.":
            $sale = 1
            jump check_four_sobes
        "80-100 тыс. руб.":
            $sale = 2
            jump check_four_sobes
        "Более 100 тыс. руб.":
            $sale = 3
            jump check_four_sobes

label check_four_sobes:

    $correct_four_sobes = 2

    if sale == correct_four_sobes:
        "Очень даже хорошо."
        $count_sobes += 1
    else:
        "Хм..."
    jump result_sobes

label result_sobes:
    scene superwell
    show dima at left
    show aloboss at right
    if count_sobes > 2:
        "Вы приняты! Поздравляю!"
        jump success_sobes
    else:
        "Мы вам перезвоним..."
        jump not_success

label success_sobes:
    scene superwell
    show olddima
    "Дима достиг того, чего хотел."
    "Усердие и труд позволили Диме со временем стать senior-разработчиком, получать хорошую заработную плату, постоянные повышения по должности."
    return

label not_success:
    scene workplace
    show olddima
    "Дима не расстроился после собеседования, он принял для себя решение, что самостоятельно разработает игру без чьей-либо помощи."
    "Итогом его hardworking становится крутой платформер, обретающий огромную популярность среди детей и подростков."
    return

label alone_way:

    scene workplace
    show olddima
    "Начиная с разработки в своей небольшой студии, Дима упорным трудом и многочисленными попытками создает свою игру."
    "Он рад тому, что его игра обрела неслыханную популярность и стала эталоном современного геймдева."
    scene gameoffice
    show olddima
    "Его рост не прекращается и он не собирается останавливаться на достигнутом, в скором времени открывая свою компанию AloGame"
    return




























