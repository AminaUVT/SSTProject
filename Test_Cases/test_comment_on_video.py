from playwright.sync_api import sync_playwright


def test_comment_on_video():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Assuming the user is already logged in
        # Submit a comment
        comment_box_selector = "textarea[aria-label='Comments']"
        page.click(comment_box_selector)
        page.fill(comment_box_selector, "This is a test comment.")
        submit_button_selector = "button[aria-label='Comment']"  
        page.click(submit_button_selector)

        page.is_visible("text=This is a test comment")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_comment_on_video()
