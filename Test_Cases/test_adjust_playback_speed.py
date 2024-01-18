from playwright.sync_api import sync_playwright


def test_adjust_playback_speed():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the specified YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Play the video
        page.click("button[title='Play']")

        # Open playback settings
        page.click("button[aria-label='Settings']")
        page.click("text=Playback speed")

        # Select a playback speed
        # Example: Choose 1.5x speed
        page.click("text=1.5")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_adjust_playback_speed()
