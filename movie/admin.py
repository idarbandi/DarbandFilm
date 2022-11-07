from django.contrib import admin

from movie.models import *


class dirAdmin(admin.ModelAdmin):
    list_display = ['name']


class ActAdmin(admin.ModelAdmin):
    list_display = ['name']


class gnrAdmin(admin.ModelAdmin):
    list_display = ['name']


class movieInlineActor(admin.StackedInline):
    model = ActorMovie


class movieInlineDirector(admin.TabularInline):
    model = DirMovie


class movieInlinegenre(admin.TabularInline):
    model = GenreMovie


class imageInline(admin.StackedInline):
    model = MovieImages


class movieAdmin(admin.ModelAdmin):
    list_display = ['name', 'awards', 'year', 'director_id', 'actor_id', 'summary', 'is_active']
    list_filter = ['is_active']
    inlines = [movieInlineDirector, movieInlinegenre, movieInlineActor, imageInline]
    search_fields = ['name', 'year']

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Director, dirAdmin)
admin.site.register(Actor, ActAdmin)
admin.site.register(Genre, gnrAdmin)
admin.site.register(Movie, movieAdmin)