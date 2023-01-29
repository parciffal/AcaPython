class IncorectCourseException(Exception):
    def __init__(self, course) -> None:
        super().__init__("Course should be from 1 to 4 not: {}".format(course))