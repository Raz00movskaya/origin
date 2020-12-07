def info(username, userlastname, yearofbirth, city, email, phone):
    print(f"Имя - {username}; Фамилия - {userlastname}; Год рождения - {yearofbirth}; Город проживания - {city}; Email - {email}; Телефон - {phone} ")

info(username=input('Введите имя: '), userlastname=input('Введите фамилию: '), yearofbirth=input('Введите год рождения: '), city=input('Введите город: '), email=input('Введите email: '), phone=input('Введите телефон: '))