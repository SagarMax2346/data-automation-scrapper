import csv
import os
from bs4 import BeautifulSoup


def scrape_local_quotes():
    html_filename = "sample_data.html"

    # Check if our sample file exists in the directory
    if not os.path.exists(html_filename):
        print(f"Error: Missing local file '{html_filename}' in your project directory.")
        return

    print(f"Opening local asset: '{html_filename}'...")

    # Read the raw HTML text from the local file
    with open(html_filename, mode="r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    quote_elements = soup.find_all("div", class_="quote")

    scraped_data = []
    print(f"Parsing engine active. Found {len(quote_elements)} entries...")

    for element in quote_elements:
        text = element.find("span", class_="text").text.strip()
        author = element.find("small", class_="author").text.strip()

        tag_elements = element.find_all("a", class_="tag")
        tags = [tag.text.strip() for tag in tag_elements]
        tags_string = ", ".join(tags)

        scraped_data.append([text, author, tags_string])

    # Write entries cleanly to your CSV portfolio sheet
    csv_filename = "quotes_portfolio_data.csv"
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])
        writer.writerows(scraped_data)

    print(f"\nSuccess! Automation data generated cleanly to '{csv_filename}'.")


if __name__ == "__main__":
    scrape_local_quotes()
