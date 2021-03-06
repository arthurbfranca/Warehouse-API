# Generated by Django 3.1.3 on 2020-12-05 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Cid', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('Caddress', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('role', models.CharField(default='worker', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('Item_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Dimensions', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('Route_id', models.IntegerField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('Transaction_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('Driver_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.employee')),
                ('Route_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.route')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('Vehicle_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('Warehouse_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('admin_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('Transaction_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('Transaction_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('Transaction_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Works_At',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Warehouse_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.warehouse')),
                ('Worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='WH_Receiver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='WH_Sender_id', to='api.warehouse'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='WH_Sender_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='WH_Receiver_id', to='api.warehouse'),
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Unnamed', max_length=100)),
                ('Total_space', models.DecimalField(decimal_places=2, default=100, max_digits=8)),
                ('Warehouse_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default=1)),
                ('Item_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.item')),
                ('Subsection_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.subsection')),
                ('Warehouse_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default=1)),
                ('Status', models.BooleanField(default=False)),
                ('Cid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('Driver_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.employee')),
                ('Item_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.item')),
                ('Route_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.route')),
            ],
        ),
        migrations.AddConstraint(
            model_name='employee',
            constraint=models.CheckConstraint(check=models.Q(('role__exact', 'worker'), ('role__exact', 'admin'), ('role__exact', 'driver'), ('role__exact', 'exec'), _connector='OR'), name='valid workers'),
        ),
        migrations.AddField(
            model_name='drive',
            name='Driver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee'),
        ),
        migrations.AddField(
            model_name='drive',
            name='Vehicle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle'),
        ),
        migrations.AlterUniqueTogether(
            name='works_at',
            unique_together={('Worker_id', 'Warehouse_id')},
        ),
        migrations.AddField(
            model_name='transfer',
            name='Item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.item'),
        ),
        migrations.AlterUniqueTogether(
            name='subsection',
            unique_together={('Warehouse_id', 'Name')},
        ),
        migrations.AlterUniqueTogether(
            name='store',
            unique_together={('Warehouse_id', 'Subsection_name', 'Item_id')},
        ),
        migrations.AlterUniqueTogether(
            name='ship',
            unique_together={('Cid', 'Item_id')},
        ),
        migrations.AddField(
            model_name='request',
            name='Admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.employee'),
        ),
        migrations.AddField(
            model_name='issue',
            name='Exec_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.employee'),
        ),
        migrations.AlterUniqueTogether(
            name='drive',
            unique_together={('Vehicle_id', 'Driver_id')},
        ),
    ]
