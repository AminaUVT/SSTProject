from playwright.sync_api import sync_playwright


def test_check_video_captions():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Turn on captions
        captions_button_selector = "button[aria-label='Captions']"
        page.click(captions_button_selector)

        # Verify that captions are displayed on the video
        captions_visible_selector = "captions"
        page.is_visible(captions_visible_selector)

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_check_video_captions()
