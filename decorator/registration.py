registered = set()


def register(is_active=True):
    """
    Registrates/unregistrates subjects.

    Depends on is_active param add/remove from registered subjects.
    :param is_active: Flag of subject

    :return: decorate function object
    """

    def decorate(func):
        pass


def subject_1():
    """Do nothing."""


def subject_2():
    """Do nothing."""


def subject_3():
    """Do nothing."""
