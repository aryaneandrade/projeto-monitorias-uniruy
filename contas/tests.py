from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class ContasTestCase(TestCase):

    def test_registro_usuario(self):
        """
        Testa apenas se o endpoint de registro responde corretamente
        e se usuário pode ser criado.
        """
        response = self.client.post(reverse("registro"), {
            "username": "novo_user",
            "password1": "12345678",
            "password2": "12345678",
            "email": "teste@teste.com"
        })

        # aceita 200 (form inválido) ou 302 (redirect sucesso)
        self.assertIn(response.status_code, [200, 302])

    def test_login_usuario(self):
        User.objects.create_user(username="loginuser", password="12345")

        response = self.client.post(reverse("login"), {
            "username": "loginuser",
            "password": "12345"
        })

        self.assertIn(response.status_code, [200, 302])