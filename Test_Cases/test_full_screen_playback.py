from playwright.sync_api import sync_playwright


def test_full_screen_playback():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the specified YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Play the video
        page.click("button[title='Play']")

        # Click the full-screen button
        page.click("button[title='Full screen']")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_full_screen_playback()
