from tabulate import tabulate
from dataclasses import dataclass

@dataclass
class Plan:
    can_stream: bool
    can_download: bool
    has_sd: bool
    has_hd: bool
    has_uhd: bool
    num_devices: int
    contents: str
    price: int
    plan_name: str
    level: int

    def check_plan(self):
        data = [
            ['Service', self.plan_name],
            ['Can stream',  u'\u2713' if self.can_stream else "-"],
            ['Can download', u'\u2713' if self.can_download else "-"],
            ['has_sd', u'\u2713' if self.has_sd else "-"],
            ['has_hd', u'\u2713' if self.has_hd else "-"],
            ['has_uhd', u'\u2713' if self.has_uhd else "-"],
            ['num_devices', self.num_devices],
            ['Price', f"Rp{self.price:,}"],
        ]

        print(tabulate(data, headers='firstrow'))


basic_plan = Plan(
    can_stream=True,
    can_download=True,
    has_sd=True,
    has_hd=False,
    has_uhd=False,
    num_devices=1,
    contents="3rd party Movie only",
    price=120_000,
    plan_name="Basic Plan",
    level=1
)

standard_plan = Plan(
    can_stream=True,
    can_download=True,
    has_sd=True,
    has_hd=True,
    has_uhd=False,
    num_devices=2,
    contents="Basic Plan + Sports",
    price=160_000,
    plan_name="Standard Plan",
    level=2
)

premium_plan = Plan(
    can_stream=True,
    can_download=True,
    has_sd=True,
    has_hd=True,
    has_uhd=True,
    num_devices=4,
    contents="Standard Plan + PacFlix Oringinals",
    price=200_000,
    plan_name="Premium Plan",
    level=3
)