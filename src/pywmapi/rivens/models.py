from enum import Enum
from typing import List, Optional

from attrs import define

from ..common import *

__all__ = [
    "RivenItem",
    "RivenAttribute",
]


@define
class RivenItem(ModelBase):
    class Group(Enum):
        primary = "primary"
        secondary = "secondary"
        melee = "melee"
        zaw = "zaw"
        sentinel = "sentinel"
        archgun = "archgun"
        kitgun = "kitgun"

    id: str
    name: str
    slug: str
    gameRef: str
    group: Group
    rivenType: WeaponType
    icon: str
    thumb: str
    disposition: float
    reqMasteryRank: int

    @classmethod
    def from_dict(cls, data: dict) -> "RivenItem":
        return cls(
            id=data["id"],
            name=data["i18n"]["en"]["name"],
            slug=data["slug"],
            gameRef=data["gameRef"],
            group=csl.Group(data["group"]),
            rivenType=data["rivenType"],
            icon=data["i18n"]["en"]["icon"],
            thumb=data["i18n"]["en"]["thumb"],
            disposition=data["disposition"],
            reqMasteryRank=data["reqMasteryRank"]
        )


@define
class RivenAttribute(ModelBase):
    class Group(Enum):
        default = "default"
        melee = "melee"
        top = "top"

    class Unit(Enum):
        percent = "percent"
        seconds = "seconds"
        # Not know what this is
        multiply = "multiply"

    id: str
    slug: str
    name: str
    gameRef: str
    group: Group
    positiveIsNegative: bool
    positiveOnly: bool
    negativeOnly: bool
    icon: str
    thumb: str
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    exclusiveTo: Optional[List[WeaponType]] = None
    unit: Optional[Unit] = None

    @classmethod
    def from_dict(cls, data: dict) -> "RivenAttribute":
        return cls(
            id=data["id"],
            slug=data["slug"],
            name=data["i18n"]["en"]["name"],
            gameRef=data["gameRef"],
            group=csl.Group(data["group"]),
            positiveIsNegative=data["positiveIsNegative"],
            positiveOnly=data["positiveOnly"],
            negativeOnly=data["negativeOnly"],
            prefix=data.get("prefix"),
            suffix=data.get("suffix"),
            exclusiveTo=data.get("exclusiveTo"),
            unit=csl.Unit(data.get("unit")),
            icon=data["i18n"]["en"]["icon"],
            thumb=data["i18n"]["en"]["thumb"],
        )
