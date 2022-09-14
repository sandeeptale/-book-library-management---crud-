

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210415_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fine',
            name='datetime_of_payment',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
