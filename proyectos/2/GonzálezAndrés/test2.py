import restaurante as rest
import restaurante_v2 as r2
from faker import Faker
import random
from time import sleep


fake = Faker(locale='es_mx')
r2.Cliente.obtenerTodos()
r2.Cliente.crear(fake.name())
r2.Cliente.crear(fake.name())
r2.Cliente.obtenerTodos()
