import pytest
from tareas import agregar_tarea, actualizar_tarea, marcar_completada, listar_tareas, eliminar_tarea, tareas

def setup_function():
    # Se ejecuta antes de cada prueba para limpiar las tareas.
    tareas.clear()

def test_agregar_tarea():
    agregar_tarea(1, 'php', 'baja')
    # assert sirve para indicar que un valor es igual a otro
    assert tareas[0] == {'id': 1, 'descripcion': 'php', 'prioridad':'baja', 'estado': False}

    with pytest.raises(ValueError):
        agregar_tarea(1, 'python', 'alta')

def test_actualizar_tarea():
    agregar_tarea(1, 'php', 'baja')
    actualizar_tarea(1 , 'PHP', 'BAJA')
    assert tareas[0] == {'id': 1, 'descripcion': 'PHP', 'prioridad': 'BAJA', 'estado': False}

    with pytest.raises(KeyError):
        actualizar_tarea(19, 'python', 'alta')

def test_marcar_completada():
    agregar_tarea(1, 'php', 'baja')
    marcar_completada(1)
    assert tareas[0]['estado'] is True

    with pytest.raises(KeyError):
        marcar_completada(8)
    
def test_listar_tareas():
    agregar_tarea(1, 'php', 'baja')
    agregar_tarea(2, 'python', 'alta')

    pendientes = tareas[0]['estado'] = False
    completadas = tareas[1]['estado'] = True

    listar_tareas(pendientes)
    listar_tareas(completadas)

    assert tareas[0] == {'id': 1, 'descripcion': 'php', 'prioridad': 'baja', 'estado': False}

    assert tareas[1] == {'id': 2, 'descripcion': 'python', 'prioridad': 'alta', 'estado': True}

def test_eliminar_tarea():
    agregar_tarea(1, 'php', 'baja')
    agregar_tarea(2, 'python', 'alta')
    eliminar_tarea(1)
    assert 1 not in tareas

    with pytest.raises(KeyError):
        eliminar_tarea(3)