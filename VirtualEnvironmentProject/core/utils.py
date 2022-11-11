import logging
import urllib.request

log = logging.getLogger(__name__)


def get_url(url):
    reqinfo = urllib.request.urlopen(url)
    info = reqinfo.read()
    decode_info = info.decode("utf8")
    reqinfo.close()
    log.info("Worked")
    return decode_info

