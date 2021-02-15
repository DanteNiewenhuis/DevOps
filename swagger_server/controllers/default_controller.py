import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server.service import student_service
from swagger_server import util


def add_student(body):  # noqa: E501
    """Add a new student

     # noqa: E501

    :param body: Student object that needs to be added
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
    
    if not body.first_name:
        return "no first name", 405

    if not body.last_name:
        return "no last name", 405

    sid = student_service.add_student(body)
    if type(sid) == int:
        return sid 
    else:
        return 'already exists', 409

def delete_student(student_id):  # noqa: E501
    """delete_student

     # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int

    :rtype: Student
    """
    res = student_service.delete_student(student_id)

    if res:
        return res

    return "not found", 404 


def get_student_by_id(student_id, subject=None):  # noqa: E501
    """Find student by ID

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int
    :param subject: The subject name
    :type subject: str

    :rtype: Student
    """

    res  = student_service.get_student_by_id(student_id, subject)

    if res:
        return res

    return "not found", 404 

def get_student_by_last_name(last_name, subject=None):  # noqa: E501
    """Find student by last name

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int
    :param subject: The subject name
    :type subject: str

    :rtype: Student
    """

    res  = student_service.get_student_by_last_name(last_name, subject)

    if res:
        return res

    return "not found", 404 