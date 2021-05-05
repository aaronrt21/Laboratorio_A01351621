#Se importa librería numpy con alias np
import numpy as np              
#Se importa pyplot de la librería matplotlib con alias plt
import matplotlib.pyplot as plt 

#Función que saca la suma de multiplicación entre las matrices fragment y kernel
#Fragment es una matriz sacada de la matriz original image
def conv_aux(fragment, kernel):
  #Saca los límites en x y y basándose en las dimensiones de la matriz fragment
  f_row, f_col = fragment.shape
  #Declara la variable result que estará pasando el valor de cada sumatoria
  result = 0.0
  for row in range(f_row):
    for col in range(f_col):
      #Result es igual a la sumatoria de la multiplicación de las
      #matrices fragment y kernel
      result = result + (fragment[row,col] *  kernel[row,col])
  return result

#Función que realiza toda la convolución con ayuda de conv_aux y regresa la matriz
#resultado
def convolution(image, kernel):

    #Saca los límites en x y y basándose en las dimensiones de las matrices image y kernel
    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape

    #Se crea una matriz (con las dimensiones de image) donde se almacenará el resultado y se llena con ceros 
    output = np.zeros(image.shape)
    #Cada índice de la matriz output va a ser igual a la suma de la multiplicación de
    #un pedazo o *fragmento* de image por la matriz filtro (kernel) 
    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = conv_aux(
                                    image[row:row + kernel_row, 
                                    col:col + kernel_col],kernel)

    #Se crea una gráfica con la matriz output         
    plt.imshow(output, cmap='hot')
    #Se asigna un título a la gráfica
    plt.title("Output Image using {}X{} Kernel".format(kernel_row, kernel_col))
    #Se muestra la gráfica
    plt.show()
 
    return output

#Se declaran las matrices basadas en los ejemplos de clase
orig_mat = np.array([[1, 2, 3,4,5, 6], [7, 8, 9,10,11, 12], [0,0,1,16,17,18], [0, 1, 0, 7, 23, 24], [1, 7, 6, 5, 4, 3]])
filter_mat = np.array([[1,1,1],[0,0,0],[2,10,3]])

#Se ejecuta la función convolución con las matrices declaradas anteriormente
convolution(orig_mat,filter_mat)