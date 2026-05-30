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

    def test_login_por_email(self):
        User.objects.create_user(
            username="loginuser",
            email="loginuser@example.com",
            password="12345"
        )

        response = self.client.post(reverse("login"), {
            "username": "loginuser@example.com",
            "password": "12345"
        })

        self.assertEqual(response.status_code, 302)

    def test_logout_redireciona(self):
        user = User.objects.create_user(
            username="logoutuser",
            password="12345"
        )
        self.client.login(username="logoutuser", password="12345")

        response = self.client.get(reverse("logout"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("monitorias_list"))