# -*- coding: utf-8 -*-
#%%
import restaurante_v2 as r2
from faker import Faker
import random
from time import sleep
#%%
fake = Faker(locale='es_mx')
r2.Cliente.obtenerTodos()
r2.Cliente.crear(fake.name())
r2.Cliente.crear(fake.name())
r2.Cliente.crear(fake.name())
#%%
clientes = r2.Cliente.obtenerTodos()
#%%
r2.Orden.crear(idCliente = 0, idMesero = 1)
r2.Orden.crear(idCliente = 1, idMesero = 1)
r2.Orden.crear(idCliente = 3, idMesero = 1)
#%%
ordenes = r2.Orden.obtenerTodos()
#%%
c = r2.Cliente.obtener(0)
#%%
o1 = c.orden
