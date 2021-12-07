import datetime
from typing import List

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from ping3 import ping


class DBConnect:
    def __init__(self, db_url, license_table=None):
        """prepare and automap db"""

        Base = automap_base()
        self._engine = create_engine(
            db_url,
            connect_args={"options": "-c timezone=utc"}
        )
        Base.prepare(self._engine, reflect=True)

        self.Car = Base.classes.car
        self.license_table = license_table
        self.Record = Base.classes.record
        self.RecordRequest = Base.classes.request
        self.GPS = Base.classes.gps

    def __enter__(self):
        self.session = Session(self._engine)
        self.car = self.session.query(self.Car).filter_by(license_table=self.license_table).first()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def get_cars(self):
        return self.session.query(self.Car).all()

    def update_cars_statuses(self):
        cars = self.get_cars()
        for car in cars:
            if car.ip_address:
                car_status = bool(ping(car.ip_address))
                car.online = car_status
                if car_status:
                    car.last_seen = datetime.datetime.now()
        self.session.commit()

    def delete_records(self, filenames: List[str]):
        """ Удалить запись из бд """
        self.session.query(self.Record).filter(self.Record.file_name.in_(filenames),
                                               self.Record.car == self.car).delete()
        self.session.commit()
