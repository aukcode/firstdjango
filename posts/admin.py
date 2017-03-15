from django.contrib import admin

# Register your models here.
from .models import Post #Henter Post modellen fra models
from .models import Del_Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_display_links = ['updated'] #Styrer hva som er klikkbart
    list_filter = ['updated', 'title'] #Man kan ha flere filtre
    list_editable = ['title'] #Lar deg endre on the fly
    search_fields = ['title', 'content'] #title og content er hva som er søkbart
    class Meta:
        model = Post

admin.site.register(Del_Post)

admin.site.register(Post, PostModelAdmin)   #Registrer Post modellen til admin.py siden (mao, den dukker opp på django administration

