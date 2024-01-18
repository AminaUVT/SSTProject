from playwright.sync_api import sync_playwright


def test_share_video():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the specified YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Click the share button
        share_button_selector = "button[aria-label='.share']"
        page.click(share_button_selector)

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_share_video()
