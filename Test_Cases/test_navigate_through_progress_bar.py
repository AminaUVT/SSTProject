from playwright.sync_api import sync_playwright


def test_navigate_through_progress_bar():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the specified YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Play the video
        page.click("button[title='Play']")

        progress_bar_selector = "div.ytp-progress-bar"
        page.click(progress_bar_selector, position={"x": 100, "y": 10})

        Example: page.text_content("selector-for-video-current-time")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_navigate_through_progress_bar()
