from playwright.sync_api import sync_playwright


def test_like_video_without_login():
    with sync_playwright() as p:
        # Launch the browser in incognito mode to ensure no user is logged in
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Attempt to click the like button
        like_button_selector = "button[aria-label='Like']"
        page.click(like_button_selector)

        page.is_visible("Sign in")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_like_video_without_login()
