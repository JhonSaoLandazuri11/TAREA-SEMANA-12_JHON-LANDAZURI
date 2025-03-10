from Biblioteca import Biblioteca
from Libro import Libro
from Usuario import Usuario

# Menú interactivo
biblioteca = Biblioteca()

while True:
    print("\nMenú de Biblioteca:")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        isbn = input("ISBN: ")
        biblioteca.agregar_libro(Libro(titulo, autor, categoria, isbn))
    elif opcion == "2":
        isbn = input("ISBN del libro a eliminar: ")
        biblioteca.quitar_libro(isbn)
    elif opcion == "3":
        nombre = input("Nombre del usuario: ")
        id_usuario = input("ID de usuario: ")
        biblioteca.registrar_usuario(Usuario(nombre, id_usuario))
    elif opcion == "4":
        id_usuario = input("ID de usuario a eliminar: ")
        biblioteca.dar_de_baja_usuario(id_usuario)
    elif opcion == "5":
        id_usuario = input("ID del usuario: ")
        isbn = input("ISBN del libro: ")
        biblioteca.prestar_libro(id_usuario, isbn)
    elif opcion == "6":
        id_usuario = input("ID del usuario: ")
        isbn = input("ISBN del libro a devolver: ")
        biblioteca.devolver_libro(id_usuario, isbn)
    elif opcion == "7":
        criterio = input("Buscar por (titulo/autor/categoria): ")
        valor = input("Valor de búsqueda: ")
        biblioteca.buscar_libro(criterio, valor)
    elif opcion == "8":
        id_usuario = input("ID del usuario: ")
        biblioteca.listar_libros_prestados(id_usuario)
    elif opcion == "9":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")