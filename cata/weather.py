"""Module that controls the weather storing and loading"""

import subprocess
import logging


class Weather:
    """Information about the weather today"""

    def __init__(self, city, is_metric_units):
        self.city = city
        self.forcast = ""
        self.max_load_time = 5  # seconds
        self.units = "?m" if is_metric_units else "?u"

    def load_from_wttr(self):
        """Load the weather info from wttr.in"""
        try:
            request_url = f"wttr.in/{self.city}{self.units}&format=3"
            self.forcast = str(
                subprocess.check_output(
                    ["curl", "-s", request_url],
                    timeout=self.max_load_time,
                    encoding="utf-8",
                )
            )[:-1]
            self.forcast = self.forcast.split(":")[1]
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, IndexError):
            logging.warning("Weather failed to load.")
            self.forcast = ""
