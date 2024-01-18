from playwright.sync_api import sync_playwright


def test_search_functionality():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)  # Set headless=False to see the browser
        page = browser.new_page()

        # Navigate to YouTube
        page.goto("https://www.youtube.com/")

        # Enter a search query and perform the search
        search_query = "Playwright Python"  # Example search query
        page.fill("input[name='search_query']", search_query)
        page.press("input[name='search_query']", "Enter")

        # Wait for search results to be displayed
        page.wait_for_selector("ytd-video-renderer")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_search_functionality()
