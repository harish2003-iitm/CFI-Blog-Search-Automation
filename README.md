# CFI Blog Search Automation

This Python script automates the process of searching for a blog on the Codeforces IIT Madras (CFI) website, applying tag and club filters, and opening the best match. Users can provide search queries, specify tags for filtering, and set club filters to find the most relevant blog post on the CFI website.

## 1.Prerequisites

- Python 3.x
- Required Python libraries (install using `pip install requests beautifulsoup4`)

## 2.Usage

1. Clone or download the repository to your local machine.

2. Open a terminal and navigate to the script's directory.

3. Run the script using Python:

    ```shell
    python cfi_blog_search.py
    ```

4. Follow the prompts to enter the following information:
   - Blog search query: Enter the keywords to search for in the blog titles.
   - Tags to filter (comma-separated, leave empty for none): Enter any tags you want to filter the blogs by.
   - Club filter (leave empty for none): Enter the name of a club to filter blogs by club.

5. The script will search for matching blogs on the CFI website based on your input and display the best match, if found.

## 3.Example

Here is an example of running the script:

```shell
Enter the blog search query: muzero
Enter tags to filter (comma-separated, leave empty for none):
Enter the club filter (leave empty for none):
Matching blogs found:
- MuZero: The Undefeatable Player: https://cfi.iitm.ac.in/blog/muzero--the-undefeatable-player-FXLFngjSnGMa
