#_*_ utf-8 _*_
from django.db import models

# Create your models here.
class ArticleCatagory(models.Model):
    """
    博客分类
    """
    name = models.CharField(verbose_name=u'类别', max_length=30)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name

class ArticleTag(models.Model):
    """
    博客标签
    """
    name = models.CharField(verbose_name=u'标签', max_length=30)
    # def __unicode__(self):
    #     return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

class blogtext(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'标题')
    catagory = models.ForeignKey('ArticleCatagory',verbose_name='分类',null=True,on_delete=models.SET_NULL)
    tags = models.ManyToManyField('ArticleTag',verbose_name='标签')
    text = models.TextField(verbose_name=u'博文')
    time = models.DateTimeField(verbose_name=u'编辑时间')
    class Meta:
        verbose_name = u'博文'
        verbose_name_plural = verbose_name

class aboutme(models.Model):
    title = models.CharField(max_length=20,verbose_name=u'主题')
    text = models.CharField(max_length=200,verbose_name=u'内容')
    img = models.ImageField(upload_to='avatar/')
    class Meta:
        verbose_name = u'简介'
        verbose_name_plural = verbose_name