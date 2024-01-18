from playwright.sync_api import sync_playwright


def test_search_autocomplete():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to YouTube
        page.goto("https://www.youtube.com/")

        # Start typing a query in the search bar
        search_query_partial = "Playwright"  # Example partial query
        page.fill("input[name='search_query']", search_query_partial)

        # Wait and check for autocomplete suggestions
        suggestions_visible = page.is_visible(".suggestions")

        assert suggestions_visible, "Autocomplete suggestions are not visible."

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_search_autocomplete()
