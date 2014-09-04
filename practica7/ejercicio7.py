
#lista=range(1,21)
#print lista
#raw_input()

#segundo ejercicio

#lista=range(20, 0,-1)
#print lista
#raw_input()


#tercer ejercicio

#    return a + b
#num1 =raw_input("Num1: ")
#num2 = raw_input("Num2: ")
#print("Opcion\n1.- Sumar")
#operacion = { '1': sumar}
#seleccion = raw_input('la operacion es : ')
#try:
 #   resultado = operaciones[seleccion](int(num1), int(num2))
  #  print resultado
#except:
 #   print("Eso no vale")
#raw_input()



#cuarto ejercicio

#def suma2(a, b):
 #   return a,b
#num1 =raw_input("Num1: ")
#num2 = raw_input("Num2: ")
#print("Opcion\n1.- Concatenar")
#operaciones = { '1': suma2,}
#seleccion = raw_input('seleccionar : ')
#try:
 #   resultado = operaciones[seleccion](int(num1), int(num2))
  #  print resultado    
#except:
 #   print("Eso no vale")
#raw_input()



#quinto ejercicio

#def suma3(a, b):
 #   return a+b
#num1 =raw_input("Num1: ")
#num2 = float (raw_input("Num: "))
#print("Opcion\n1.- sumar\n2.- salir")
#operaciones = { '1': suma3,}
#seleccion = raw_input('seleccionar : ')
#try:
#    resultado = operaciones[seleccion](int(num1), abs(num2 - int(num2)))
#    print resultado    
#except:
#    print("gracias")
#raw_input()


#ejercicio nro 2

#num =int(raw_input("Num2: "))
#for i in range(num):
#	if i%2==0:
#		print ' ' +str(i),
#raw_input()


#ejercicio nro 3
#print"inserte una palabra"
#def es_palindromo (cadena):
#    pal_invertida = inversa (cadena)
#    ind = 0
 #   cont = 0
  #  for i in range (len(cadena)):
   #     if pal_invertida[indice] == cadena[ind]:
    #        ind =ind+1
     #       cont =cont+1
      #  else:
       #     print "False"
        #    break
    	#if cont == len(cadena): 
        #	print "True"
#raw_input()


#ejercicio nro 4
#palabra1 = raw_input("Palabra 1: ")
#palabra2 = raw_input("Palabra 2: ")
#largo_pal1 = len(palabra1)                      
#largo_pal2 = len(palabra2)                      
#dif_largo = abs(largo_pal1 - largo_pal2)    
#if largo_pal1 > largo_pal2:                 
#    print "La palabra es : ", palabra1     
#elif largo_pal1 < largo_pal2:                
#    print "La palabra es: ", palabra2    
#else:                                               
#    print "La palabra es : ", palabra1+palabra2
#raw_input() 


#EJERCICIO 5
#def tabla_divicion():
#	for x in xrange(1,11):
#		for y in xrange(1,11):
#			print(str(y*x)+"/"+str(y)+"="+str(y*x/y))+"\t",
#		print("")

#tabla_divicion()
#raw_input()


#EJERCICIO 6
#def calcular_letras_numeros(frase):
#	letras=0
#	digitos=0
#	for x in frase:
#		if x.isalpha():
#			letras=letras+1
#		if x.isdigit():
#			digitos=digitos+1
#	print(str(letras)+" "+str(digitos))

#frase=raw_input("escriba una frase: ")
#calcular_letras_numeros(frase)
#raw_input()



def generar(n):
	for a in xrange(1,n+1):
		print str(a)*a
	a=n-1
	while a:
		print str(a)*a
		a=a-1
n=int(raw_input("ingrese un numero:"))
generar(n)
raw_input()
