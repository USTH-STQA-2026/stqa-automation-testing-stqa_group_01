# REPORT: Web UI Automation Testing
---
**Tools**: Python + Playwright + pytest

## 1. Login Module
- **Module Tested**: Login Functionality (`tests/test_login.py`)

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
**Module Tested:** Search and Filter Functionality (`tests/test_search_filter.py`)

### 2.1 How it works

- **Flutter Web Support:** As with the login module, `enable_flutter_semantics(page)` is used so Playwright can read the search box, filter box, and book cards rendered on the Flutter canvas.
- **RIPR Model:** Each test case follows Reachability → Infection → Propagation → Revealability: log in to reach the book list, type a keyword to trigger the search/filter logic, wait for the UI to update, then assert the result is correct.
- **Smart Waiting:** `wait_for_flutter(page, selector=...)` or `wait_for_flutter(page, text=...)` ensures the test waits until the search results actually render before checking them, avoiding flaky false failures.
- **Reading Book Cards:** Each book card has `role="group"` and an `aria-label` containing its info (code, title, author, category), so results are verified by inspecting `aria-label` attributes of `flt-semantics` elements.

### 2.2 Test Cases Summary

| Test ID | Scenario | Description | Status |
|---|---|---|---|
| TC-04 | Search by Book Name | Enters "Flutter" in the search box → at least one book card with "Flutter" in its `aria-label` is displayed, and the "Không tìm thấy sách" (no results) message does not appear. | PASS |
| TC-05 | Search with No Result | Enters "Tiểu thuyết" (a keyword not in the seed data) → the system displays the "Không tìm thấy sách" message and no book cards are shown. | PASS |

### 2.3 Test Evidence (Screenshots)

The automated screenshots for each result have been generated and saved into the project folder when running the script:

- `screenshots/TC-04_search_by_name.png`
- `screenshots/TC-05_search_no_result.png`

---


## 4. General Function Testing
- **Module Tested**: Logout function and Language changing (`tests/test_general.py`)
- **Tools**: Python + Playwright + pytest

### 4.1 How it works

- **UI Synchronization**: Since Flutter re-renders dynamically, using `enable_flutter_semantics(page)` after actions (logout/switch language) is compulsory. It refresh Semantics Tree so Playwright can see the updated elements, combined with implicit/explicit waits to ensure UI stability before assertions.
- **Smart Waiting**: By using `flt-semantics[role="button"]:has-text("...")`, the tests locate elements by their visible text, which makes the script reliable and resistant to internal DOM structural changes.
- **Validation Logic**: Logout used multi-point validation (for both Login button and Email input) to guarantee a complete return to the initial state. Language Change used a partial keyword match (any()) to verify the transition to English, so the test stays reliable even if only parts of the UI change.

### 4.2 Test Cases Summary

Every positive test ensures the UI transitions to the expected state and the displayed content is updated correctly without errors.

| Test ID | Scenario | Description | Status |
| --- | --- | --- | --- |
| **TC-11** | Logout Success | Afer logging in, Logs out with dedicated button on the website. | PASS |
| **TC-12** | Switch Language | Change language from Vietnamese to English with EN button | PASS |

### 4.3 Test Evidence (Screenshots)

The automated screenshots for each result have been generated and saved into the project folder when running the script:

- `screenshots/logout_success.png`
- `screenshots/language_en.png`

---
