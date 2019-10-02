from itertools import count
platillos = [
    {'id' : 0, 'nombre' :'Pozole'}, 
    {'id' : 1, 'nombre' :'Tacos al Pastor'}, 
    {'id' : 2, 'nombre' :'Enchiladas Verdes'}, 
    {'id' : 3, 'nombre' :'Enchiladas Rojas'},
    {'id' : 4, 'nombre' :'Enchiladas de Mole'},
    {'id' : 5, 'nombre' :'Caldo de pollo'},
    {'id' : 6, 'nombre' :'Caldo de res'},
    {'id' : 7, 'nombre' :'Mole de Olla'},
    {'id' : 8, 'nombre' :'Chiles en Nogada'},
    {'id' : 9, 'nombre' :'Tacos dorados de pollo'},
    {'id' : 10, 'nombre' :'Tacos dorados de res'},
    {'id' : 11, 'nombre' :'Tacos dorados de papa'},
    {'id' : 12, 'nombre' :'Tacos dorados combinados'},
    {'id' : 13, 'nombre' :'Especial de la casa'},
    {'id' : 14, 'nombre' :'Cochinita'},
    {'id' : 15, 'nombre' :'Tinga de res'},
    {'id' : 16, 'nombre' :'Tinga de pollo'},
]
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
    def obtenerOrden(self):
        global ordenes
        orden = list(filter(lambda x: x['idCliente'] == self.id, ordenes))
        return orden
    
    def guardar(self):
        global clientes
        clientes.append({
            'id' : self.id,
            'nombre' : self.nombre
        })
        return True

    @classmethod
    def crear(cls, nombre):
        global clientes
        id = next(cls._ids)
        clientes.append({
            'id' : id,
            'nombre' : nombre
        })
        return True

    @classmethod
    def eliminar(cls, id):
        global clientes
        idxs_items = list(
            filter(lambda i_x: i_x[1]['id'] == id, enumerate(clientes)))
        if idxs_items:
            i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
            del clientes[i]
            return True
        else:
            return False
    
    @classmethod
    def obtenerTodos(cls):
        global clientes
        return [cliente for cliente in clientes]

    @classmethod
    def obtener(cls, id):
        global clientes
        cliente = list(filter(lambda x: x['id'] == id, clientes))
        return cliente

class Mesero(object):
    _ids = count(0)
    def __init__(self, nombre : str):
        self.id = next(self._ids)
        self.nombre = nombre

    @property
    def obtenerOrden(self):
        global ordenes
        orden = list(filter(lambda x: x['idMesero'] == self.id, ordenes))
        return orden
    
    def guardar(self):
        global meseros
        meseros.append({
            'id' : self.id,
            'nombre' : self.nombre
        })
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
            return False
    
    @classmethod
    def obtenerTodos(cls):
        global meseros
        return [mesero for mesero in meseros]

    @classmethod
    def obtener(cls, id):
        global meseros
        mesero = list(filter(lambda x: x['id'] == id, meseros))
        return mesero

class Cocineros(object):
    pass

class Ordenes(object):
    pass

class Platillo(object):
    pass