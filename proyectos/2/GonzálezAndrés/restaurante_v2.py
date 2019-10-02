# -*- coding: utf-8 -*-
from itertools import count
import threading as th

platillos = []
clientes = []
meseros = []
cocineros = []
ordenes = []
ordenes_platillos = []

class Cliente(object):
    _ids = count(0)
    def __init__(self, nombre : str):
        self.id = next(self._ids)
        self.nombre = nombre

    @property
    def orden(self):
        global ordenes
        try:
            orden = list(filter(lambda x: x.idCliente == self.id, ordenes))[0]
        except IndexError as e:
            print('No tiene órdenes registradas')
            return None
        return orden
    
    def guardar(self):
        global clientes
        clientes.append(self)
        return True

    @classmethod
    def crear(cls, nombre):
        global clientes
        #id = next(cls._ids)
        clientes.append(cls(nombre))
        return True

    @classmethod
    def eliminar(cls, id):
        global clientes
        idxs_items = list(
            filter(lambda i_x: i_x[1].id == id, enumerate(clientes)))
        if idxs_items:
            i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
            del clientes[i]
            return True
        else:
            return None
    
    @classmethod
    def obtenerTodos(cls):
        global clientes
        return [cliente for cliente in clientes]

    @classmethod
    def obtener(cls, id):
        global clientes
        try:
            cliente = list(filter(lambda x: x.id == id, clientes))[0]
        except IndexError as e:
            print('No se encontró el cliente')
            return None
        return cliente
    
    def __str__(self):
        return self.nombre

class Mesero(object):
    _ids = count(0)
    def __init__(self, nombre : str):
        self.id = next(self._ids)
        self.nombre = nombre

    @property
    def orden(self):
        global ordenes
        orden = list(filter(lambda x: x.idMesero == self.id, ordenes))
        return orden
    
    def guardar(self):
        global meseros
        meseros.append(self)
        return True

    @classmethod
    def crear(cls, nombre):
        global meseros
        meseros.append(cls(nombre))
        return True

    @classmethod
    def eliminar(cls, id):
        global meseros
        idxs_items = list(
            filter(lambda i_x: i_x[1].id == id, enumerate(meseros)))
        if idxs_items:
            i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
            del meseros[i]
            return True
        else:
            return None
    
    @classmethod
    def obtenerTodos(cls):
        global meseros
        return [mesero for mesero in meseros]

    @classmethod
    def obtener(cls, id):
        global meseros
        try:
            mesero = list(filter(lambda x: x.id == id, meseros))[0]
        except IndexError as e:
            return None
        return mesero

class Cocinero(object):
    _ids = count(0)
    def __init__(self, nombre):
        self.id = next(self._ids)
        self.nombre = nombre

class Orden(object):
    _ids = count(0)
    def __init__(self, idCliente = None, idMesero = None):
        self.id = next(self._ids)
        self.idMesero = idMesero
        self.idCliente = idCliente
    
    def guardar(self):
        global ordenes
        ordenes.append(self)
        return True

    @property
    def mesero(self):
        global meseros
        try:
            mesero = list(filter(lambda x: x.id == self.idMesero, meseros))
        except IndexError as e:
            print('La orden no tiene asignada ningún mesero')
            return None
        return mesero

    @property
    def cliente(self):
        global clientes
        try:
            cliente = list(filter(lambda x: x.id == self.idCliente, clientes))[0]
        except IndexError as e:
            print('La orden no le pertenece a ningún cliente')
            return None
        return cliente

    @classmethod
    def crear(cls, idMesero = None, idCliente = None):
        global ordenes
        ordenes.append(cls(idMesero, idCliente))
        return True
    
    @classmethod
    def obtenerTodos(cls):
        global ordenes
        return [orden for orden in ordenes]

    @classmethod
    def obtener(cls, id):
        global ordenes
        try:
            orden = list(filter(lambda x: x.id == id, ordenes))[0]
        except IndexError as e:
            return None
        return orden

class Platillo(object):
    _ids = count(0)
    def __init__(self, nombre : str):
        self.id = next(self._ids)
        self.nombre = nombre

    @property
    def orden(self):
        global ordenes
        orden = list(filter(lambda x: x.idMesero == self.id, ordenes))
        return orden
    
    def guardar(self):
        global meseros
        meseros.append(self)
        return True

    @classmethod
    def crear(cls, nombre):
        global meseros
        id = next(cls._ids)
        meseros.append({
            'id' : id,
            'nombre' : nombre
        })
        return True

    @classmethod
    def eliminar(cls, id):
        global meseros
        idxs_items = list(
            filter(lambda i_x: i_x[1]['id'] == id, enumerate(meseros)))
        if idxs_items:
            i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
            del meseros[i]
            return True
        else:
            return None
    
    @classmethod
    def obtenerTodos(cls):
        global meseros
        return [mesero for mesero in meseros]

    @classmethod
    def obtener(cls, id):
        global meseros
        mesero = list(filter(lambda x: x['id'] == id, meseros))[0]
        return mesero

platillos = [Platillo(nombre) for nombre in
    ['Pozole', 
    'Tacos al Pastor', 
    'Enchiladas Verdes', 
    'Enchiladas Rojas',
    'Enchiladas de Mole',
    'Caldo de pollo',
    'Caldo de res',
    'Mole de Olla',
    'Chiles en Nogada',
    'Tacos dorados de pollo',
    'Tacos dorados de res',
    'Tacos dorados de papa',
    'Tacos dorados combinados',
    'Especial de la casa',
    'Cochinita',
    'Tinga de res',
    'Tinga de pollo',]
]