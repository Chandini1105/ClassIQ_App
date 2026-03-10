from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("allocation", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="allocation",
            name="is_cancelled",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="allocation",
            name="cancelled_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="allocation",
            name="cancellation_student_name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="allocation",
            name="cancellation_faculty_name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="allocation",
            name="cancellation_reason",
            field=models.TextField(blank=True),
        ),
    ]

