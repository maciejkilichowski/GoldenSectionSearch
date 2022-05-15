
#importowanie potrzebnych bibliotek
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
 
#funkcja Sinusa
def func_fx(x):
    fx=np.sin(x)
    return fx
#aktualizacja x1 i x2 w oparciu o wartości graniczne
def check_pos(x1,x2):
    if x2<x1:
        label='right'
    else:
        label=''
    return label
def update_interior(xl,xu):
    d=((np.sqrt(5)-1)/2)*(xu-xl)
    x1=xl+d
    x2=xu-d
    return x1,x2
#Wybór optymalnego punktu do wyznaczenia nowej wartości granicznej xl,xu oraz x1,x2
#Szukanie maksimum funkcji
def find_max(xl,xu,x1,x2,label):
    fx1=func_fx(x1)
    fx2=func_fx(x2)
    if fx2>fx1 and label=='right':
        xl=xl
        xu=x1
        new_x=update_interior(xl,xu)
        x1=new_x[0]
        x2=new_x[1]
        xopt=x2
    else:
        xl=x2
        xu=xu
        new_x=update_interior(xl,xu)
        x1=new_x[0]
        x2=new_x[1]
        xopt=x1
    return xl,xu,xopt
#Szukanie minimum funkcji
def find_min(xl,xu,x1,x2,label):
    fx1=func_fx(x1)
    fx2=func_fx(x2)
    if fx2>fx1 and label=='right':
        xl=x2
        xu=xu
        new_x=update_interior(xl,xu)
        x1=new_x[0]
        x2=new_x[1]
        xopt=x1
    else:
        xl=xl
        xu=x1
        new_x=update_interior(xl,xu)
        x1=new_x[0]
        x2=new_x[1]
        xopt=x2
    return xl,xu,xopt
#Wyświetlanie wykresu oraz pozycji testowych
def plot_graph(xl,xu,x1,x2):
    clear_output(wait=True)
   
    #Wyświetlenie wykresu sinusa
    plt.plot(x,y)
    plt.plot([0,6],[0,0],'k')
   
    #Wyświetlenie punktu x1
    plt.plot(x1,func_fx(x1),'ro',label='x1')
    plt.plot([x1,x1],[0,func_fx(x1)],'k')
   
    #Wyświetlenie punktu x2
    plt.plot(x2,func_fx(x2),'bo',label='x2')
    plt.plot([x2,x2],[0,func_fx(x2)],'k')
   
    #Wyświetlenie linii xl
    plt.plot([xl,xl],[0,func_fx(xl)])
    plt.annotate('xl',xy=(xl-0.01,-0.2))
       
    #Wyświetlenie liniii xu
    plt.plot([xu,xu],[0,func_fx(xu)])
    plt.annotate('xu',xy=(xu-0.01,-0.2))
       
    #Wyświetlenie linii x1
    plt.plot([x1,x1],[0,func_fx(x1)],'k')
    plt.annotate('x1',xy=(x1-0.01,-0.2))
       
    #wyświetlenie linii x2
    plt.plot([x2,x2],[0,func_fx(x2)],'k')
    plt.annotate('x2',xy=(x2-0.01,-0.2))
   
    #Określenie zakresy Y
    plt.ylim([-1.2,1.2])
    plt.show()
def golden_search(xl,xu,mode,et):
    it=0
    e=1
    while e>=et:
        new_x=update_interior(xl,xu)
        x1=new_x[0]
        x2=new_x[1]
        fx1=func_fx(x1)
        fx2=func_fx(x2)
        label=check_pos(x1,x2)
        clear_output(wait=True)
        plot_graph(xl,xu,x1,x2) #Wyświetlenie wykresu
        plt.show()
       
        #Wybór granic, w których działać będzie metoda
        if mode=='max':
            new_boundary=find_max(xl,xu,x1,x2,label)
        elif mode=='min':
            new_boundary=find_min(xl,xu,x1,x2,label)
        else:
            print('Należy zdefiniować tryb działania programu: min/max')
            break #Przerwanie działania programu jeżeli nie zostanie zdefiniowany tryb
        xl=new_boundary[0]
        xu=new_boundary[1]
        xopt=new_boundary[2]
       
        it+=1
        print ('Iteration: ',it)
        r=(np.sqrt(5)-1)/2 #złota proporcja
        e=((1-r)*(abs((xu-xl)/xopt)))*100 #błąd progowy
        print('Error:',e)
        time.sleep(1)
#Generowanie sinusa  
x=np.linspace(0,6,100)
y=func_fx(x)
 
#Wywołanie funkcji golden_search
golden_search(0,6,'min',0.05)
