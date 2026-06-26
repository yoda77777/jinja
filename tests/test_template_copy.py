import copy

from jinja2 import Template


def test_template_deepcopy():
    """deepcopy(Template(...)) must not raise.

    Regression for https://github.com/pallets/jinja/issues/758
    """
    t = Template("Hello {{ name }}")
    t2 = copy.deepcopy(t)
    assert t2 is t
    assert t2.render(name="world") == "Hello world"

    t3 = copy.copy(t)
    assert t3 is t
