import re
from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.urls import reverse

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목', help_text = '포스팅 제목을 입력해주세요. 최대 100자')
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    #choices = (
    #    ('제목1', '제목1 레이블'), # ('저장될 값'. 'UI에 보여질 레이블')
    #    ('제목2', '제목2 레이블'),
    #    ('제목3', '제목3 레이블'),
    #))
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    Inglat = models.CharField(max_length=50, blank=True,
        validators = [lnglat_validator],
        help_text='위도/경도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True) # Tag가 뒤에있으니까 문자열로 처리
    # Tag를 위에다가 만들어놓고 그냥 Tag라고 써도 되긴하는데 위 방식으로 할 것.
    # 이거를 Relation을 거는건데 1:N 처럼 Tag 클래스 안에서 구현해도 되지만 이게 더 나음. 종속성.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
       return self.title 
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(Post) # post_id라는 이름의 field가 생긴다!!
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
# Post.objects.filter(tag_set__name:'django') (tag_set__name_in:['django','python']) 등
# 이런식으로 shell에서 쿼리를 날리면 해당 태그가 걸린 Post가 다나옴.
