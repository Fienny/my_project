from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    author_rating = models.FloatField()

    def update_rating(self, user_rating):
        sum_rating_post = 0
        for post_rate in Post.objects.all():
            sum_rating_post += 3 * post_rate.post_rating
        sum_comment_rating = 0
        for comment_rate in Comment.objects.all():
            sum_comment_rating += comment_rate.comment_rating
        self.author_rating = sum_rating_post + sum_comment_rating + user_rating
        self.save()


class Category(models.Model):
    name = models.CharField(unique=True, null=False, max_length=255)


class Post(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True)
    choice = models.CharField(max_length=255)
    post_date = models.DateTimeField()
    heading = models.CharField(null=False, max_length=255)
    text = models.CharField(max_length=255)
    post_rating = models.FloatField()
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        preview = self.text[0:124] + "..."
        return preview

    def get_absolute_url(self):
        return reverse('new_create', args=[])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(null=False, max_length=255)
    date = models.DateTimeField()
    comment_rating = models.FloatField()

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
