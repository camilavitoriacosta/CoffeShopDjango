# Generated by Django 4.0 on 2021-12-16 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_itens', models.IntegerField()),
                ('total', models.FloatField()),
                ('nome_cliente', models.CharField(max_length=50)),
                ('mesa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=250)),
                ('tamanho', models.IntegerField()),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_produto', models.IntegerField()),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeShopApp.pedido')),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeShopApp.produto')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeShopApp.usuario'),
        ),
    ]
