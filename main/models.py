from django.db import models

class TinyUrl(models.Model):
    url = models.URLField(verify_exists=False, null=False)
    tiny = models.CharField(null=False, max_length=50)

    def __unicode__(self):
        return "%s - %s" % (str(self.url), self.tiny)
