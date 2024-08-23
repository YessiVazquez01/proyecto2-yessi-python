tareas = []

def sistemaGestionTareas():
    condicion = True

    while condicion:
        print('Bienvenido al Sistema de Gestion de Tareas \n¿Que desea hacer?')
        print('1) Agregar una tarea \n2) Actualizar una tarea \n3) Marcar una tarea como completada \n4) Listar tareas \n5) Eliminar tarea \n6) Salir')
        accion = int(input('Ingrese la opcion: '))

        if accion == 1:
            codigo = int(input('Codigo: '))
            descripcion_tarea = input('Descripcion: ')
            prioridad_tarea = input('Prioridad: ')
            try:
                agregar_tarea(codigo, descripcion_tarea, prioridad_tarea)
            except ValueError as e:
                print(e)

        elif accion == 2:
            num_id = int(input('¿Que tarea desea modificar?(Indique el codigo): '))
            modificar_descripcion = input('Modifique la descripcion: ')
            modificar_prioridad = input('Modificar la prioridad: ')
            try:
                actualizar_tarea(num_id, modificar_descripcion, modificar_prioridad)
                print('¡Modificado!')
            except KeyError as e:
                print(e)

        elif accion == 3:
            tarea_completada = int(input('¿Que tarea desea marcar como completa? (codigo): '))
            try:
                marcar_completada(tarea_completada)
                print('¡Tarea marcada exitosamente!')
            except KeyError as e:
                print(e)

        elif accion == 4:
            accion2 = input('¿Que tipo de tareas desea ver?(Pendiente\Completadas): ')
            if accion2 == 'Pendiente':
                print('Tareas Pendientes: ',listar_tareas(False))
            elif accion2 == 'Completadas':
                print('Tareas Completadas: ',listar_tareas(True))
            else:
                print('Opcion invalida...')

        elif accion == 5:
            eliminando_tarea = int(input('Ingrese el codigo de la tarea que desea eliminar: '))
            try:
                eliminar_tarea(eliminando_tarea)
                print('¡Tarea eliminada!')
            except KeyError as e:
                print(e)

        elif accion == 6:
            print('Saliendo del sistema... ')
            condicion = False

        else:
            print('Opcion invalida, intente de nuevo...')
            

def agregar_tarea(id_tarea, descripcion, prioridad):
    # Evaluar que no exista una tarea con el mismo ID
    for item in tareas:
        if id_tarea == item['id']:
            raise ValueError(f'Ya existe una tarea con el codigo: {id_tarea}')
    
    # Agregar los datos en un diccionario
    arregloTareas = {
        'id': id_tarea,
        'descripcion': descripcion,
        'prioridad': prioridad,
        'estado': False
    }

    # Agregar el diccionario en un arreglo
    tareas.append(arregloTareas)

    print('¡Agregado!')

def actualizar_tarea(id_tarea, nueva_descripcion, nueva_prioridad):

    for item in tareas:
        if id_tarea != item['id']:
            raise KeyError(f'No existe una tarea con este codigo: {id_tarea}')
        else:
            item['descripcion'] = nueva_descripcion
            item['prioridad'] = nueva_prioridad

def marcar_completada(id_tarea):    
    for item in tareas:
        if id_tarea == item['id']:
            item['estado'] = True
        else:
            raise KeyError(f'No existe una tarea con este codigo: {id_tarea}')

def listar_tareas(completadas=False):
    for item in tareas:
        if completadas == item['estado']:
            return item

def eliminar_tarea(id_tarea): 
    for item in tareas:
        if id_tarea == item['id']:
            tareas.remove(item)
        else:
            raise KeyError(f'No existe una tarea con este codigo: {id_tarea}')

sistemaGestionTareas()
#print(tareas)