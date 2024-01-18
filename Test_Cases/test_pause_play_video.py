from playwright.sync_api import sync_playwright


def test_pause_play_video():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Play the video
        page.click("button[title='Play']")

        # Wait for the video to start playing
        page.wait_for_selector("video selector")

        # Pause the video
        page.click("button[title='Pause']")

        # Wait for a moment to ensure the video has paused
        page.wait_for_timeout(1000)  # Waits for 1 second

        # Play the video again
        page.click("button[title='Play']")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_pause_play_video()
