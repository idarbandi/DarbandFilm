from django.contrib import admin

from movie.models import *


class dirAdmin(admin.ModelAdmin):
    list_display = ['name']


class ActAdmin(admin.ModelAdmin):
    list_display = ['name']


class QualityInline(admin.TabularInline):
    model = MovieQuality


class gnrAdmin(admin.ModelAdmin):
    list_display = ['name']


class qualityAdmin(admin.ModelAdmin):
    list_display = ['quality']


class commentAdmin(admin.ModelAdmin):
    list_display = ['body']


class movieInlineActor(admin.StackedInline):
    model = ActorMovie


class movieInlineDirector(admin.TabularInline):
    model = DirMovie


class movieInlinegenre(admin.TabularInline):
    model = GenreMovie


class imageInline(admin.StackedInline):
    model = MovieImages


class movieAdmin(admin.ModelAdmin):
    list_display = ['name', 'awards', 'year', 'summary', 'is_active']
    list_filter = ['is_active']
    inlines = [movieInlineDirector, movieInlinegenre, movieInlineActor, imageInline, QualityInline]
    search_fields = ['name', 'year']

    def has_delete_permission(self, request, obj=None):
        return True


class TrailerAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'summary']


admin.site.register(Movie, movieAdmin)
admin.site.register(Actor, ActAdmin)
admin.site.register(Director, dirAdmin)
admin.site.register(Quality, qualityAdmin)
admin.site.register(Comment, commentAdmin)
admin.site.register(Genre, gnrAdmin)
admin.site.register(Trailer, TrailerAdmin)
