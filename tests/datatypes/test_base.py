
from mock import Mock

from chapter10.datatypes import base


def test_lazy():
    body = base.Base(Mock(data_type=0, data_length=5,
                          file=Mock(tell=Mock(return_value=5))))
    assert body.__dict__.get('data') is None


def test_load(monkeypatch):
    monkeypatch.setattr(base.Base, 'parse', Mock())
    body = base.Base(Mock(data_type=0, data_length=5,
                          file=Mock(tell=Mock(return_value=5))))
    getattr(body, 'data', None)
    assert base.Base.parse.called
