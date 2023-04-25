from django.db import models

class Menu(models.Model):
    name = models.CharField("Имя меню", max_length=50, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
    
class MenuItem(models.Model):
    menu = models.ForeignKey("menu.Menu", verbose_name="Меню", on_delete=models.CASCADE)
    title = models.CharField("Название пункта", max_length=50)
    url = models.CharField("Ссылка/Имя url", max_length=100, blank=True)
    parent = models.ForeignKey('self', verbose_name="Родительский пункт", null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

