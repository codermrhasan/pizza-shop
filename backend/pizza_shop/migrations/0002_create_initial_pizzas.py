from django.db import migrations

def create_pizzas(apps, schema_editor):
    Pizza = apps.get_model('pizza_shop', 'Pizza')
    Pizza.objects.create(name='Lebanese Chicken', description='Lebanese chicken, capsicum,sweet corn.', price=4)
    Pizza.objects.create(name='Farmhouse', description='Smoked chicken, mushroom, sweet corn, black olives.', price=4)
    Pizza.objects.create(name='Smoked Chicken', description='Smoked chicken, capsicum, jalapenos.', price=4)
    Pizza.objects.create(name='Spicy Chicken', description='Lebanese chicken, mushroom, onion, green chilies.', price=4)
    Pizza.objects.create(name='Smokey Buzz', description='Smoked chicken, mushroom, onion, red paprika.', price=4)
    Pizza.objects.create(name='Bbq Temptation', description='Spicy chicken marinated in BBQ sauce, onions, capsicum, tomatoes, green chilies.', price=4)

class Migration(migrations.Migration):
    dependencies = [
        ('pizza_shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_pizzas),
    ]