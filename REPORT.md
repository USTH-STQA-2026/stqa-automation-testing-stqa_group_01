# REPORT: Web UI Automation Testing
---

## 1. Login Module
- **Module Tested**: Login Functionality (`tests/test_login.py`)
- **Tools**: Python + Playwright + pytest

### 1.1 How it works

- **Flutter Web Support**: Since Flutter renders the app on a canvas instead of normal HTML, we used `enable_flutter_semantics(page)` so Playwright can read the text fields and buttons.
- **Smart Waiting**: We used `wait_for_flutter(page, text="...")` to make the script wait for the exact moment an error message appears. This stops the test from rushing ahead and failing early.

### 1.2 Test Cases Summary

Every negative test checks two things: that the correct error message shows up, and that the user is safely kept on the login page (the app didn't crash or log them in by mistake).

| Test ID | Scenario | Description | Status |
| --- | --- | --- | --- |
| **TC-01** | Login Success | Logs in with valid email/password $\rightarrow$ sees `"Đăng xuất"`. | PASS |
| **TC-02** | Wrong Password | Logs in with bad password $\rightarrow$ sees `"Mật khẩu không đúng."`. | PASS |
| **TC-03** | Empty Fields | Clicks login with no inputs $\rightarrow$ sees `"Vui lòng nhập email và mật khẩu."`. | PASS |
| **TC-13** | User Not Found | Logs in with a fake email $\rightarrow$ sees `"Không tìm thấy thành viên."`. | PASS |

### 1.3 Test Evidence (Screenshots)

The automated screenshots for each result have been generated and saved into the project folder when running the script:

- `screenshots/login_success.png`
- `screenshots/login_fail_wrong_password.png`
- `screenshots/login_fail_empty_fields.png`
- `screenshots/login_fail_member_not_found.png`

---

## 2. Searching and Filtering books module