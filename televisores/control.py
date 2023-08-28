class Control:
    
    def enlazar (self,televisor):
        
        self._tv = televisor
        self._tv.setControl(self)
        
    def getTv (self):
        return self._tv
    
    def setTv (self,tv):
        self._tv = tv
    
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()
    def volumenUp(self):
        self._tv.volumenUp()
    def volumeDown(self):
        self._tv.volumeDown()
    def setCanal(self,canal):
        self._tv.setCanal(canal)
    def setVolumen(self,volumen):
        self._tv.setVolume(volumen)