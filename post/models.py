from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to='post-img')

    # TODO: Define fields here

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('post_detail', kwargs={'pk': self.pk})
