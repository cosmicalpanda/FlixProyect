# Factory method to jsonify series or movie.
import json
from flask import jsonify


## FACTORY METHOD 
## This way we can create any kind of entry without modifying the code of the call
##Solid 3 LSP: we can
class EntriesMaker:
    def makeJson(self, lista, typeOf):
        jsonPayload = self._get_payload(typeOf)
        return jsonPayload(lista)
    
    #Solid 2 OCP: if the desired behaviour of the return changes we can modify the return function instead of the call
    def _get_payload(self, typeOf):
        if typeOf == 'Movie':
            return self._payload_movie
        elif typeOf == 'Series':
            return self._payload_serie
        else:
            raise ValueError(typeOf)
    #Solid 1 SRP:  only takes care of movies
    def _payload_movie(self, lista):
        newMovie = Movie
        return newMovie.jsonRet(self,lista)
    #Solid 1 SRP:  only takes care of series
    def _payload_serie(self, lista):
        payload = {
            'id': "NO HAY SERIES DISPONIBLES POR EL MOMENTO"
        }
        return json.dumps(payload)

class Movie:
    def jsonRet(self, lista):
        return jsonify(lista)