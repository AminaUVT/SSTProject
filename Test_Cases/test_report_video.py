from playwright.sync_api import sync_playwright


def test_report_video():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a specific YouTube video
        page.goto("https://www.youtube.com/watch?v=5e1zT7miep8")

        # Click the report button
        report_button_selector = "button[aria-label='Report']"
        page.click(report_button_selector)

        # Verify that the report options are displayed
        report_options_selector = "Report"
        page.is_visible(report_options_selector)

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_report_video()
