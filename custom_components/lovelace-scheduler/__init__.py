from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration


DOMAIN = "lovelace_scheduler"

type LSConfigEntry = ConfigEntry[LSData]


@dataclass
class LSData:
    foo: str
    integration: Integration


def setup(hass: HomeAssistant, config: LSConfigEntry):
    hass.states.set("lovelace_scheduler.foo", "bar")

    # Return boolean to indicate that initialization was successful.
    return True
