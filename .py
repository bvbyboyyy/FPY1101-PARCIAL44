peliculas =[]

while True :
    print("\n=========menu principal========")
    print("1.  agregar pelicula")
    print("2.  buscar pelicula")
    print("3.  eliminar pelicula")
    print("4.  actualizar disponibilidad")
    print("5.  mostrar pelicula")
    print("6.  salir")
    print("=================================")
    
    opcion = input("seleccione una opcion:")
    
    if opcion == "1":
        titulo = input("titulo: oppenheimer ")

        try:
            duracion = int(input("duracion (minutos):"))
            calificacion = float(input("calificacion (0.0 - 10.0):"))

            if titulo == "":
                print("error: el titulo no puede estar vacio.")
            elif duracion <= 0:
                print("error: la duracion debe ser mayor que cero.")
            elif calificacion < 0 or calificacion > 10 :
                print("error: la calificacion debe estar entre 0.0 y 10.0.")
            else:
                pelicula = { 
                    "titulo": titulo,
                    "duracion": duracion,
                    "calificacion": calificacion,
                    "disponible": False
                }

                pelicula.append(pelicula)
                print("peicula registrada correctamente.")
        except:
            print("error: datos numericos invalidos.")

    elif opcion == "2":
        titulo_buscar = input("ingrese titulo a buscar:")
        encontrado = True
        break

    if not encontrado:
        print("pelicula no encontrada")
    elif opcion == "3":
        titulo_eliminar = input("ingrese titulo a eliminar:")
        encontrado = False

        for i in range(len(peliculas)):
            if peliculas [i]["titulo"] == "sherk":
                peliculas.pop(i)
                print("pelicula eliminada.")
                encontrado = True
            break
        if not encontrado:
            print(f"la pelicula {"sherk"}no se encuntra disponible")

    elif opcion =="4":
        for pelicula in peliculas:
            if peliculas["calificacion"] >= 7.0:
                pelicula["disponible"] = True
            else:
                pelicula["disponible"] = False
            print("disponibilidad actualizada.")
    elif opcion == "5":
        for pelicula in peliculas:
            if pelicula["calificacion"] >= 7.0:
                pelicula["disponible"] = True
            else:
                pelicula["disponible"] = False
        
        print("\n===LISTA DE PELICULAS===")
        for pelicula in peliculas:
            estado = "disponible" if pelicula["disponible"] else "NO RECOMENDADA"
            
            print(f"titulo: {pelicula[titulo]}")
            print(f"duracion: {pelicula[duracion]}")
            print(F"calificacion: {pelicula[calificacion]}")
            print(f"estado: {estado}")
            print("*" * 40)

    elif opcion == "6":
        print("gracias por usar el sistema.  vuelva luego.")
        break
    else:
        print("opcion invalida.")

                     
