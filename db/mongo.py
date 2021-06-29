from dataclasses import dataclass

from pymongo import MongoClient


@dataclass
class MongoDatabase:
    _db = None

    @property
    def db(self):
        if not self._db:
            client = MongoClient('localhost', 27017)
            self._db = client['carshop']
        return self._db

    def get_car_by_model(self, model):
        cars = list(self.db.cars.find({'model': model}))
        for c in cars:
            del c['_id']
        return cars
