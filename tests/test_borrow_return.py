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


def test_borrow_book(page, test_config): # made by Nguyễn Xuân Dương
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
    # Find all available books, then click the first available
    buttons = page.get_by_role("button", name="Mượn sách này")
    if buttons.count() > 0:
        buttons.first.click()
    else:
        assert buttons.count() > 0, "No books to borrow"
    # After clicking the borrow button, a confirmation window appears, we need to confirm borrowing
    wait_for_flutter(page,"Xác nhận mượn sách")
    flutter_click_button(page,"Mượn")
    
    # [P] Propagation: Wait for the system to process the request
    # We are expecting an anouncement for successfully borrowing a book
    wait_for_flutter(page,"Mượn sách thành công")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "after_borrow.png"))

    # [R] Revealability: Test oracle checks if the book has been successfully borrowed
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "thành công" in sem_text, \
        "Borrow book wasn't successful"

    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_view_borrowed_books(page, test_config): #made by Vũ Trần Nam Khánh
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

    # [R] Reachability: Access the website
    login(page,test_config)
    
    # [I] Infection: Switch tab
    # Click on the tab which contains borrowed books
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()

    # [P] Propagation: View borrowed books
    wait_for_flutter(page, "Phiếu mượn của tôi")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "view_borrowed_books.png"))
    
    # [R] Revealability: Test oracle checks if the borrowed books can be view
    # use .content() to also include the html contents
    sem_text = "".join(page.content())
    assert "Đang mượn" in sem_text, \
       "Fault : No display of 'Đang mượn'!"
    assert "Trả sách" in sem_text, \
        "Fault : No display of 'Trả sách'!"
    assert "Đã trả" in sem_text, \
        "Fault : No display of 'Đã trả'" 

    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_return_book(page, test_config): # made by Nguyễn Xuân Dương
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
    login(page, test_config)

    # [I] Infection: Return a book
    # Click on the tab which contains borrowed books
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    wait_for_flutter(page, text="Phiếu mượn của tôi")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "before_return.png"))
    # Return a book
    flutter_click_button(page, "Trả sách")

    # [P] Propagation: Wait for the system to process the request
    wait_for_flutter(page, "Trả sách thành công")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "after_return.png"))

    # [R] Revealability: Test oracle checks if the book has been returned
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "thành công" in sem_text, \
        "Return book wasn't successful"

    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_book_limit(page, test_config): # made by Vũ Trần Nam Khánh
    """TC-11: Checking borrowing limit
    
    Description:

    """
    # [R] Reachability: Access the website
    # Login as MEM003 due to no borrowed books in this account 
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "dam.tran@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")

    # [I] Infection: Borrow 4 books
    '''
    The idea for this for-loop is simple. The borrow book 1, 2 and 3 will always be success (and that it will pass the `if i < 4`)
    For the fourth borrow, it will go to the `else`. The sem_text will check whether if the "Đã đạt giới hạn mượn tối đa" is displayed or not.
    '''
    for i in range(1, 5, 1):
        buttons = page.get_by_role("button", name="Mượn sách này")
        if buttons.count() > 0:
            buttons.first.click()
        else:
            assert buttons.count() > 0, "No books to borrow"
        wait_for_flutter(page,"Xác nhận mượn sách")
        flutter_click_button(page,"Mượn")

        # [P] Propagation: Check if the fourth book triggers the error message
        wait_for_flutter(page, "Mượn sách thành công")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"borrow_number_{i}.png")) 

        if i < 4:
            # Scroll the page down to borrow books
            page.wait_for_timeout(3800)
            page.mouse.wheel(0, 30)
            page.wait_for_timeout(1000)
        else:
            # [R] Revealability: Test oracle checks if the limit has been reached
            sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
            assert "Đã đạt giới hạn mượn tối đa" in sem_text, \
                "Fault : The book limit counting is false. It should be < 3"
            # Due to the bug that a member can borrow up to 4 books instead of 3 books in the system, this TC will always fail.

    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_borrow_permission_expired(page, test_config): # made by Nguyễn Xuân Dương
    """TC-12: Testing the borrow permission of an expired account
    
    Description:

    """
    # [R] Reachability: Access the website
    # Login as the expired account MEM005
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "binh.pham@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")

    # [I] Infection: Try borrowing an available book
    buttons = page.get_by_role("button", name="Mượn sách này")
    if buttons.count() > 0:
        buttons.first.click()
    else:
        assert buttons.count() > 0, "No books to borrow"
    wait_for_flutter(page,"Xác nhận mượn sách")
    flutter_click_button(page,"Mượn")

    # [P] Propagation: Wait for the system to process the request
    # We are expecting an error
    wait_for_flutter(page, "Không thể mượn sách")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrow_from_expired_acc.png"))
    
    # [R] Revealability: Test oracle checks if the expired account can borrow a book or if the error message is correct
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "hết hạn" in sem_text, \
        f"No announcement or incorrect announcement"

    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_borrow_permission_suspended(page, test_config): # made by Nguyễn Xuân Dương
    """TC-13: Testing the borrow permission of an expired account
    
    Description:

    """
    # [R] Reachability: Access the website
    # Login as the suspended account MEM004
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "cu.le@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")

    # [I] Infection: Try borrowing an available book
    buttons = page.get_by_role("button", name="Mượn sách này")
    if buttons.count() > 0:
        buttons.first.click()
    else:
        assert buttons.count() > 0, "No books to borrow"
    wait_for_flutter(page,"Xác nhận mượn sách")
    flutter_click_button(page,"Mượn")

    # [P] Propagation: Wait for the system to process the request
    # We are expecting an error
    wait_for_flutter(page, "Không thể mượn sách")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrow_from_suspended_acc.png"))
    
    # [R] Revealability: Test oracle checks if the suspended account can borrow a book or if the error message is correct
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "tạm ngưng" in sem_text, \
        f"No announcement or incorrect announcement"

    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_librarian_view_borrow_overdue(page,test_config): # made by Vũ Trần Nam Khánh
    """TC-14: Testing librarian's check overdue function

    Description:
    Since for librarian account, it possess some additional functions / features that a regular account cannot.

    One particular goal is to check inside the "Mượn / Trả" where the librarian could press on the "Kiểm tra sách quá hạn"
    to see borrowed books are overdue or not.
    """
    # [R] Reachability: Access the website
    # Login as the librarian account
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "librarian@library.com")
    flutter_fill(page, "Mật khẩu", "admin123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")   

    # [I] Infection: Clicking the check overdue button
    # We switch into the tab "Mượn / Trả"
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    wait_for_flutter(page, text="Kiểm tra sách quá hạn")
    # Click on the button that shows "Kiểm tra sách quá hạn"
    flutter_click_button(page, "Kiểm tra sách quá hạn")

    # [P] Propagation: Wait for the system to process the request
    # Wait for the flutter renders completely
    page.wait_for_timeout(1000)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "librarian_view_borrow_overdue.png"))

    # [R] Revealability: Test oracle checks if the borrowed books which are overdue change states
    # Use .content() to also include the html contents
    # If we use all_text_contents() then it will ignore the "Quá hạn"
    sem_text = "".join(page.content()) 
    assert "Kiểm thử phần mềm nhập môn" in sem_text, \
        "Fault: Target book card disappeared from the list"
    assert "Quá hạn" in sem_text, \
        "Fault: The 'Quá hạn' status badge failed to generate after running the date check"    

    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")
