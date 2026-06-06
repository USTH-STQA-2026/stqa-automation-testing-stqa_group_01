"""
Search & Filter Tests (*Kiểm thử Tìm kiếm & Lọc sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 4 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 4 test case trong file này.*)

Hints (*Gợi ý*):
    - After logging in, use flutter_fill() to type into the search box
      (*Sau khi đăng nhập, dùng flutter_fill() để nhập vào ô tìm kiếm*)
    - Search box aria-label: "Tìm kiếm theo tên sách hoặc tác giả..."
    - Category filter aria-label: "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
    - Each book card has role="group" and aria-label containing book info
      (*Mỗi card sách có role="group" và aria-label chứa thông tin sách*)
    - Use login() helper from conftest.py to log in before testing
      (*Dùng login() helper từ conftest.py để đăng nhập trước khi test*)
"""
import os
import time
import pytest
from conftest import enable_flutter_semantics, flutter_fill, flutter_click_button, wait_for_flutter, login, SCREENSHOT_DIR


def test_search_by_name(page, test_config):
    """TC-04: Search by book name – type "Flutter" (*Tìm sách theo tên – nhập "Flutter"*)

    🟢 Done

    Description (*Mô tả*):
        Type "Flutter" in the search box → system displays books containing "Flutter".
        (*Nhập "Flutter" vào ô tìm kiếm → hệ thống hiển thị sách có chứa "Flutter".*)

    Hints (*Gợi ý*):
        - login(page, test_config)
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")
        - Verify: page.locator('flt-semantics[aria-label*="Flutter"]').count() > 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    # pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")

    # [R] Reachability: Login and reach the book list page with search functionality
    login(page, test_config)

    # [I] Infection: Type "Flutter" in the search box — trigger the search/filter logic
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")

    # [P] Propagation: Wait for book cards containing "Flutter" to appear in the UI
    # Note: book card titles are stored in aria-label, not textContent
    wait_for_flutter(page, selector='flt-semantics[aria-label*="Flutter"]')

    # [R✓] Revealability: Test Oracle checks the search results
    assert page.locator('flt-semantics[aria-label*="Flutter"]').count() > 0, \
        "Fault: No book card with 'Flutter' in aria-label found in search results."

    #assert page.locator('flt-semantics[aria-label*="Lập trình Flutter cơ bản"]').count() > 0, \
    #    "Fault: BOOK001 'Lập trình Flutter cơ bản' not found in search results."

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Không tìm thấy sách" not in sem_text, \
        "Fault: System shows 'Không tìm thấy sách' even though BOOK001 exists in seed data."

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-04_search_by_name.png"))


def test_search_no_result(page, test_config):
    """TC-05: Search with no results (*Tìm sách – không có kết quả*)

    🟢Done 

    Description (*Mô tả*):
        Type a keyword that does not match any book → system shows an appropriate message.
        (*Nhập từ khóa không khớp bất kỳ sách nào → hệ thống hiển thị thông báo phù hợp.*)

    Hints (*Gợi ý*):
        - Verify: page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count() == 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    # pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")

    # [R] Reachability: Login and reach the book list page with search functionality
    login(page, test_config)

    # [I] Infection: Type a keyword that does not exist in seed data — trigger empty search
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Tiểu thuyết")

    # [P] Propagation: Wait for the empty-state message to appear in the UI
    wait_for_flutter(page, text="Không tìm thấy sách")

    # [R✓] Revealability: Test Oracle checks the empty-state message
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Không tìm thấy sách" in sem_text, \
        "Fault: 'Không tìm thấy sách' message not shown when search returns no results."

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-05_search_no_result.png"))


def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category 'Công nghệ' (*Lọc sách theo thể loại 'Công nghệ'*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → enter "Công nghệ" in the category filter → verify all displayed books
        belong to the "Công nghệ" category.
        (*Đăng nhập → nhập "Công nghệ" vào ô lọc thể loại → kiểm tra tất cả sách
        hiển thị đều thuộc thể loại Công nghệ.*)

    Hints (*Gợi ý*):
        - flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
        - Get book list: page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
          (*Lấy danh sách sách*)
        - Loop through each book, verify aria-label contains "Công nghệ"
          (*Lặp qua từng sách, kiểm tra aria-label chứa "Công nghệ"*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    login(page, test_config)

    # Nhập "Công nghệ" vào ô lọc thể loại
    flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
    wait_for_flutter(page, text="Công nghệ")
    enable_flutter_semantics(page)

    # Lấy danh sách sách
    books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    book_count = books.count()
    assert book_count > 0, "Phải có ít nhất 1 sách"

    # Kiểm tra từng sách đều thuộc Công nghệ
    for i in range(book_count):
        label = books.nth(i).get_attribute("aria-label") or ""
        assert "Công nghệ" in label, f"Sách không thuộc Công nghệ: {label}"

    page.screenshot(path=f"{test_config['screenshot_dir']}/TC-06-filter-category.png")


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name (*Tìm kiếm sách theo tên tác giả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search author name (e.g. "Nguyễn Minh Đức") → verify results found.
        (*Đăng nhập → tìm kiếm tên tác giả → kiểm tra có kết quả.*)

    Hints (*Gợi ý*):
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
        - Verify: page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]').count() > 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    login(page, test_config)

    # Nhập tên tác giả
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
    wait_for_flutter(page, text="Nguyễn Minh Đức")
    enable_flutter_semantics(page)

    # Kiểm tra có kết quả
    results = page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]')
    assert results.count() > 0, "Phải tìm thấy sách của Nguyễn Minh Đức"

    page.screenshot(path=f"{test_config['screenshot_dir']}/TC-07-search-author.png")