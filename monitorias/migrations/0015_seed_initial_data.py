from django.db import migrations


def create_initial_data(apps, schema_editor):
    Categoria = apps.get_model("monitorias", "Categoria")
    Beneficio = apps.get_model("monitorias", "Beneficio")

    categorias = [
        "TI",
        "ENGENHARIAS",
        "EXTENSÕES",
    ]

    beneficios = [
        "AAC",
        "CERTIFICADO",
    ]

    for nome in categorias:
        Categoria.objects.get_or_create(nome=nome)

    for nome in beneficios:
        Beneficio.objects.get_or_create(nome=nome)


def reverse_initial_data(apps, schema_editor):
    Categoria = apps.get_model("monitorias", "Categoria")
    Beneficio = apps.get_model("monitorias", "Beneficio")

    Categoria.objects.filter(
        nome__in=["TI", "ENGENHARIAS", "EXTENSÕES"]
    ).delete()

    Beneficio.objects.filter(
        nome__in=["AAC", "CERTIFICADO"]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("monitorias", "0014_rename_owner_monitoria_monitor"),
    ]

    operations = [
        migrations.RunPython(
            create_initial_data,
            reverse_initial_data,
        ),
    ]