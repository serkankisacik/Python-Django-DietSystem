from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from program.models import Category, Program, Images, Comment


class ProgramImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(MPTTModelAdmin):
    list_display = ['title','status',]
    list_filter = ['status']


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag', 'price','status']
    readonly_fields = ('image_tag',)
    list_filter = ['status','category']
    inlines = [ProgramImageInline]
    prepopulated_fields = {'slug': ('title',)}

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'program','image_tag']
    readonly_fields = ('image_tag',)




class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_programs_count', 'related_programs_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Program,
                'category',
                'programs_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Program,
                 'category',
                 'programs_count',
                 cumulative=False)
        return qs

    def related_programs_count(self, instance):
        return instance.programs_count
    related_programs_count.short_description = 'Related programs (for this specific category)'

    def related_programs_cumulative_count(self, instance):
        return instance.programs_cumulative_count
    related_programs_cumulative_count.short_description = 'Related programs (in tree)'




class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','program','user','status']
    list_filter = ['status']






admin.site.register(Category,CategoryAdmin2)
admin.site.register(Program,ProgramAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)

