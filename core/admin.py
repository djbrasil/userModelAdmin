from django.contrib import admin

from .models import Post

# habilitando models no dashboard admin do django.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')
    exclude = ['autor',]

    # cada autor é um usuario no sistema
    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    # apresenta somente os dados do autor que esta logado
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)

    # alterar o metodo de salvar
    # informar o autor que esta salvando
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)
