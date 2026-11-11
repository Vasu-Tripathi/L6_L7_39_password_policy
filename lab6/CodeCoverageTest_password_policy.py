"""Lab 6 - Code (line) coverage tests for password_policy.py.

Goal: every line of password_policy.py executes at least once.
"""
from password_policy import check_password, strength, suggest_fix


# ---------- check_password ----------
def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []


def test_too_short_password():
    assert "too short" in check_password("Ab1!")


def test_too_long_password():
    assert "too long" in check_password("Aa1!" * 20)  # 80 chars


def test_common_password():
    issues = check_password("password")
    assert "common" in issues


def test_all_character_classes_missing_reported():
    # only lowercase letters -> no uppercase, no digit, no special
    issues = check_password("abcdefgh")
    assert issues == ["no uppercase", "no digit", "no special"]


def test_no_lowercase():
    assert "no lowercase" in check_password("ABCDEFG1!")


# ---------- strength ----------
def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"


def test_long_valid_password_is_strong():
    assert strength("Abcdefghijk1!x") == "strong"  # 14 chars


def test_weak_password():
    assert strength("Abcdefgh") == "weak"  # no digit, no special


def test_very_weak_password():
    assert strength("abc") == "very weak"


# ---------- suggest_fix ----------
def test_suggest_none_needed():
    assert suggest_fix([]) == "none needed"


def test_suggest_too_short():
    assert suggest_fix(["too short"]) == "add more characters"


def test_suggest_common():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_suggest_missing_class():
    assert suggest_fix(["no digit"]) == "add digit"


def test_suggest_too_long():
    assert suggest_fix(["too long"]) == "shorten it"
