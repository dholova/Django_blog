from django.db import models

class Post(models.Model):
    '''Дані посту'''
    title = models.CharField('Заголовок посту', max_length=100)
    description = models.TextField('Текст посту')
    author = models.CharField("Ім'я автора", max_length=100)
    date = models.DateField('Дата публікації')
    img = models.ImageField('Зображення', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

class Comments(models.Model):
    '''Коментарі'''
    email = models.EmailField()
    name = models.CharField("Ім'я", max_length=50)
    text_comments = models.TextField('Коментарі', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'

class Likes(models.Model):
    '''Вподобайки'''
    ip = models.CharField('IP-адреса', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)