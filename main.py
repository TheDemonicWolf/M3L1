from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Привет! Здесь будет показано несколько рандомных фактов о технологической зависимости.</h1><a href="/random_fact">Посмотреть случайный факт!</a> <a href="/random_mem">Посмотреть случайный мем!</a>'

@app.route("/random_fact")
def fact():
    facts_list = ['Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.',

'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.',
'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.',

'Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.',

'Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.',
'Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.',

'Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.']
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/random_mem")
def mem():
    mem_list = ['https://i.ytimg.com/vi/99GfoR5MCs8/maxresdefault.jpg', 'https://avatars.dzeninfra.ru/get-zen_doc/1657335/pub_5d93526ff557d000ae816923_5d9353cf0ce57b00aeb2cdc6/scale_1200', 'https://sun9-57.userapi.com/impf/c855216/v855216641/122b4d/AYPGiYdVDkQ.jpg?size=784x855&quality=96&sign=7eab5f1212bf6ca225100608c67b4d1a&c_uniq_tag=S1Px9V5LzxVb636Y9or7JkH8GLuRbBeyQEa0x8GJfMQ&type=album', 'https://cdn.fishki.net/upload/post/2020/03/23/3265006/1584946561-pressa-tv-4y.jpg', 'https://avatars.dzeninfra.ru/get-zen_gallery/3006251/pub_5fbc13a80b4af801498426c1_5fbc14210b4af8014984e5f5/scale_1200', 'https://cdn.fishki.net/upload/post/201404/10/1259669/16.jpg', 'https://otvet.imgsmail.ru/download/250728787_b628e34eb9e20955d0966dcc6fa52350.jpg']
    return f'<img src={random.choice(mem_list)}/>'
app.run(debug=True)