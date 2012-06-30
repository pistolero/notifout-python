import mock
from nose.tools import eq_, ok_, raises
from notifout import Notifout, InsufficientFundsError
import urllib2

@mock.patch('urllib2.Request')
@mock.patch('urllib2.urlopen')
def test_normal_send(urlopen, Request):
    resp = mock.Mock()
    resp.headers={'Content-Type': 'application/json'}
    resp.read.return_value = '{"status": "accepted"}'
    urlopen.return_value = resp

    n = Notifout('123')
    n.send('tpl1', 'serg@shopium.ua')

    Request.assert_called_once_with('https://notifout.com/api/send', 
                                    '{"token": "123", "messages": [{"data": null, "recipient": "serg@shopium.ua", "sender": null, "template": "tpl1", "subject": null}]}', 
                                    headers={'Content-Type': 'application/json'})
    ok_(urlopen.called)


@raises(InsufficientFundsError)
@mock.patch('urllib2.Request')
@mock.patch('urllib2.urlopen')
def test_insufficient_funds(urlopen, Request):
    resp = mock.Mock()
    resp.read.return_value = '{"status": "error", "error": "insufficient funds"}'
    urlopen.side_effect = urllib2.HTTPError('', 402, 'payment required', {'Content-Type': 'application/json'}, resp)

    n = Notifout('123')
    n.send('tpl1', 'serg@shopium.ua')

    Request.assert_called_once_with('https://notifout.com/api/send', 
                                    '{"token": "123", "messages": [{"data": null, "recipient": "serg@shopium.ua", "sender": null, "template": "tpl1", "subject": null}]}', 
                                    headers={'Content-Type': 'application/json'})
    ok_(urlopen.called)    