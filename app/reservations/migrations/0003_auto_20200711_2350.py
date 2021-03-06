# Generated by Django 2.2.14 on 2020-07-11 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_reservation_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='pay_with',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='canceled_at',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='is_canceled',
        ),
        migrations.AddField(
            model_name='payment',
            name='canceled_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='card_num',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='is_canceled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[('card', '카드결제'), ('easy', '간편결제')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='pg',
            field=models.CharField(choices=[('payletter', '페이레터'), ('kakao', '카카오페이')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='receipt_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='reservations.Payment'),
        ),
    ]
