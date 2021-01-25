from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    BOOK_TYPES = [
        ('H', 'Hardcover'),  # Wert und lesbare Form
        ('P', 'Paperback'),
        ('E', 'E-book'),
        ('A', 'Audio book'),
    ]

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100,
                                blank=True)
    author = models.CharField(max_length=50)
    pages = models.IntegerField()  # Must call function to take effect
    date_published = models.DateField(blank=True,
                                      default=date.today,
                                      )
    type = models.CharField(max_length=1,
                            choices=BOOK_TYPES,
                            )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='book_created_by',
                             related_query_name='book_created_by',
                             )

    class Meta:
        ordering = ['title', '-type']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def check_date_published(self):
        print('----- In Book.check_date_published():', self.date_published, 'vs.', date.today())

        if self.date_published > date.today():
            print('----- Warning: date_published is in the future')
            return False
        else:
            return True

    def get_full_title(self):
        return_string = self.title
        if self.subtitle:  # if subtitle is not empty
            return_string = self.title + ': ' + self.subtitle
        return return_string

    def get_upvotes(self):
        upvotes = Vote.objects.filter(up_or_down='up',
                                      book=self)
        return upvotes

    def get_upvotes_count(self):
        return len(self.get_upvotes())

    def get_downvotes(self):
        downvotes = Vote.objects.filter(up_or_down='down',
                                        book=self)
        return downvotes

    def get_downvotes_count(self):
        return len(self.get_downvotes())

    def vote(self, user, up_or_down):
        vote = Vote.objects.create(up_or_down=up_or_down,
                                   user=user,
                                   book=self
                                   )

    def __str__(self):
        return self.title + ' (' + self.author + ')'

    def __repr__(self):
        return self.get_full_title() + ' / ' + self.author + ' / ' + self.type


class Comment(models.Model):
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def get_comment_prefix(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text

    def __str__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ')'

    def __repr__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ' / ' + str(self.timestamp) + ')'


class Vote(models.Model):
    VOTE_TYPES = [
        ('U', 'up'),
        ('D', 'down'),
    ]

    up_or_down = models.CharField(max_length=1,
                                  choices=VOTE_TYPES,
                                 )
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.up_or_down + ' on ' + self.book.title + ' by ' + self.user.username
