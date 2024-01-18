from playwright.sync_api import sync_playwright


def test_check_video_description():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        description_button_selector = "button[aria-label='Show more']"
        if page.is_visible(description_button_selector):
            page.click(description_button_selector)

        description_selector = "Description"
        is_description_visible = page.is_visible(description_selector)
        assert is_description_visible, "Video description is not visible"

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_check_video_description()
