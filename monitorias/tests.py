from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from monitorias.models import Monitoria, Categoria, Beneficio, Inscricao


# =========================
#  TESTES DE MODELO
# =========================
class MonitoriaModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="monitor",
            password="123456"
        )

        self.categoria = Categoria.objects.create(nome="TI")
        self.beneficio = Beneficio.objects.create(nome="Certificado")

        self.monitoria = Monitoria.objects.create(
            titulo="Python",
            descricao="Curso Python",
            categoria=self.categoria,
            beneficio=self.beneficio,
            vagas=5,
            monitor=self.user
        )

    def test_monitoria_criada_corretamente(self):
        self.assertEqual(self.monitoria.titulo, "Python")
        self.assertEqual(self.monitoria.vagas, 5)

    def test_vagas_restantes_inicial(self):
        self.assertEqual(self.monitoria.vagas_restantes, 5)


# =========================
#  TESTES DE INSCRIÇÃO
# =========================
class InscricaoTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("monitor", password="123456")
        self.categoria = Categoria.objects.create(nome="TI")
        self.beneficio = Beneficio.objects.create(nome="Certificado")

        self.monitoria = Monitoria.objects.create(
            titulo="Django",
            descricao="Curso Django",
            categoria=self.categoria,
            beneficio=self.beneficio,
            vagas=2,
            monitor=self.user
        )

    def test_criar_inscricao(self):
        inscricao = Inscricao.objects.create(
            monitoria=self.monitoria,
            nome="Aluno",
            email="aluno@email.com",
            telefone="(71) 99999-9999"
        )

        self.assertEqual(inscricao.email, "aluno@email.com")

    def test_inscricao_duplicada_nao_cria_dois(self):
        Inscricao.objects.create(
            monitoria=self.monitoria,
            nome="Aluno",
            email="aluno@email.com",
            telefone="(71) 99999-9999"
        )

        duplicada = Inscricao.objects.filter(
            monitoria=self.monitoria,
            email="aluno@email.com"
        ).count()

        self.assertEqual(duplicada, 1)


# =========================
#  TESTES DE VIEW
# =========================
class MonitoriaViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username="monitor",
            password="123456"
        )

        self.categoria = Categoria.objects.create(nome="TI")
        self.beneficio = Beneficio.objects.create(nome="Certificado")

        self.monitoria = Monitoria.objects.create(
            titulo="Python",
            descricao="Curso Python",
            categoria=self.categoria,
            beneficio=self.beneficio,
            vagas=5,
            monitor=self.user
        )

    def test_lista_monitorias_status_200(self):
        response = self.client.get(reverse("monitorias_list"))
        self.assertEqual(response.status_code, 200)

    def test_lista_monitorias_exibe_titulo(self):
        response = self.client.get(reverse("monitorias_list"))
        self.assertContains(response, self.monitoria.titulo)

    def test_criar_monitoria_requer_login(self):
        response = self.client.get(reverse("criar_monitoria"))
        self.assertIn(response.status_code, [302, 403])


# =========================
# TESTES DE AUTENTICAÇÃO
# =========================
class AuthTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_registro_usuario_cria_conta(self):
        response = self.client.post(reverse("registro"), {
            "username": "novo_user",
            "email": "novo@email.com",
            "password1": "Senha123456",
            "password2": "Senha123456",
        })

        self.assertEqual(response.status_code, 302)

        user_exists = User.objects.filter(
            username="novo_user"
        ).exists()

        self.assertTrue(user_exists)

    def test_login_funciona(self):
        User.objects.create_user(
            username="user",
            password="123456"
        )

        response = self.client.post(reverse("login"), {
            "username": "user",
            "password": "123456"
        })

        self.assertEqual(response.status_code, 302)