# DIAGRAMA DE FLUJO HECHO A MANO DEL SISTEMA DE L AMAQUINA DE SNACK
![diagrama de flujo](diagrama_flujo.jpeg)
estees eldiagrama de flujo hecho en clases parapoder mostrar como se ejecutara en vs code mediante python y github ademas que el codigo es mas sencillo para que todos ouedan entenderlo mejor
# MAQUINA EXPENDEDORA DE SNACK 
## EXPLICACION DE COMO ES LA MAQUINA EXPENDEDORA 
la simulacion de la maquina expendedora es como una de la vida real 
### inicio
la maquina inicia con elmonto fijo de 5 bs 
### menu 
el menu les muestra en la pantalla su dinero disponible en tiempo real y el menu de productos con sus precios  
### papas :BS.1.5
### chocolates :BS.2.00
### refrescos :BS.2.50
### toma la desicion 
el usuario preciona una tecla que no existe en el menu la maquina le avisa que la opcion es invalida y le vuelve a pedir que elija correctamente 
### rechazo 
si le alcanza resta el precio del snack del dinero disponible 
si no le alcanza bloquea la transaccion le avisa que no tiene saldo suficiente y lo vuelve al menu 
### salida 
todo se repíte indefinidamente hasta que el usuario precione la oopcion "0" (salir)