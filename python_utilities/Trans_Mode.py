import json as Json
class Trans_Mode:
    def __init__(self):
        self.mode = self.__class__

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value


class Latlng:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return "{:3.2f}, {:3.2f}".format(self.lat, self.lng)


class Walk(Trans_Mode):
    def __init__(self, data: dict):
        super().__init__()
        self.start_time = 1
        self.end_time = 2
        self.distance = data['distance']['value']
        start = data['start_location']
        self.start_point = Latlng(start['lat'], start['lng'])
        end = data['end_location']
        self.end_point = Latlng(end['lat'], start['lng'])
        self.json = {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "time": self.end_time - self.start_time,
            "distance": self.distance,
            "start_point": {
                "lat": self.start_point.lat,
                "lng": self.start_point.lng
            },
            "end_point": {
                "lat": self.end_point.lat,
                "lng": self.end_point.lng
            }

        }

    def __str__(self) -> str:
        return str(self.json)

class Transit(Trans_Mode):
    def __init__(self, data: dict):
        super().__init__()
        self.start_time = 1
        self.end_time = 2
        self.distance = data['distance']['value']
        start = data['start_location']
        self.start_point = Latlng(start['lat'], start['lng'])
        end = data['end_location']
        self.end_point = Latlng(end['lat'], start['lng'])
        self.json = {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "time": self.end_time - self.start_time,
            "distance": self.distance,
            "start_point": {
                "lat": self.start_point.lat,
                "lng": self.start_point.lng
            },
            "end_point": {
                "lat": self.end_point.lat,
                "lng": self.end_point.lng
            }

        }

    def __str__(self) -> str:
        return str(self.json)
class Drive(Trans_Mode):
    def __init__(self, data: dict):
        super().__init__()
        self.start_time = 1
        self.end_time = 2
        self.distance = data['distance']['value']
        self.start_address = data['start_address']
        self.end_address = data['end_address']
        start = data['start_location']
        self.start_point = Latlng(start['lat'], start['lng'])
        end = data['end_location']
        self.end_point = Latlng(end['lat'], start['lng'])

        self.json = {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "time": self.end_time - self.start_time,
            "distance": self.distance,
            "start_address":self.start_address,
            "start_point": {
                "lat": self.start_point.lat,
                "lng": self.start_point.lng
            },
            "end_address":self.end_address,
            "end_point": {
                "lat": self.end_point.lat,
                "lng": self.end_point.lng
            }

        }

    def __str__(self) -> str:
        return str(self.json)

if __name__ == '__main__':
    pass
