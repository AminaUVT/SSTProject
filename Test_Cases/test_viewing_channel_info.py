from playwright.sync_api import sync_playwright


def test_viewing_channel_info():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video from a channel
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Click on the channel name to go to the channel page
        page.click("yt-simple-endpoint style-scope yt-formatted-string")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_viewing_channel_info()
