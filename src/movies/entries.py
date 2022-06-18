# Factory method to jsonify series or movie.
import json
from flask import jsonify



class EntriesMaker:
    def makeJson(self, lista, typeOf):
        jsonPayload = self._get_payload(typeOf)
        return jsonPayload(lista)
    
    def _get_payload(self, typeOf):
        if typeOf == 'Movie':
            return self._payload_movie
        elif typeOf == 'Series':
            return self._payload_serie
        else:
            raise ValueError(typeOf)

    def _payload_movie(self, lista):
        return jsonify(lista)

    def _payload_serie(self, lista):
        payload = {
            'id': "NO HAY SERIES DISPONIBLES POR EL MOMENTO"
        }
        return json.dumps(payload)