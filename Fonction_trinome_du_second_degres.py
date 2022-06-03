while True:
    print("#####################################")
    print("# Fonction trinôme du second degrès #")
    print("#####################################")
    print()
    print()
    print("      #######################")
    print("      # 1 = Forme canonique #")
    print("      # 2 = Racines         #")
    print("      # 3 = Tableaux        #")
    print("      # 4 = Forme initiale  #")
    print("      #######################")
    print()
    print()
    program=int(input("Entrez le chiffre qui correspond au programme en question : "))
    print()
    print()

    if program==1:
        a=float(input("Entrez la valeur de a: "))

        if a==0:
           print("a ne peut être égale à 0")
           input("Appuyez sur Entrée, le programme va s'arrêter...")
           exit()

        b=float(input("Entrez la valeur de b: "))
        c=float(input("Entrez la valeur de c: "))

        alpha =((-1)*(b)/(2*a))
        beta = (a*(alpha*alpha)+b*alpha+c)
        alpha=round(alpha,2)
        beta=round(beta,2)
        if beta>=0 and alpha>=0:
            print(a,"*( x -",alpha,")² +",beta,)

        elif beta<0 and alpha>=0:
            print(a,"*( x -",alpha,")² -",abs(beta),)

        elif beta>=0 and alpha<0:
            print(a,"*( x +",abs(alpha),")² +",beta,)

        elif beta<0 and alpha<0:
            print(a,"*( x +",abs(alpha),")² -",abs(beta),)
        
        rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
            
        if rep2=="oui":
            exit()
        elif rep2=="non":
            print("Alors continuons !")
        print()
        print()
    
    if program==2:
        a=float(input("Entrez la valeur de a: "))

        if a==0:
           print("a ne peut être égale à 0")
           input("Appuyez sur Entrée, le programme va s'arrêter...")
           exit()
        
        b=float(input("Entrez la valeur de b: "))
        print(b)
        c=float(input("Entrez la valeur de c: "))

        delta=(b**2)-(4*a*c)
        print("La valeur de delta est : ",delta,)
        if delta==0:
            x0=-float((-b)/(2*a))
            print (b)
            print("La racine de la fonction est : ",x0,)
            rep=input("Est-ce que vous voulez la forme factorisé ? (oui/non) : ")
            if rep=="oui":
                if x0>0:
                    print(a,"*(x -",x0,")²")
                elif x0<0:
                    print(a,"*(x +",abs(x0),")²")
                rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                if rep2=="oui":
                    exit()
                elif rep2=="non":
                    print("Alors continuons !")    
            elif rep=="non":
                rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                if rep2=="oui":
                    exit()
                elif rep2=="non":
                    print("Alors continuons !")
        elif delta<0:
            print("a fonction f(x) ne possède pas de racines réels")
            rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
            if rep2=="oui":
                exit()
            elif rep2=="non":
                print("Alors continuons !")
        elif delta>0:
            from math import *
            racine=sqrt(delta)
            x1=((-b)+racine)/(2*a)
            x2=((-b)-racine)/(2*a)
            x1=round(x1,2)
            x2=round(x2,2)
            print("Les racines de la fonction sont,",x1,"et",x2)
            rep=input("Est-ce que vous voulez la forme factorisé ? (oui/non) : ")
            if rep=="oui":
                if x1>0 and x2>0:
                    print(a,"*(x +",x1,")(x -",x2,")")
                elif x1<0 and x2<0:
                    print(a,"*(x +",abs(x1),")(x +",abs(x2),")")
                elif x1<0 and x2>0:
                    print(a,"*(x +",abs(x1),")(x -",x2,")")
                elif x1>0 and x2<0:
                    print(a,"*(x -",x1,")(x +",abs(x2),")")
            rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
            if rep2=="oui":
                exit()
            elif rep2=="non":
                print("Alors continuons !")

    if program==3:
        print("        ############")
        print("        # Tableaux #")
        print("        ############")
        print()
        print()
        print("############################")
        print("# 1 = Tableau de signe     #")
        print("# 2 = Tableau de variation #")
        print("############################")
        print()
        print()
        tbl=int(input("Entrez le chiffre qui correspond au tableau en question : "))
        if tbl==1:
            a=float(input("Entrez la valeur de a: "))

            if a==0:
                print("a ne peut être égale à 0")
                input("Appuyez sur Entrée, le programme va s'arrêter...")
                exit()  

            b=float(input("Entrez la valeur de b: "))
            c=float(input("Entrez la valeur de c: "))
            print()
            print()
            delta=(b**2)-4*a*c
            if delta<0 :
                if a<0 :
                        print("  _____________________")                    
                        print(" | x |- infini  +infini|")
                        print(" |___|_________________|")
                        print(" |   |                 |")
                        print(" | f |         -       |")
                        print(" |___|_________________|")
                        print()
                        print()
                if a>0 :
                        print("  _____________________")                    
                        print(" | x |- infini  +infini|")
                        print(" |___|_________________|")
                        print(" |   |                 |")
                        print(" | f |         +       |")
                        print(" |___|_________________|")
                        print()
                        print()
                rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                if rep2=="oui":
                    exit()
                elif rep2=="non":
                    print("Alors continuons !")
                    print()
                    print()
            if delta>0:
                from math import *
                racine=sqrt(delta)
                x1=((-b)+racine)/(2*a)
                x2=((-b)-racine)/(2*a)
                x1=round(x1,2)
                x2=round(x2,2)
                if x1<a<x2:
                    print("  ___________________________________________________")
                    print(" | x |- infini       ",x1,"       ",x2,"    +infini|")
                    print(" |___|_______________________________________________|")
                    print(" |   |                 |            |                |")
                    print(" | f |         +       O      -     O        +       |")
                    print(" |___|_________________|____________|________________|")
                elif x2<a<x1:
                    print("  ___________________________________________________")
                    print(" | x |- infini       ",x2,"       ",x1,"    +infini|")
                    print(" |___|_______________________________________________|")
                    print(" |   |                 |            |                |")
                    print(" | f |         +       O      -     O        +       |")
                    print(" |___|_________________|____________|________________|")
                elif a<x1<x2 or x1<x2<a:
                    print("  ___________________________________________________")
                    print(" | x |- infini       ",x1,"       ",x2,"    +infini|")
                    print(" |___|_______________________________________________|")
                    print(" |   |                 |            |                |")
                    print(" | f |         -       O      +     O        -       |")
                    print(" |___|_________________|____________|________________|")
                elif a<x2<x1 or x2<x1<a:
                    print("  ___________________________________________________")
                    print(" | x |- infini       ",x2,"       ",x1,"    +infini|")
                    print(" |___|_______________________________________________|")
                    print(" |   |                 |            |                |")
                    print(" | f |         -       O      +     O        -       |")
                    print(" |___|_________________|____________|________________|")
                    print()
                    print()
                rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                if rep2=="oui":
                    exit()
                elif rep2=="non":
                    print("Alors continuons !")
                    print()
                    print()
                
                if delta==0:
                    x0=((-b)/(2*a))
                    x0=round(x0,2)
                    if a>0:
                        print("  _______________________________________")                    
                        print(" | x |- infini       ",x0,"    +infini|")
                        print(" |___|__________________________________|")
                        print(" |   |                 |                |")
                        print(" | f |         +       O        +       |")
                        print(" |___|_________________|________________|")
                        print()
                        print()
                    if a<0:
                        print("  _______________________________________")                    
                        print(" | x |- infini       ",x0,"    +infini|")
                        print(" |___|__________________________________|")
                        print(" |   |                 |                |")
                        print(" | f |         -       O        -       |")
                        print(" |___|_________________|________________|")
                        print()
                        print()
                    rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                    if rep2=="oui":
                        exit()
                    elif rep2=="non":
                        print("Alors continuons !")
        
        if tbl==2:
            a=float(input("Entrez la valeur de a: "))

            if a==0:
                print("a ne peut être égale à 0")
                input("Appuyez sur Entrée, le programme va s'arrêter...")
                exit()   

            b=float(input("Entrez la valeur de b: "))
            c=float(input("Entrez la valeur de c: "))
            print()
            print()
            alpha =((-b)/(2*a))
            beta = (a*(alpha*alpha)+b*alpha+c)
            alpha=round(alpha,2)
            beta=round(beta,2)
            if alpha<0:
                 print("  ___________________________________________")                    
                 print(" | x |- infini       ",alpha,"          +infini |")
                 print(" |___|_______________________________________|")
                 print(" |   |                                       |")
                 print(" |   |   décroissant            croissant    |")
                 print(" | f |                                       |")
                 print(" |   |                ",beta,"                  |")
                 print(" |___|_______________________________________|")
                 print()
                 print()
            if alpha>0:
                 print("  ___________________________________________")                    
                 print(" | x |- infini       ",alpha,"          +infini |")
                 print(" |___|_______________________________________|")
                 print(" |   |                                       |")
                 print(" |   |               ",beta,"                   |")
                 print(" | f |                                       |")
                 print(" |   |   croissant            décroissant    |")
                 print(" |___|_______________________________________|")
                 print()
                 print()
            rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
            if rep2=="oui":
                exit()
            elif rep2=="non":
                print("Alors continuons !")

    if program==4:
        print("     ##################")
        print("     # Forme initiale #")
        print("     ##################")
        print()
        print()
        print("############################")
        print("# 1 = Par forme canonique  #")
        print("# 2 = Par forme factorisée #")
        print("############################")
        print()
        print()
        choise=int(input("Entrez le chiffre qui correspond a la forme de fonction : "))
        if choise==1:
            a=float(input("Entrez la valeur de a : "))
            if a==0:
                print("a ne peut être égale à 0")
                input("Appuyez sur Entrée, le programme va s'arrêter...")
                exit()    
            
            alpha=float(input("Entrez la valeur d'alpha : "))
            beta=float(input("Entrez la valeur de beta : "))
            b=2*alpha
            c=alpha**2+beta
            if b>=0 and c>=0:
                print(a,"x² +",b,"x +",c )
                rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                if rep2=="oui":
                    exit()
                elif rep2=="non":
                    print("Alors continuons !")
            if b<0 and c<0:
                print(a,"x² -",abs(b),"x -",abs(c) )
                rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                if rep2=="oui":
                    exit()
                elif rep2=="non":
                    print("Alors continuons !")
            if b>=0 and c<0:
                print(a,"x² +",b,"x -",abs(c) )
                rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                if rep2=="oui":
                    exit()
                elif rep2=="non":
                    print("Alors continuons !")
            if b<0 and c>=0:
                print(a,"x² -",abs(b),"x +",c )
                rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                if rep2=="oui":
                    exit()
                elif rep2=="non":
                    print("Alors continuons !")
        elif choise==2:
            rep3=int(input("Combien de racine possède la fonction en question ? (1/2) : "))
            if rep3==1:
                a=float(input("Entrez la valeur de a : "))
                if a==0:
                    print("a ne peut être égale à 0")
                    input("Appuyez sur Entrée, le programme va s'arrêter...")
                    exit()
                
                x0=float(input("Entrez une valeur numérique de x0 : "))

                b=a*(2*x0)
                c=a*(x0**2)

                b=round(b,2)
                c=round(c,2)

                if b>=0 and c>=0:
                    print(a,"x² +",b,"x +",c)
                if b<0 and c<0:
                    print(a,"x² -",abs(b),"x -",abs(c))
                if b>=0 and c<0:
                    print(a,"x² +",b,"x -",abs(c))
                if b<0 and c>=0:
                    print(a,"x² -",abs(b),"x +",c)
                rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                if rep2=="oui":
                    exit()
                elif rep2=="non":
                    print("Alors continuons !")
            
            elif rep3==2:
                a=float(input("Entrez la valeur de a : "))
                if a==0:
                    print("a ne peut être égale à 0")
                    input("Appuyez sur Entrée, le programme va s'arrêter...")
                    exit()
                
                x1=float(input("Entrez une valeur numérique de x1 : "))
                x2=float(input("Entrez une valeur numérique de x2 : "))
                if x1>0 and x2<0:
                    b=abs(x2)-x1
                    print(b)
                if x1<0 and x2<0:
                    b=abs(x2)+abs(x1)
                    print(b)
                if x1<0 and x2>0:
                    b=x2+abs(x1)
                    print(b)
                c=x1*x2
                c=a*c

                b=a*b
                print(b)
                
                b=round(b,2)
                c=round(c,2)
                if b>=0 and c>=0:
                    print(a,"x² +",b,"x +",c)
                if b<0 and c<0:
                    print(a,"x² -",abs(b),"x -",abs(c))
                if b>=0 and c<0:
                    print(a,"x² +",b,"x -",abs(c))
                if b<0 and c>=0:
                    print(a,"x² -",abs(b),"x +",c)
                rep2=input("Est ce que vous voulez arrêtez le programme ? (oui/non) : ")
                if rep2=="oui":
                    exit()
                elif rep2=="non":
                    print("Alors continuons !")
            
