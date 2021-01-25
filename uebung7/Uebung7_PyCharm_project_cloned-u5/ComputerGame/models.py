from datetime import date
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
    genre = models.CharField(max_length=3,
                             choices=GAMES_TYPES,
                             )

    class Meta:
        ordering = ['name']
        verbose_name = 'ComputerGame'
        verbose_name_plural = 'ComputerGame'

    def get_upvotes(self):
        upvotes = Vote.objects.filter(up_or_down='up',
                                      game=self)
        return upvotes

    def get_upvotes_count(self):
        return len(self.get_upvotes())

    def get_downvotes(self):
        downvotes = Vote.objects.filter(up_or_down='down',
                                        game=self)
        return downvotes

    def get_downvotes_count(self):
        return len(self.get_downvotes())

    def vote(self, user, up_or_down):
        vote = Vote.objects.create(up_or_down=up_or_down,
                                   user=user,
                                   game=self
                                   )


class Comment(models.Model):
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(ComputerGame, on_delete=models.CASCADE)

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
    game = models.ForeignKey(ComputerGame, on_delete=models.CASCADE)

    def __str__(self):
        return self.up_or_down + ' on ' + self.ComputerGame.title + ' by ' + self.user.username

# def get_full_title(self):
#    return_string = self.title
# if self.subtitle:  # if subtitle is not empty
#   return_string = self.title + ': ' + self.subtitle
# return return_string

# def __str__(self):
#   return self.title + ' (' + self.author + ')'

# def __repr__(self):
#   return self.get_full_title() + ' / ' + self.author + ' / ' + self.type
