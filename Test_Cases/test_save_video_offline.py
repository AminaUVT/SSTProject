from playwright.sync_api import sync_playwright


def test_save_video_offline():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        save_offline_button_selector = "button[aria-label='Download']"
        page.click(save_offline_button_selector)

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_save_video_offline()
