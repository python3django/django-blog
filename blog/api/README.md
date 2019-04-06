# DRF API для блога.
---

## API реализует следующий функционал:

* /api/ - отобразит endpoints.  
* /api/posts/ - GET метод отобразит список всех постов блога, POST метод создаст новый пост если пользователь зарегистрирован.  
* /api/posts/id/ - отобразит детальную информацию о посте с конкретным id. Автор поста может изменить или удалить его.  
* /api/comments/ - GET метод отобразит список всех комментариев блога, POST метод создаст новый комминтарий.  
Функционал реализован так чтобы любой пользователь, не зависимо от того зарегистривано он или нет, смог оставить свой комментарий.

Пример создания нового комментария:  
http POST 127.0.0.1:8000/api/comments/ body="Text test comment 26." name="TestName" post_id="66" email="test@gmail.com" active="true"

http - консольная программа используемая для тестирования api.  
post_id - id поста к которому относиться комментарий.

/api/comments/id/ - отобразит детальную информацию о комментарии с конкретным id.  
Только ADMIN сможет изменить или удалить комментарий.

В API также реализован функционал для throttling, чтобы ограничить количество запросов.

### Фильтрация, поиск и сортировка.

Необходимо установить пакет django-filter: pip3 install django-filter

#### Для posts/  
Фильтр реализован по полям 'title' и 'author'. Пример фильтра по полю title:  
http ":8000/api/posts/?title=What+is+Django?"

Пример фильтра по полю author:  
http ":8000/api/posts/?author=2"

Пример фильтрации по обоим полям одновременно:  
http ":8000/api/posts/?author=1&title=What+is+Django?"

Сортировака реализована по полям 'title', 'created', 'status'.  
Пример фильтрации по полю author и сортировка по полю title:  
http ":8000/api/posts/?author=1&ordering=title"

Пример фильтрации по полю author и сортировки по полю created (дата создания) в обратном порядке:  
http ":8000/api/posts/?author=1&ordering=-created"

Поиск реализован по полям 'title' и 'body', например:  
http ":8000/api/posts/?search=django"  
http ":8000/api/posts/?search=django&ordering=created"

#### Для comments/  
Фильтрация по полям 'name' и 'email', поиск по 'body', сортировка по 'created':  
http ":8000/api/comments/?name=Oleg&search=nuclear&ordering=-created"


### Пагинация выдает по 4 объекта.

