from playwright.sync_api import sync_playwright


def test_play_video_from_channel():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube channel page
        # Replace with an actual YouTube channel URL
        page.goto("https://www.youtube.com/channel/UC4KIXOHiOjd918SH-H5SlXQ")

        # Select a video from the channel's video list
        page.click("ytd-grid-video-renderer >> nth=0")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_play_video_from_channel()
