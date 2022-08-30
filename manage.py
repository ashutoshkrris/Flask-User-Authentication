from flask.cli import FlaskGroup

from src import app

import unittest


cli = FlaskGroup(app)


@cli.command('test')
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


if __name__ == "__main__":
    cli()
