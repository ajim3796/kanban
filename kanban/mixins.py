from django.contrib.auth.mixins import UserPassesTestMixin


class OnlyYouMixin(UserPassesTestMixin):
    reise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs["pk"]
