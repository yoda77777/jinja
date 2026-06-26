import jinja2
from jinja2.exceptions import FilterArgumentError


def test_filter_argument_error_exported():
    """FilterArgumentError is part of the public jinja2 API.

    Regression for https://github.com/pallets/jinja/issues/2172
    """
    assert jinja2.FilterArgumentError is FilterArgumentError
    assert issubclass(jinja2.FilterArgumentError, jinja2.TemplateRuntimeError)
