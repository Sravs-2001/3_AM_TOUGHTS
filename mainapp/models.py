from django.db import models

class Concept(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title

class ThoughtPost(models.Model):
    content = models.TextField(blank=True, null=True)
    media = models.FileField(upload_to='thoughts_media/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content[:50] if self.content else "Media Post"
