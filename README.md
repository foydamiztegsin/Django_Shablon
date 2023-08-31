# Django Shablon

# Installation(O'rnatish)
* 1 - Loyihani klonlang (clone repo)

```git clone https://github.com/foydamiztegsin/Django_Shablon```

* 2 - Virtual muhit yaratish va faollashtirish (create a virtual environment and activate)

```
python -m venv venv
venv\Scripts\activate  (windows uchun) yoki  source venv/bin/activate(unix-ga asoslangan tizimlar)
```

* 3 - Loyiha papkasiga kiring (cd into project) 

```cd Django_Shablon```

* 4 - Bog'liqlarni o'rnating (Install dependencies)

```
pip3 install -r requirements.txt 
yoki
pip install -r requirements.txt
```

* 5 - Atrof-muhit o'zgaruvchilarini o'rnating (Set your environment variables)

```
copy .env.exam .env (windows uchun) yoki 
.env.exam .env(unix-ga asoslangan tizimlar)
.env o'zgaruvchilari
    SECRET_KEY      ==> Yangi loyiha yarating Djangoda settings.py filedan SECRET_KEY ni oling va shu yerga joylang
    DEBUG=True      ==> Default
    ALLOWED_HOSTS=* ==> Default
    PostgreSQL database yarating unga user hamda passwordlarni ham joylashtiring
```

* 6 - Ishga tushirish (Run)

```
python3 manage.py collectstatic
python3 manage.py migrate
python3 manage.py runserver
```

* 7 - Loyihaga mustaqil davom etish: loyihaga ko'ra app yaratish

```
python3 manage.py startapp your_app_name
```


<hr>
 Mehnatimiz sizga foyda berayotgan bolsa GITHUB profilimizga obuna bo'ling va telegram kanalimizda reaksiyalarni qoldiring 👍
 
# *E'tiboringiz uchun rahmat* Savollaringiz bo'lsa [Telegram](https://t.me/foydamizteg_sin)