
import threading
import serial 
import time

global incomingByte
#mutex = threading.Lock()

def create_porta():
    global portaUSB
    aux = '/dev/ttyACM0'
    try:
        portaUSB = serial.Serial(aux, 9600, timeout=1)
    except:
        print('conexao nao estabelecida')

def chave():
    global incomingByte
    #i = 0
    while(1):
        #mutex.acquire()
        incomingByte = portaUSB.read().rstrip().decode('CP1252')
        #print(incomingByte)
        #i = i + 1
        #mutex.release()

def sen_command(cod):
    aux = str(cod)
    portaUSB.write(aux.encode())

def comandoFarois():

    global incomingByte
    print('TESTE')
    #mutex.acquire()
    if(incomingByte == 'F'):
        sen_command('ligar farois')
        print('LIGA FAROIS')
    else:
        sen_command('desligar farois')
        print('DESLIGA FAROIS')
    #mutex.release()


# CRIAÇÃO DAS THREADS
Tchave = threading.Thread(target=chave)
ligafarois = threading.Thread(target=comandoFarois)

# CHAMADAS DE FUNÇÕES
create_porta()

# INICIANDO AS THREADS
Tchave.start()
ligafarois.start()

while Tchave.isAlive():
    print("Thread da chave esta funcionando")
    time.sleep(5)
