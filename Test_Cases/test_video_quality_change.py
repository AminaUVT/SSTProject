from playwright.sync_api import sync_playwright


def test_video_quality_change():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=example_video_id")
        # Play the video
        page.click("button[title='Play']")
        # Wait for the video to start playing
        page.wait_for_selector("video selector")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_video_quality_change()
