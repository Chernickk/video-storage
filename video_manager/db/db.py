from typing import List

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


class DBConnect:
    def __init__(self, db_url, license_table):
        """prepare and automap db"""

        Base = automap_base()
        self._engine = create_engine(
            db_url,
            connect_args={"options": "-c timezone=utc"}
        )
        Base.prepare(self._engine, reflect=True)

        self._Car = Base.classes.car
        self.license_table = license_table
        self.Record = Base.classes.record
        self.RecordRequest = Base.classes.request
        self.GPS = Base.classes.gps

    def __enter__(self):
        self.session = Session(self._engine)
        self.car = self.session.query(self._Car).filter_by(license_table=self.license_table).first()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def delete_records(self, filenames: List[str]):
        """ Удалить запись из бд """
        self.session.query(self.Record).filter(self.Record.file_name.in_(filenames),
                                               self.Record.car == self.car).delete()
        self.session.commit()
