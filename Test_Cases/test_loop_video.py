from playwright.sync_api import sync_playwright


def test_loop_video():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Enable the loop feature
        # Looping a video on YouTube typically involves right-clicking on the video and selecting 'Loop'
        page.click("video", button="right")
        page.click("text=Loop")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_loop_video()
