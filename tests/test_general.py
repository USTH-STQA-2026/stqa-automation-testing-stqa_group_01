"""
Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - Logout button: 'flt-semantics[role="button"]:has-text("Đăng xuất")'
      (*Nút Đăng xuất*)
    - Language switch EN button: 'flt-semantics[role="button"]:has-text("EN")'
      (*Nút chuyển ngôn ngữ EN*)
    - After logout: page returns to login (has "Đăng nhập" button and "Email" input)
      (*Sau đăng xuất: trang quay về login*)
    - After switching to EN: text "Logout", "Borrow", "Search", "Library" may appear
      (*Sau chuyển EN: text tiếng Anh có thể xuất hiện*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR,
)


def test_logout(page, test_config):
    """TC-11: Logout success (*Đăng xuất thành công*)
    Description (*Mô tả*):
        Log in → click Logout → verify page returns to login screen.
        (*Đăng nhập → click Đăng xuất → kiểm tra quay về trang đăng nhập.*)

    Suggested steps (*Gợi ý*):
        1. login(page, test_config)
        2. Find "Đăng xuất" button and click (*Tìm nút "Đăng xuất" và click*)
        3. Wait 3s, re-enable semantics (*Đợi 3s, bật lại semantics*)
        4. Assert: "Đăng nhập" button or Email input exists
           (*Assert: có nút "Đăng nhập" hoặc ô input Email*)
    """
    # login
    login(page, test_config)
    # find logout button and click
    logout_btn= 'flt-semantics[role="button"]:has-text("Đăng xuất")'
    page.locator(logout_btn).click()
    
    # wait and re-enable semantic
    time.sleep(3)
    enable_flutter_semantics(page)
    
    # verify/Assert
    login_btn='flt-semantics[role="button"]:has-text("Đăng nhập")'
    email_input='input[aria-label="Email"]'
    is_login_page=page.locator(login_btn).is_visible() or page.locator(email_input).is_visible()
    
    assert is_login_page, "Fault: Did not return to login page."
    
    # save screenshot
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "logout_success.png"))


def test_switch_language_to_english(page, test_config):
    """TC-12: Switch language to English (*Chuyển ngôn ngữ sang tiếng Anh*)

    Description (*Mô tả*):
        Log in → click "EN" button → verify UI switches to English.
        (*Đăng nhập → click nút "EN" → kiểm tra giao diện chuyển sang tiếng Anh.*)

    Suggested steps (*Gợi ý*):
        1. login(page, test_config)
        2. Find "EN" button and click (*Tìm nút "EN" và click*)
        3. Wait 2s, re-enable semantics (*Đợi 2s, bật lại semantics*)
        4. Get sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
        5. Assert: "Logout" or "Borrow" or "Library" in sem_text
    """
    # login
    login(page, test_config)
    
    # find "EN" and click
    btn_en = 'flt-semantics[role="button"]:has-text("EN")'
    page.locator(btn_en).click()
    
    # wait 2s and re-enable semantic
    time.sleep(2)
    enable_flutter_semantics(page)
    
    # get text content on screen
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    
    # checks if there are any English words
    found_en = any(word in sem_text for word in ["Logout", "Borrow", "Search", "Library"])
    
    assert found_en, "Error: Language has not been changed to English!"
    
    # save screenshot
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "language_en.png"))
