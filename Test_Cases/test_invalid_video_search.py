from playwright.sync_api import sync_playwright


def test_invalid_video_search():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to YouTube homepage
        page.goto("https://www.youtube.com")

        # Enter an invalid search query
        invalid_query = "asdfqwerzksjhsfd---;sbchebklxcv"
        page.fill("input[name='search_query']", invalid_query)
        page.press("input[name='search_query']", "Enter")

        # Verify that a no results message is displayed
        no_results_message_selector = "text=No results found"
        page.wait_for_selector(no_results_message_selector)

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_invalid_video_search()
