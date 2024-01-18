from playwright.sync_api import sync_playwright


def test_search_for_channel():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the YouTube homepage
        page.goto("https://www.youtube.com")

        # Enter a channel name in the search bar and perform the search
        channel_name = "liana flores"
        page.fill("input[name='search_query']", channel_name)
        page.press("input[name='search_query']", "Enter")

        # Wait for the search results to load and verify the channel is in the results
        page.wait_for_selector("ytd-channel-renderer", state="visible")
        is_channel_visible = page.is_visible(f"text={channel_name}")
        assert is_channel_visible, "Channel is not visible in search results"

        # Closing the browser
        browser.close()


if __name__ == "__main__":
    test_search_for_channel()
