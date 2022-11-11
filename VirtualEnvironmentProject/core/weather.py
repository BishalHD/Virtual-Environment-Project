import logging
from VirtualEnvironmentProject.core.utils import get_url

log = logging.getLogger(__name__)

class weather:
    list_of_choises["Relative Humidity", "Dewpoint", "Apparent Temperature", "Showers"]
    def __init__(self):
        log.info("LOADED WEATHER")
        self.url = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, longitude:float, latitude:float, rain: bool):
        new_url = f"{self.url}?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        if rain == True:
            new_url = new_url + ",rain"
            log.info("Requested Rain")
        log.info(new_url)
        data = get_url(new_url)
        log.info(data)
        return data

    def choises(self, options):
        


