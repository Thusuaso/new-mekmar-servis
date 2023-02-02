
from views.galleria import Galery
from flask_restful import Resource
 
class GalleriaPhotosApi(Resource):
    def get(self):
        galery = Galery()
        result = galery.getGaleryPhotosList()
        return result