from flask import Flask
from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# ##### Это надо отправить -- начало{
def main():
    global_init(input())

    session = create_session()

    for user in session.query(User).filter(User.age < 18):
        print(f'{user} {user.age} years')


if __name__ == '__main__':
    main()
# ##### Это надо отправить -- конец}