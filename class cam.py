class Camera():
    """Il s'agit de la classe camera
    Ses atributs:
        - imgSize
        - ips
    Ses méthodes:
        - afficher 
    """
    def __init__(self,ips=25 ,imgSize=12  ):
        self.imgSize = imgSize
        self.ips = ips
        print("passage par le constructeur")
    
    def __str__(self):
       return f"({self.ips,self.imgSize})"


    def __repr__(self):
        return f"{self.ips,self.imgSize}"

    def calculer(self):
        laCamera=Camera(12,22)
        
    print(Camera.__doc__) 
uneCamera = Camera(25,"12 ko")
print(laCamera)

def calculerHDD(sefl.duree)