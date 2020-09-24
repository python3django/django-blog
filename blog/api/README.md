# DRF API
---

## English

### API:

* /api/ - endpoints.
* /api/posts/ - The GET method will display a list of all blog posts, the POST method will create a new post if the user is registered.
* /api/posts/id/ - detailed information about a post with a specific id. The author of the post or the administrator can change or delete it.
* /api/comments/ - The GET method will display a list of all blog comments, the POST method will create a new comment.
* /api/comments/id/ - will display detailed information about a comment with a specific id. Only admin can edit or delete a comment.
* /api/users/ - will display a list of all users if the request is made by a token-authenticated user.
* /api/users/id/ - will display detailed information about a user with a specific id if the request is made by a token-authenticated user.

The blog is implemented so that any user, regardless of whether he is registered or not, can leave a comment.

An example of creating a new comment by the console program http, post_id is the id of the post to which the comment belongs:

```
http POST 127.0.0.1:8000/api/comments/ body="Test text" name="Bob" post_id="66" email="test@gmail.com"
```

Edit existing comment:

```
http --auth admin:password PUT 127.0.0.1:8000/api/comments/35/ body="Edited text comment." name="Bob" post_id="66" email="test@gmail.com"
```

An example of requests to users/:

```
http 127.0.0.1:8000/api/users/ "Authorization: Token 65fc5108dee0d130d508a04748c8e914cf863f64"
```

```
http 127.0.0.1:8000/api/users/2/ "Authorization: Token 65fc5108dee0d130d508a04748c8e914cf863f64"
```

The API also implements *throttling* functionality to limit the number of requests.

### The *django-filter* package is required for filtering, searching and sorting.

#### Для posts/

The filter is implemented by the fields 'title' and 'author'.
An example of a filter by the title field:

```
http ":8000/api/posts/?title=What+is+Django?"
```

An example of a filter on the author field:

```
http ":8000/api/posts/?author=2"
```

An example of filtering by both fields at the same time:

```
http ":8000/api/posts/?author=1&title=What+is+Django?"
```

Sorting is implemented by the fields 'title', 'created', 'status'.
An example of filtering by the author field and sorting by the title field:

```
http ":8000/api/posts/?author=1&ordering=title"
```

An example of filtering by the author field and sorting by the created (creation date) field in reverse order:

```
http ":8000/api/posts/?author=1&ordering=-created"
```

Search is implemented by fields 'title' and 'body', for example:

```
http ":8000/api/posts/?search=django"
http ":8000/api/posts/?search=django&ordering=created"
```

#### comments/

Filtering by fields 'name' and 'email', searching by 'body', sorting by 'created':

```
http ":8000/api/comments/?name=Oleg&search=nuclear&ordering=-created"
```

#### users/

```
http "127.0.0.1:8000/api/users/?search=A&ordering=-id" "Authorization: Token PASTE-TOKEN-HERE"
```

### Pagination produces 4 objects each.

## Russian

## API реализует следующий функционал:

* /api/ - отобразит endpoints.
* /api/posts/ - GET метод отобразит список всех постов блога, POST метод создаст новый пост если пользователь зарегистрирован.
* /api/posts/id/ - отобразит детальную информацию о посте с конкретным id. Автор поста или администратор могут изменить или удалить его.
* /api/comments/ - GET метод отобразит список всех комментариев блога, POST метод создаст новый комминтарий.
* /api/comments/id/ - отобразит детальную информацию о комментарии с конкретным id. Только admin сможет изменить или удалить комментарий.
* /api/users/ - отобразит список всех пользователей если запрос сделан аутентифицировнным при помощи токена пользователем.
* /api/users/id/ - отобразит детальную информацию о пользователе с конкретным id если запрос сделан аутентифицировнным при помощи токена пользователем.

Функционал реализован так чтобы любой пользователь, не зависимо от того зарегистривано он или нет, смог оставить свой комментарий.

Пример создания нового комментария консольной программой http, post_id - id поста к которому относиться комментарий:
http POST 127.0.0.1:8000/api/comments/ body="Test text" name="Bob" post_id="66" email="test@gmail.com"

Изменить существующий комментарий:
http --auth admin:password PUT 127.0.0.1:8000/api/comments/35/ body="Edited text comment." name="Bob" post_id="66" email="test@gmail.com"

Пример запросов к users/:
http 127.0.0.1:8000/api/users/ "Authorization: Token 65fc5108dee0d130d508a04748c8e914cf863f64"
http 127.0.0.1:8000/api/users/2/ "Authorization: Token 65fc5108dee0d130d508a04748c8e914cf863f64"

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

#### Для users/
http "127.0.0.1:8000/api/users/?search=A&ordering=-id" "Authorization: Token PASTE-TOKEN-HERE"

### Пагинация выдает по 4 объекта.
