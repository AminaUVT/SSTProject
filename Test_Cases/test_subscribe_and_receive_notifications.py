from playwright.sync_api import sync_playwright


def test_subscribe_and_receive_notifications():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube channel page
        page.goto("https://www.youtube.com/channel/UC4KIXOHiOjd918SH-H5SlXQ")

        # Assuming the user is already logged in
        # Click the subscribe button
        subscribe_button_selector = "button[aria-label='Subscribe']"
        page.click(subscribe_button_selector)

        # Opt to receive notifications

        notifications_button_selector = "button[aria-label='.notifications']"
        page.click(notifications_button_selector)

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_subscribe_and_receive_notifications()
