import os


class Image():
    """Every image object contains :
        - the path of an image
        - an unique identifier(id) for further accessing of image's attributes
        - a value (operand- ie 5,6,10, 0, etcs)
            (the last one is useful in computing the score when the player hits a baddie.
             The score can increase with a value or can be equaled to zero., depend on player's moves )
    """
    def __init__( self,path, id,  value):
        self.__value = value
        self.__id = id
        self.__path = path

    def get_value(self):
        return  self.__value

    def get_id(self):
        return  self.__id

    def get_path(self):
        return  self.__path


class ImagesRepository:
    """
        A simple class that contains all availables baddies and their attributes.
    """
    def __init__(self):
        self.allImages = []
        self.createList()

    def getImagePath(self):
        """
            Return the path of images folder.
        """
        # currentPath = os.path.join( os.path.dirname( __file__ ), '..' )
        one_folder_up = os.getcwd()
        resourcesPath = os.path.join(one_folder_up, "Resources")
        imagesPath = os.path.join(resourcesPath, "Images")
        return imagesPath

    def get_all(self):
        return  self.allImages

    def getByID(self, id ):
        allImages= self.get_all()
        if id <=len(allImages):
            return allImages[id-1]

    def createList(self):
        path = self.getImagePath()
        #goodies
        self.allImages.append(Image(os.path.join(path, "apple.png"),1,5))
        self.allImages.append(Image(os.path.join(path, "burger.png"),2,5))
        self.allImages.append(Image(os.path.join(path, "chicken.png"),3,5))
        self.allImages.append(Image(os.path.join(path, "cheese.png"),4,5))
        self.allImages.append(Image(os.path.join(path, "croissant.png"),5,5))
        self.allImages.append(Image(os.path.join(path, "grape.png"),6,5))
        self.allImages.append(Image(os.path.join(path, "melon.png"),7,5))
        self.allImages.append(Image(os.path.join(path, "orange.png"),8,5))
        self.allImages.append(Image(os.path.join(path, "pizza.png"),9,5))
        self.allImages.append(Image(os.path.join(path, "steak.png"),10,5))
        #baddies
        self.allImages.append(Image(os.path.join(path, "bacteria.png"),11,-5))
        self.allImages.append(Image(os.path.join(path, "flower.png"),12,-5))
        self.allImages.append(Image(os.path.join(path, "construction.png"),13,-5))
        self.allImages.append(Image(os.path.join(path, "wrench.png"),14,-5))
        self.allImages.append(Image(os.path.join(path, "dog.png"),15,-5))
        self.allImages.append(Image(os.path.join(path, "flower.png"),16,-5))
        self.allImages.append(Image(os.path.join(path, "guitar.png"),17,-5))
        self.allImages.append(Image(os.path.join(path, "hammer.png"),18,-5))
        self.allImages.append(Image(os.path.join(path, "music.png"),19,-5))
        self.allImages.append(Image(os.path.join(path, "pill.png"),20,-5))
        self.allImages.append(Image(os.path.join(path, "rock.png"),21,-5))
        self.allImages.append(Image(os.path.join(path, "bacteria.png"),22,-5))
        #bonus
        self.allImages.append(Image(os.path.join(path, "life.png"),23,0))






