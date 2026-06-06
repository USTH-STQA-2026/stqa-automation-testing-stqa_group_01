"""
Borrow & Return Tests (*Kiểm thử Mượn & Trả sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 3 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 3 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - "Mượn / Trả" tab: role="tab", aria-label="Mượn / Trả"
    - Available books have "Có sẵn" in aria-label, borrowed books have "Đang mượn"
      (*Sách "Có sẵn" có aria-label chứa "Có sẵn", sách "Đang mượn" chứa "Đang mượn"*)
    - Borrow button: 'flt-semantics[role="button"]:has-text("Mượn sách này")'
      (*Nút mượn*)
    - After clicking "Mượn sách này", a confirmation dialog appears — click "Mượn" again
      (*Sau khi click "Mượn sách này" sẽ hiện dialog xác nhận — cần click nút "Mượn" lần nữa*)
    - Return button: 'flt-semantics[role="button"]:has-text("Trả sách")'
      (*Nút trả*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR, wait_for_flutter
)


def test_borrow_book(page, test_config):
    """TC-08: Borrow an available book (*Mượn sách có trạng thái 'Có sẵn'*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → find an "Available" book → click "Mượn sách này" → confirm dialog
        → verify book status changes to "Borrowed".
        (*Đăng nhập → tìm sách "Có sẵn" → click "Mượn sách này" → xác nhận dialog
        → kiểm tra sách chuyển sang trạng thái "Đang mượn".*)

    Suggested steps (*Gợi ý các bước*):
        1. login(page, test_config)
        2. Find available book: page.locator('flt-semantics[role="group"][aria-label*="Có sẵn"]')
           (*Tìm sách Có sẵn*)
        3. Click "Mượn sách này" button inside that book card
           (*Click nút "Mượn sách này" trong sách đó*)
        4. Wait for confirmation dialog, re-enable semantics
           (*Đợi dialog xác nhận, bật lại semantics*)
        5. Click "Mượn" button (confirm button in dialog)
           (*Click nút "Mượn" — nút xác nhận trong dialog*)
        6. Assert: "Đang mượn" or "thành công" appears
           (*Assert: "Đang mượn" hoặc "thành công" xuất hiện*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)  

    # [R] Reachability: Access the website
    login(page, test_config)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "before_borrow.png"))

    # [I] Infection: Borrow a book
    buttons = page.get_by_role("button", name="Mượn sách này")
    if buttons.count()>0:
        buttons.first.click()
    else:
        assert buttons.count() > 0, "No books to borrow"
    
    wait_for_flutter(page,"Xác nhận mượn sách")
    flutter_click_button(page,"Mượn")
    
    # [P] Propagation: Wait for the system to process the request
    wait_for_flutter(page,"Mượn sách thành công")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "after_borrow.png"))

    # [R] Revealability: Test oracle check if the book has changed state
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "thành công" in sem_text, \
        f"Borrow book wasn't successful"

    # pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_view_borrowed_books(page, test_config):
    """TC-09: View borrowed books list (*Xem danh sách sách đang mượn — tab Mượn / Trả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → switch to "Mượn / Trả" tab → verify borrowed books are shown.
        (*Đăng nhập → chuyển sang tab "Mượn / Trả" → kiểm tra có sách đang mượn.*)

    Hints (*Gợi ý*):
        - Click tab: page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
        - Verify: books with "Đang mượn" in aria-label, or "Trả sách" button exists
          (*Kiểm tra: có sách với aria-label chứa "Đang mượn" hoặc có nút "Trả sách"*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)

    # [R] Reachability : Access to the web
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    # [I] Infection: Enter correct data (here is entering correct data to login)
    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    # [P] Propagation : Test the view borrowed books 
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').first.click()
    enable_flutter_semantics(page)
    wait_for_flutter(page, text="Phiếu mượn của tôi")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "view_borrowed.png"))
    
    sem_text = page.content()
    
    #[role='group'][aria-label*='Kiểm thử phần mềm nhập môn'][aria-label*='Trả sách']
    # assert "Đang mượn" in sem_text or "Trả sách" in sem_text, \
    #     "Fault : Error with the display for borrowed book"
    assert "Đang mượn" in sem_text, \
       "Fault : No display of 'Đang mượn'!"
    assert "Trả sách" in sem_text, \
        "Fault : No display of 'Trả sách'!"
    assert "Đã trả" in sem_text, \
        "Fault : No display of 'Đã trả'" 

    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_return_book(page, test_config):
    """TC-10: Return a borrowed book (*Trả sách đang mượn*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → go to "Mượn / Trả" tab → click "Trả sách" → verify book is returned.
        (*Đăng nhập → tab "Mượn / Trả" → click "Trả sách" → kiểm tra sách được trả.*)

    Hints (*Gợi ý*):
        - Switch to "Mượn / Trả" tab (*Chuyển tab "Mượn / Trả"*)
        - Find return button: page.locator('flt-semantics[role="button"]:has-text("Trả sách")')
          (*Tìm nút "Trả sách"*)
        - Click and verify status change or success message
          (*Click và kiểm tra sách chuyển trạng thái hoặc có thông báo thành công*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)

    # [R] Reachability: Access the website
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "ba.nguyen@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
 
    tab=page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
    tab.click()

    # [I] Infection: Return a book
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "before_return.png"))
    flutter_click_button(page,"Trả sách")

    # [P] Propagation: Wait for the system to process the request
    wait_for_flutter(page,"Trả sách thành công")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "after_return.png"))
    
    # [R] Revealability: Test oracle check if the borrowing slip has changed state
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "thành công" in sem_text, \
        f"Return book wasn't successful"

    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")

def test_book_limit(page, test_config):

    pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")

def test_borrow_permission_expired(page, test_config):

    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "binh.pham@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    page.wait_for_timeout(2000)
    buttons = page.get_by_role("button", name="Mượn sách này")
    if buttons.count()>0:
        buttons.first.click()
    else:
        assert buttons.count() > 0, "No books to borrow"
    wait_for_flutter(page,"Xác nhận mượn sách")
    flutter_click_button(page,"Mượn")
    
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Thành viên đã hết hạn" in sem_text, \
        f"No announcement or incorrect announcement"

    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")
