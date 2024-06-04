class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def rig(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'F':
            return 8
        raise MealyError('rig')

    def trim(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        if self.state == 'B':
            self.state = 'D'
            return 3
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 6
        if self.state == 'F':
            self.state = 'A'
            return 7
        raise MealyError('trim')


def main():
    return StateMachine()


def raises(function, error):
    output = None
    try:
        output = function()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.rig() == 0
    assert o.rig() == 2
    assert o.trim() == 4
    assert o.trim() == 5
    assert o.trim() == 6
    assert o.rig() == 8
    assert o.trim() == 7
    assert o.rig() == 0
    assert o.trim() == 3
    o = main()
    assert o.trim() == 1
    # assert o.put() == 2
    # assert o.put() == 3
    # assert o.put() == 5
    # assert o.put() == 6
    # assert o.share() == 8
    o = main()
    assert o.trim() == 1
    raises(lambda: o.rig(), MealyError)
    o.state = 'K'
    raises(lambda: o.trim(), MealyError)
