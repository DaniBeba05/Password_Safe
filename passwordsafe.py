import module


p = module.Password("", 0)

while p.comprobar_num_intentos():

    p.introducirpassword()

    if p.tiene_longitud_maxima():

        if not p.tiene_una_mayuscula():

            print(p.mensajerequisitomayuscula())

        elif not p.tiene_un_numero():

            print(p.mensajerequisitonumero())

        elif not p.tiene_un_simbolo():

            print(p.mensajerequisitosimbolo())


        if p.comprobar_password_valida():
            break


        p.sumar_num_intentos()

        if not p.comprobar_num_intentos():
            print(p.mensajedesuperaciondeintentos())

    else:


        print(p.mensajerequisitonumcaracteres())
        p.sumar_num_intentos()

        if not p.comprobar_num_intentos():
            print(p.mensajedesuperaciondeintentos())


if (p.comprobar_password_valida()):
    print (p.mensajedepasswordvalida())
