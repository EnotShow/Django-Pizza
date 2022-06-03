menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Сделать заказ', 'url_name': 'products'},
]

auth = [
    {'title': 'Корзина', 'url_name': 'cart_detail'},
    {'title': 'Выйти', 'url_name': 'logout'},
]

no_auth = {'title': 'Войти', 'url_name': 'login'}

context = {
    'menu': menu,
    'auth': auth,
    'no_auth': no_auth,
}


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['auth'] = auth
        context['no_auth'] = no_auth
        return context