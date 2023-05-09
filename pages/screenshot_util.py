def take_screenshot(driver, file_name):
    driver.save_screenshot(file_name)


def pytest_exception_interact(node, report):
    if report.failed and hasattr(node.instance, "driver"):
        take_screenshot(node.instance.driver, "screenshots/screenshot_{}.png".format(report.when))
