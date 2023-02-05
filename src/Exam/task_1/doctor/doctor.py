from typing import Dict
from datetime import datetime, timedelta

from Exam.task_1.patient.patient import Patient


class Doctor:
 
    def __init__(self, name: str,
                 surname: str,
                 scedule: Dict = {}):
        """

        :type scedule: Dict[datetime: Patient]

        """
        self.__name = name
        self.__surname = surname
        self.__scedule = scedule


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value: str):
        self.__surname = value

    @property
    def scedule(self) -> Dict:
        return self.__scedule
    
    @scedule.setter
    def scedule(self, key: datetime, value: Patient) :
        self.__scedule[key] = value

    def schedule_str(self):
        return "".join(["\n{}: {}".format(k, self.scedule[k]) for k in self.scedule.keys()])

    def __repr__(self) -> str:
        return "Doctor {} {} \nschedule\n{}"\
            .format(self.name, self.surname, self.schedule_str())

    def register_patient(self, patient: Patient, dt: datetime):
        if self.is_free(dt) and self.is_registreted(patient) == False:
            self.scedule[dt] = patient

    def is_free(self, dt: datetime):
        keys = [i for i in self.scedule.keys()]
        if 10 <= dt.hour < 13 or 14 <= dt.hour <= 18:
            if len(keys) == 0:
                return True
            jam_ka = False
            for i in range(len(keys)):
                if dt > keys[i]:
                    kl = dt - keys[i]
                elif dt < keys[i]:
                    kl = keys[i] - dt
                if kl >= timedelta(minutes=30):
                    jam_ka = True
                else:
                    jam_ka = False
            return jam_ka
        else:
            return False

    def is_registreted(self, patient):
        for k in self.scedule:
            if patient == self.scedule[k]:
                return True
        return False


def test():
    pat1 = Patient("ani", 'sd', False, 58)
    pat2 = Patient("seda", 'sd', False, 48)
    pat3 = Patient("Ashot", 'sd', True, 30)
    dt1 = datetime.now()
    dt3 = dt1 + timedelta(minutes=38)
    dt2 = dt1 + timedelta(hours=1)
    doctor = Doctor("Armen", "Shargsyan")
    doctor.register_patient(pat1, dt1)

    doctor.register_patient(pat2, dt2)
    print(doctor)
    doctor.register_patient(pat3, dt3)
    print(doctor)