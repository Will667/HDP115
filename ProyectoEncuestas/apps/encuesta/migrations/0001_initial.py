# Generated by Django 2.0.6 on 2020-07-09 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('iddepartamento', models.AutoField(db_column='IDDEPARTAMENTO', primary_key=True, serialize=False)),
                ('nombredepartamento', models.CharField(db_column='NOMBREDEPARTAMENTO', max_length=30)),
            ],
            options={
                'db_table': 'DEPARTAMENTO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('idmunicipio', models.AutoField(db_column='IDMUNICIPIO', primary_key=True, serialize=False)),
                ('nombremunicipio', models.CharField(db_column='NOMBREMUNICIPIO', max_length=40)),
            ],
            options={
                'db_table': 'MUNICIPIO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('idreclamo', models.AutoField(db_column='IDRECLAMO', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, db_column='DESCRIPCION', null=True)),
            ],
            options={
                'db_table': 'RECLAMO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('idrespuesta', models.AutoField(db_column='IDRESPUESTA', primary_key=True, serialize=False)),
                ('numerodepregunta', models.IntegerField(db_column='NUMERODEPREGUNTA')),
            ],
            options={
                'db_table': 'RESPUESTA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipotrasporte',
            fields=[
                ('idtrasporte', models.AutoField(db_column='IDTRASPORTE', primary_key=True, serialize=False)),
                ('tipo', models.CharField(db_column='TIPO', max_length=10)),
            ],
            options={
                'db_table': 'TIPOTRASPORTE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('dui', models.CharField(db_column='DUI', max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=60)),
                ('apellido', models.CharField(db_column='APELLIDO', max_length=50)),
                ('edad', models.IntegerField(db_column='EDAD')),
                ('sexo', models.CharField(db_column='SEXO', max_length=6)),
                ('domicilio', models.TextField(db_column='DOMICILIO')),
            ],
            options={
                'db_table': 'USUARIO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estacompuesto',
            fields=[
                ('idpregunta', models.ForeignKey(db_column='IDPREGUNTA', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='encuesta.Respuesta')),
                ('fecha', models.DateField(db_column='FECHA')),
            ],
            options={
                'db_table': 'ESTACOMPUESTO',
                'managed': False,
            },
        ),
    ]