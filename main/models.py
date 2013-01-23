from django.db import models
import random


class TinyUrl(models.Model):
    url = models.URLField(verify_exists=False, null=False)
    tiny = models.CharField(null=False, max_length=50)

    def save(self, *args, **kwargs):

        self.tiny = self.generate_slug()

        try:
            found = TinyUrl.objects.filter(tinyurl=slug).count()

            while found != 0:
                self.tiny = self.generate_slug()
                found = TinyUrl.objects.filter(tinyurl=slug).count()

        except Exception, e:
            pass

        super(TinyUrl, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return "%s - %s" % (str(self.url), self.tiny)

    def generate_slug(self):

        h = [chr(random.randrange(65, 91)), chr(random.randrange(97, 123)),
        random.randrange(0, 10), chr(random.randrange(97, 123)),
        chr(random.randrange(97, 123))]

        random.shuffle(h)

        return ''.join(str(i) for i in h)
