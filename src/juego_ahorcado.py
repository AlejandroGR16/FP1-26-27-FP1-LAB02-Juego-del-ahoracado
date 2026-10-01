import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena=cadena.lower()
    cadena=cadena.strip()
    cadena=cadena.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ü','u')
    return cadena

def enmascarar(palabra_secreta, letras_usadas=''):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    resultado=''
    for c in palabra_secreta:
        if c in letras_usadas:
            resultado+=c
        else: resultado+='_'
    return resultado


def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    if '_' in palabra_enmascarada:
        return False
    else:
        return True

def mostrar_estado(palabra_enmascarada,intentos_restantes,letras_usadas=''):
    print(f'Estado: {" ".join(palabra_enmascarada)}')
    if letras_usadas=='':
        print(f'Letras usadas: ninguna')
    else:
        print(f'Letras usadas: {letras_usadas}')
    print(f'Intentos restantes: {intentos_restantes}')

def pedir_letra(letras_usadas,letra=''):
    while True:
        letra=input('Introduce una letra:')
        letra=letra.lower()
        letra=letra.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ü','u')
        if (letra.isalpha()) and (len(letra)==1) and (not(letra in letras_usadas)):
            break
        else:
            if (letra.isalpha())==False:
                print('Debes introducir una letra')
            if len(letra)!=1:
                print('Debes introducir una única letra')
            if letra in letras_usadas:
                print('Esa letra ya la has usado anteriormente')
    return letra


def jugar(palabra_secreta='',letra='',palabra_enmascarada='',letras_usadas='',intentos_restantes=6):
    if palabra_secreta!='':
        print('')
        print('¡Bienvenido al juego del ahorcado!')
        print('')
        palabra_secreta=normalizar(palabra_secreta)
        palabra_enmascarada=enmascarar(palabra_secreta,letras_usadas)
        while intentos_restantes>0 and '_' in palabra_enmascarada:
            mostrar_estado(palabra_enmascarada,intentos_restantes,letras_usadas)
            letra=pedir_letra(letras_usadas,letra)
            letras_usadas+=letra
            if letra in palabra_secreta:
                print(f'✅ La letra {letra} está')
                palabra_enmascarada=enmascarar(palabra_secreta,letras_usadas)
            else:
                print(f'❌ La letra {letra} NO está')
                intentos_restantes-=1
            print('')
        if not('_' in palabra_enmascarada):
            print(f'Has ganado, la palabra es: {palabra_secreta}')
        else: print(f'Has perdido, te has quedado sin intentos. La palabra era: {palabra_secreta}')
    else: return None


jugar(elige_palabra())
