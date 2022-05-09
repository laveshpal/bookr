from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn__exact', 'publisher__name__startswith')
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')

    def isbn13(self, obj):
        return f"{obj.isbn[0:3]}-{obj.isbn[3:4]} - {obj.isbn[4:6]} - {obj.isbn[6:12]} - {obj.isbn[12:13]} "


class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited',)
    # fields = ('content', 'rating', 'creator', 'book')
    fieldsets = ((None, {'fields': ('creator', 'book')}),
                 ('Review content', {'fields': ('content', 'rating')}))

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ('first_names', 'last_names__startswith')
    list_filter = ('last_names', )


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
# admin.site.register(Book, BookAdmin)
