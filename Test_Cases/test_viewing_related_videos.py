from playwright.sync_api import sync_playwright


def test_viewing_related_videos():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the specified YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Scroll to the related videos section
        related_videos_selector = "ytd-watch-next-secondary-results-renderer ytd-compact-video-renderer"
        page.wait_for_selector(related_videos_selector)
        page.hover(related_videos_selector)

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_viewing_related_videos()
