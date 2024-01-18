from playwright.sync_api import sync_playwright

def test_add_to_watch_later():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the specified YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Assuming the user is already logged in
        # Click the 'Add to Watch Later' button
        watch_later_button_selector = "button[aria-label='Add to Watch Later']"
        page.click(watch_later_button_selector)

        # Closing the browser
        browser.close()

if __name__ == "__main__":
    test_add_to_watch_later()
