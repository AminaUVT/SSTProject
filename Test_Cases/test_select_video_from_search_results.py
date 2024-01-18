from playwright.sync_api import sync_playwright


def test_select_video_from_search_results():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to YouTube
        page.goto("https://www.youtube.com")

        # Perform a search
        search_query = "example search query"
        page.fill("input[name='search_query']", search_query)
        page.press("input[name='search_query']", "Enter")

        # Wait for the search results to load and select a video from the results
        page.wait_for_selector("ytd-video-renderer", state="visible")
        page.click("ytd-video-renderer >> nth=0")

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_select_video_from_search_results()
