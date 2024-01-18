from playwright.sync_api import sync_playwright


def test_like_video():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Assuming the user is already logged in
        # Click the like button
        page.click("button[aria-label='Like this video']")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_like_video()
