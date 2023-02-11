
#3 discos
def jogar_3():
    haste_1 = [1, 2, 3]
    haste_2 = [0, 0, 0]
    haste_3 = [0, 0, 0]
    print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3)
    while True:
        disco = int(input("Digite o número do disco que deseja mover: "))
        if (disco != haste_1[0]) and (disco != haste_2[0]) and (disco != haste_3[0]):
            print("O disco selecionado não pode ser movido ! tente outra jogada !")
            continue
        elif disco == 0:
            print("O disco selecionado não pode ser movido pois é uma ferramenta de controle do código ! tente outra jogada !")      
            continue
        else:
            jogada = int(input(f"Digite o número da haste para qual quer mover o disco: "))
            if jogada != 1 and jogada != 2 and jogada != 3:
                print("Essa haste não existe !")
            if jogada == 1 and disco == haste_1[0]:
                print("Esse disco já está nessa haste ! tente mové-lo para outra haste")
                continue             
            elif jogada == 1 and disco != haste_1[0]:
                   if (haste_1[0] != 0 ) and (disco > haste_1[0]):
                       print("Esse disco não pode ser alocado nessa haste ! tente novamente !")
                       continue
                   else:
                       if disco in haste_2:
                           haste_2.remove(disco)
                           haste_2.append(0)
                       elif disco in haste_3:
                           haste_3.remove(disco)
                           haste_3.append(0)
                       haste_1.remove(haste_1[2])
                       haste_1.insert(0, disco)
                       print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3)
               
            elif jogada == 2 and disco == haste_2[0]:
                print("Esse disco já está nessa haste ! tente mové-lo para outra haste")
                continue             
            elif jogada == 2 and disco != haste_2[0]:
                   if (haste_2[0] != 0 ) and (disco > haste_2[0]):
                       print("Esse disco não pode ser alocado nessa haste ! tente novamente !")
                       continue
                   else:
                       if disco in haste_1:
                           haste_1.remove(disco)
                           haste_1.append(0)
                       elif disco in haste_3:
                           haste_3.remove(disco)
                           haste_3.append(0)
                       haste_2.remove(haste_2[2])
                       haste_2.insert(0, disco)
                       print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3)

            elif jogada == 3 and disco == haste_3[0]:
                print("Esse disco já está nessa haste ! tente mové-lo para outra haste")
                continue             
            elif jogada == 3 and disco != haste_3[0]:
                   if (haste_3[0] != 0 ) and (disco > haste_3[0]):
                       print("Esse disco não pode ser alocado nessa haste ! tente novamente !")
                       continue
                     
                   else:
                       if disco in haste_1:
                           haste_1.remove(disco)
                           haste_1.append(0)
                       elif disco in haste_2:
                           haste_2.remove(disco)
                           haste_2.append(0)
                       haste_3.remove(haste_3[2])
                       haste_3.insert(0, disco)
                       print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3 )      
            if  haste_2 == [1, 2, 3]:
                 print("Você ganhou !!")
                 break
            if  haste_3 == [1, 2, 3]:
                 print("Você ganhou !!")
                 break
             
#4 discos
def jogar_4():
    haste_1 = [1, 2, 3, 4]
    haste_2 = [0, 0, 0, 0]
    haste_3 = [0, 0, 0, 0]
    print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3)
    while True:
        disco = int(input("Digite o número do disco que deseja mover: "))
        if (disco != haste_1[0]) and (disco != haste_2[0]) and (disco != haste_3[0]):
            print("O disco selecionado não pode ser movido ! tente outra jogada !")
            continue
        elif disco == 0:
            print("O disco selecionado não pode ser movido pois é uma ferramenta de controle do código ! tente outra jogada !")      
            continue
        else:
            jogada = int(input(f"Digite o número da haste para qual quer mover o disco: "))
            if jogada != 1 and jogada != 2 and jogada != 3:
                print("Essa haste não existe !")
            if jogada == 1 and disco == haste_1[0]:
                print("Esse disco já está nessa haste ! tente mové-lo para outra haste")
                continue             
            elif jogada == 1 and disco != haste_1[0]:
                   if (haste_1[0] != 0 ) and (disco > haste_1[0]):
                       print("Esse disco não pode ser alocado nessa haste ! tente novamente !")
                       continue
                   else:
                       if disco in haste_2:
                           haste_2.remove(disco)
                           haste_2.append(0)
                       elif disco in haste_3:
                           haste_3.remove(disco)
                           haste_3.append(0)
                       haste_1.remove(haste_1[3])
                       haste_1.insert(0, disco)
                       print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3)
               
            elif jogada == 2 and disco == haste_2[0]:
                print("Esse disco já está nessa haste ! tente mové-lo para outra haste")
                continue             
            elif jogada == 2 and disco != haste_2[0]:
                   if (haste_2[0] != 0 ) and (disco > haste_2[0]):
                       print("Esse disco não pode ser alocado nessa haste ! tente novamente !")
                       continue
                   else:
                       if disco in haste_1:
                           haste_1.remove(disco)
                           haste_1.append(0)
                       elif disco in haste_3:
                           haste_3.remove(disco)
                           haste_3.append(0)
                       haste_2.remove(haste_2[3])
                       haste_2.insert(0, disco)
                       print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3)

            elif jogada == 3 and disco == haste_3[0]:
                print("Esse disco já está nessa haste ! tente mové-lo para outra haste")
                continue             
            elif jogada == 3 and disco != haste_3[0]:
                   if (haste_3[0] != 0 ) and (disco > haste_3[0]):
                       print("Esse disco não pode ser alocado nessa haste ! tente novamente !")
                       continue
                     
                   else:
                       if disco in haste_1:
                           haste_1.remove(disco)
                           haste_1.append(0)
                       elif disco in haste_2:
                           haste_2.remove(disco)
                           haste_2.append(0)
                       haste_3.remove(haste_3[3])
                       haste_3.insert(0, disco)
                       print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3 )
            
            if  haste_2 == [1, 2, 3, 4]:
                 print("Você ganhou !!")
                 break
            if  haste_3 == [1, 2, 3, 4]:
                 print("Você ganhou !!")
                 break
                 
