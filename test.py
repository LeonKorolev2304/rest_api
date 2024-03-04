from requests import get, post, delete

# print(get('http://localhost:8080/api/news').json())
# print(get('http://localhost:8080/api/news/1').json())
# print(get('http://localhost:8080/api/news/wqe').json())
# print(get('http://localhost:8080/api/news/2').json())
# print(post('http://localhost:8080/api/news', json={}).json())
'''print(post('http://localhost:8080/api/news',
           json={'title': 'Заголовок'}).json())'''
'''print(post('http://localhost:8080/api/news',
           json={'title': 'Заголовок',
                 'content': 'Новость добавлена через api',
                 'user_id': 2,
                 'is_private': False}).json())'''
# print(delete('http://localhost:8080/api/news/999').json())
# новости с id = 999 нет в базе
print(delete('http://localhost:8080/api/news/5').json())
