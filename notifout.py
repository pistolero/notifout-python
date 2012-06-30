import urlparse
import urllib2
import logging
import simplejson

logger = logging.getLogger('notifout')

class NotifoutError(RuntimeError): pass
class InsufficientFundsError(NotifoutError): pass
class ServiceError(NotifoutError): pass


class Notifout(object):
    """Notifout.com client"""

    API_BASE = 'https://notifout.com/'

    def __init__(self, token):
        self.token = token

    def send(self, template, recipient, data=None, subject=None, sender=None):
        """Send message

        Arguments:
        template -- template slug defined in Notifout
        recipient -- message recipient. Can be specified as 'some name <email@example.org>' or as tuple ('some name', 'email@example.org')
        data -- variables
        subject -- override default message subject.
        sender -- override default message sender. Can be specified as 'some name <email@example.org>' or as tuple ('some name', 'email@example.org')
        """
        
        url = urlparse.urljoin(self.API_BASE, '/api/send')
        msg = {
            'template': template,
            'recipient': recipient,
            'data': data,
            'subject': subject,
            'sender': sender
        }
        self._request(url, self._build_send([msg]))

    def _build_send(self, messages):
        return {'token': self.token, 'messages': messages}

    def _request(self, url, data):
        req = urllib2.Request(url, simplejson.dumps(data), headers={'Content-Type': 'application/json'})

        try:
            resp = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            if e.code == 402:
                raise InsufficientFundsError(unicode(e.msg))
            resp = e
        except Exception, e:
            logger.error('Failed to read Notifout response')
            raise ServiceError('Failed to read Notifout response')

        headers = resp.headers if hasattr(resp, 'headers') else resp.hdrs
        if not headers.get('Content-Type') == 'application/json':
            logger.error('Got unknown content-type %r from Notifout', headers.get('Content-Type'))
            raise ServiceError('Got unknown content-type %r from Notifout' % headers.get('Content-Type'))

        try:
            content = resp.read()
        except Exception, e:
            logger.error('Failed to read Notifout response')
            raise ServiceError('Failed to read Notifout response')

        try:
            content = simplejson.loads(content)
        except Exception, e:
            logger.error('Failed to parse Notifout response')
            raise ServiceError('Failed to parse Notifout response')

        if content.get('status', 'error') == 'error':
            logger.error('Got error from Notifout: %s' % content.get('error'))
            raise ServiceError('Got error from Notifout: %s' % content.get('error'))

        return content
