from customers.models import Domain
from customers.models import Client
client = Client.objects.create(schema_name="public", name="RGPV")

Domain.objects.create(
    domain='localhost',
    tenant=client,
    is_primary=True
)


# urls
'''
for school
http://school1.localhost:8000/students/
for school admin
http://school1.localhost:8000/admin
fro public admin 
http://localhost:8000/
'''

'''
python manage.py migrate_schemas --shared
python manage.py tenant_command migrate
python manage.py tenant_command createsuperuser --schema=school1

'''
'''
Docker run configuration
TODO: 
1. docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres
to get the details about port and other things
2. docker ps



'''