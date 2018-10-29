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

    return decorate


@register(is_active=True)
def subject_1():
    pass


@register(is_active=False)
def subject_2():
    pass


@register(is_active=True)
def subject_3():
    pass
