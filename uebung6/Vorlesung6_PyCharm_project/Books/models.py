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

    def __str__(self):
        return self.title + ' (' + self.author + ')'

    def __repr__(self):
        return self.get_full_title() + ' / ' + self.author + ' / ' + self.type
