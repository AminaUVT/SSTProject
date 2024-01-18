from playwright.sync_api import sync_playwright


def test_mute_unmute_video():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Mute the video
        mute_button_selector = "button[aria-label='Mute (m)']"
        page.click(mute_button_selector)

        # Unmute the video
        unmute_button_selector = "button[aria-label='Unmute (m)']"
        page.click(unmute_button_selector)

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_mute_unmute_video()
