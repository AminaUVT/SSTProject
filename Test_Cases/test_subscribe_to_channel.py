from playwright.sync_api import sync_playwright


def test_subscribe_to_channel():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the specified YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Assuming the user is already logged in
        # Click the subscribe button
        page.click("ytd-subscribe-button-renderer")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_subscribe_to_channel()
