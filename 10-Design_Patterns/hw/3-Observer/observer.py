"""
С помощью паттерна "Наблюдатель" реализуйте простую систему подписок и уведомлений видеохостинга MyTube.

Для реализации можно использовать следующие определения классов:

MyTubeChannel - канал, у которого есть владелец.
    Параметры:
        name: str - Название канала
        owner: MyTubeUser - Владелец канала
        playlists: Dict[str, List[str]] - Плейлисты на канале ({'Название плейлиста': ['видео 1', 'видео 2', 'видео 3']})

    Методы:
        __init__(channel_name: str, chanel_owner: MyTubeUser) - При создании канала указывается название канала и его владелец
        subscribe(user: MyTubeUser) - Подписка пользователя user на канал
        publish_video(video: str) - Публикация нового видео и рассылка новости о публикации всем подписчика
        publish_playlist(name: str, playlist: List[str]) - Публикация нового плейлиста и рассылка новости о публикации всем подписчикам

MyTubeUser - Пользователь видеохостинга MyTube
    Параметры:
        _name: str - Имя пользователя MyTube
    Методы:
        __init__(user_name: str) - У нового пользователя есть имя
        update(message: str): - Метод для приёма уведомлений о публикации

Пример кода, который должен работать:

matt = MyTubeUser('Matt')
john = MyTubeUser('John')
erica = MyTubeUser('Erica')

dogs_life = YoutubeChannel('All about dogs', matt)
dogs_life.subscribe(john)
dogs_life.subscribe(erica)

dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos]

for video in dogs_nutrition_videos:
    dogs_life.publish_video(video)

dogs_life.publish_playlist(dogs_nutrition_playlist)

Output:
Dear John, there is new video on 'All about dogs' channel: 'What do dogs eat?'
Dear Erica, there is new video on 'All about dogs' channel: 'What do dogs eat?'
Dear John, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
Dear Erica, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
Dear John, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'
Dear Erica, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'

"""


class Subject:

    def subscribe(self, user):
        """
        Подписка пользователя user на канал
        """
        pass

    def publish_video(self, video):
        """
        Публикация нового видео и рассылка новости о публикации всем подписчика
        """
        pass

    def publish_playlist(self, playlist):
        """
        Публикация нового плейлиста
        и рассылка новости о публикации всем подписчикам
        """
        pass


class MyTubeChannel(Subject):
    playlists = {}  # Dict[str, List[str]] - Плейлисты на

    #  канале({'Название плейлиста': ['видео 1', 'видео 2', 'видео 3']})

    observers = {}  # Словарь подписчиков. Адрес-имя

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner  # MyTubeUser - Владелец канала

    def subscribe(self, user):
        """
        Подписка пользователя user на канал
        """
        print(f'Новый подписчик {user.user_name}')
        self.observers.update({user: user.user_name})

    def publish_video(self, video):
        """
        Публикация нового видео и рассылка новости о публикации всем подписчика
        """
        for observer in self.observers:
            string = f"Dear {self.observers[observer]}, there is new video on '{self.name}' channel: '{video}'"
            observer.update(string)

    def publish_playlist(self, playlist):
        """
        Публикация нового плейлиста
        и рассылка новости о публикации всем подписчикам
        """
        self.playlists.update(playlist)
        # print('--->', self.playlists)
        for observer in self.observers:
            string = f"Dear {self.observers[observer]}, there is new playlist " \
                     f"on '{self.name}' channel: '{list(playlist.keys())[0]}'"
            observer.update(string)


class MyTubeUser:
    def __init__(self, user_name):
        self.user_name = user_name

    def update(self, string):
        """
        Метод для приёма уведомлений о публикации
        """
        print(string)


if __name__ == '__main__':
    matt = MyTubeUser('Matt')
    john = MyTubeUser('John')
    erica = MyTubeUser('Erica')

    dogs_life = MyTubeChannel('All about dogs', matt)
    dogs_life.subscribe(john)
    dogs_life.subscribe(erica)

    dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
    dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos}

    for video in dogs_nutrition_videos:
        dogs_life.publish_video(video)
    dogs_life.publish_playlist(dogs_nutrition_playlist)
