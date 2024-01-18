from playwright.sync_api import sync_playwright


def test_search_empty_string():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to YouTube
        page.goto("https://www.youtube.com/")

        # Enter an empty search query and perform the search
        page.fill("input[name='search_query']", "")
        page.press("input[name='search_query']", "Enter")

        # Wait and check for the prompt to enter search keywords
        prompt_visible = page.is_visible(
            "text=Please enter a search term")

        assert prompt_visible, "The prompt to enter search keywords is not visible."

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_search_empty_string()
