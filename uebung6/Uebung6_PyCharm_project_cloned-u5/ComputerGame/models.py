from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import User


class ComputerGame(models.Model):
    name = models.CharField(max_length=50)
    GAMES_TYPES = [('FPS', 'First person shot'), ('PUZ', 'Puzzle'), ('STR', 'Strategy')]
    description = models.CharField(max_length=100,
                                   blank=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='users',
                             related_query_name='user',
                             )

    added_on = models.DateField(blank=True,
                                default=date.today,
                                )
    added_at = models.DateField(blank=True,
                                default=datetime.now(),
                                )
    genre = models.CharField(max_length=3,
                             choices=GAMES_TYPES,
                             )

    class Meta:
        ordering = ['name']
        verbose_name = 'ComputerGame'
        verbose_name_plural = 'ComputerGame'

    def is_spammer(self, user_name: str) -> bool:
        print("self.user->")
        print(self.user)
        return False

# def get_full_title(self):
#    return_string = self.title
# if self.subtitle:  # if subtitle is not empty
#   return_string = self.title + ': ' + self.subtitle
# return return_string

# def __str__(self):
#   return self.title + ' (' + self.author + ')'

# def __repr__(self):
#   return self.get_full_title() + ' / ' + self.author + ' / ' + self.type
