class calculadora:
    #determino los numeros que se usaran en las operaciones
    def __init__(self,n1,n2):
        
        self.suma=n1+n2
        self.resta=n1-n2
        self.multiplicacion=n1*n2
        self.division=n1/n2
operacion=calculadora(6,2)
print('El resultado es:',operacion.resta)