import datetime
from pages.screenshot_util import take_screenshot


def pytest_exception_interact(node, report):
    if report.failed and hasattr(node.instance, "driver"):
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        take_screenshot(node.instance.driver, "screenshot_{}_{}.png".format(report.when, now))
