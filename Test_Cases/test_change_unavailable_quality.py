from playwright.sync_api import sync_playwright


def test_change_unavailable_quality():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the specified YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Open playback settings
        page.click("button[aria-label='Settings']")
        page.click("text=Quality")

        page.click("text=Non-Existing Quality Option")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_change_unavailable_quality()
