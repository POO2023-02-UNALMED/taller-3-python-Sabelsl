class TV:
    _canal = 1
    _volumen = 1
    _precio = 500
    _Tv_numTV = 0
    
    
    def __init__ (self,marca,estado):
        self._marca = marca
        self._estado = estado
        TV._Tv_numTV +=1 
        
    def getMarca (self):
        return self._marca
    
    def setMarca (self,marca):
        self._marca = marca
        
    def getCanal (self):
        return self._canal
    
    def setCanal (self,canal):
        if self._estado:
            if self._canal >=1 and self._canal <=120:
                self._canal = canal
        
    def getVolumen (self):
        return self._volumen
    
    def setVolumen (self,volumen):
        if self._estado:
            if self._volumen >=0 and self._volumen <=7:
                self._volumen = volumen
        
    def getPrecio (self):
        return self._precio
    
    def setPrecio (self,precio):
        self._precio = precio
        
    @staticmethod
    def getNumTV ():
        return TV._Tv_numTV
    
    @staticmethod
    def setNumTV(numTV):
        TV._Tv_numTV = numTV
        
    def getEstado (self):
        return self._estado
    
    def setControl (self,control):
        self._control = control
        
    def getControl (self):
        return self._control
    
    def turnOn (self):
        self._estado = True
        
    def turnOff (self):
        self._estado = False
        
    def canalUp (self):
        if self._estado:
            if self._canal <= 119:
                self._canal +=1
        
    def canalDown (self):
        if self._estado:
            if self._canal >= 1:
                self._canal -=1
    
    def volumenUp (self):
        if self._estado:
            if self._volumen <= 6:
                self._volumen +=1
        
    def volumenDown (self):
        if self._estado:
            if self._volumen >= 1:
                self._volumen -=1
        