#5 discos         
def jogar_5():
    haste_1 = [1, 2, 3, 4, 5]
    haste_2 = [0, 0, 0, 0, 0]
    haste_3 = [0, 0, 0, 0, 0]
    print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3)
    while True:
        disco = int(input("Digite o número do disco que deseja mover: "))
        if (disco != haste_1[0]) and (disco != haste_2[0]) and (disco != haste_3[0]):
            print("O disco selecionado não pode ser movido ! tente outra jogada !")
            continue
        elif disco == 0:
            print("O disco selecionado não pode ser movido pois é uma ferramenta de controle do código ! tente outra jogada !")      
            continue
        else:
            jogada = int(input(f"Digite o número da haste para qual quer mover o disco: "))
            if jogada != 1 and jogada != 2 and jogada != 3:
                print("Essa haste não existe !")
            if jogada == 1 and disco == haste_1[0]:
                print("Esse disco já está nessa haste ! tente mové-lo para outra haste")
                continue             
            elif jogada == 1 and disco != haste_1[0]:
                   if (haste_1[0] != 0 ) and (disco > haste_1[0]):
                       print("Esse disco não pode ser alocado nessa haste ! tente novamente !")
                       continue
                   else:
                       if disco in haste_2:
                           haste_2.remove(disco)
                           haste_2.append(0)
                       elif disco in haste_3:
                           haste_3.remove(disco)
                           haste_3.append(0)
                       haste_1.remove(haste_1[4])
                       haste_1.insert(0, disco)
                       print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3)
               
            elif jogada == 2 and disco == haste_2[0]:
                print("Esse disco já está nessa haste ! tente mové-lo para outra haste")
                continue             
            elif jogada == 2 and disco != haste_2[0]:
                   if (haste_2[0] != 0 ) and (disco > haste_2[0]):
                       print("Esse disco não pode ser alocado nessa haste ! tente novamente !")
                       continue
                   else:
                       if disco in haste_1:
                           haste_1.remove(disco)
                           haste_1.append(0)
                       elif disco in haste_3:
                           haste_3.remove(disco)
                           haste_3.append(0)
                       haste_2.remove(haste_2[4])
                       haste_2.insert(0, disco)
                       print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3)

            elif jogada == 3 and disco == haste_3[0]:
                print("Esse disco já está nessa haste ! tente mové-lo para outra haste")
                continue             
            elif jogada == 3 and disco != haste_3[0]:
                   if (haste_3[0] != 0 ) and (disco > haste_3[0]):
                       print("Esse disco não pode ser alocado nessa haste ! tente novamente !")
                       continue
                     
                   else:
                       if disco in haste_1:
                           haste_1.remove(disco)
                           haste_1.append(0)
                       elif disco in haste_2:
                           haste_2.remove(disco)
                           haste_2.append(0)
                       haste_3.remove(haste_3[4])
                       haste_3.insert(0, disco)
                       print("Haste 1:",haste_1,"\nHaste 2:",haste_2,"\nHaste 3:",haste_3 )
            
            if  haste_2 == [1, 2, 3, 4, 5]:
                 print("Você ganhou !!")
                 break
            if  haste_3 == [1, 2, 3, 4, 5]:
                 print("Você ganhou !!")
                 break
#Menu de opções
def menu():
    print("1 - Nivel fácil: possui 3 discos \n2 - Nivel médio: possui 4 discos \n3 - Nivel dificil: possui 5 discos")
    opcao= int(input("Digite o nivel que deseja jogar: "))
    if opcao == 1:
        jogar_3()
    elif opcao == 2:
        jogar_4()
    elif opcao == 3:
        jogar_5()
  
menu()