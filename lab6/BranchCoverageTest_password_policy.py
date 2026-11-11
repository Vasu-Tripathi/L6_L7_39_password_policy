"""Lab 6 - Branch coverage tests for password_policy.py.

Every decision (if / elif / for) is driven to BOTH its True and False outcome.
Run with:  coverage run --branch -m pytest BranchCoverageTest_password_policy.py
"""
import pytest
from password_policy import check_password, strength, suggest_fix


# ---------- check_password: length checks ----------
# if len(pw) < 8      -> True / False
# elif len(pw) > 64   -> True / False
@pytest.mark.parametrize("pw, expect_short, expect_long", [
    ("Ab1!", True, False),          # < 8          -> "too short"
    ("Abcdef1!", False, False),     # 8..64        -> neither
    ("A" * 8, False, False),        # boundary 8   -> neither
    ("Aa1!" * 16, False, False),    # boundary 64  -> neither
    ("Aa1!" * 16 + "x", False, True),  # 65        -> "too long"
])
def test_length_branches(pw, expect_short, expect_long):
    issues = check_password(pw)
    assert ("too short" in issues) == expect_short
    assert ("too long" in issues) == expect_long


# ---------- check_password: common-password check ----------
def test_common_true_case_insensitive():
    assert "common" in check_password("QWERTY")


def test_common_false():
    assert "common" not in check_password("Zx9!Zx9!")


# ---------- check_password: character loop ----------
def test_empty_password_loop_body_never_runs():
    # for-loop False branch on first check; every class missing
    assert check_password("") == [
        "too short", "no uppercase", "no lowercase", "no digit", "no special"
    ]


@pytest.mark.parametrize("pw, missing", [
    ("abcdef1!", "no uppercase"),
    ("ABCDEF1!", "no lowercase"),
    ("Abcdefg!", "no digit"),
    ("Abcdefg1", "no special"),
])
def test_each_missing_class_true_branch(pw, missing):
    assert check_password(pw) == [missing]


def test_all_classes_present_false_branches():
    assert check_password("Abcdef1!") == []


# ---------- strength ----------
@pytest.mark.parametrize("pw, expected", [
    ("Abcdefghijk1!x", "strong"),     # no issues, len >= 14
    ("Abcdefghijk1!", "good"),        # no issues, len == 13
    ("Abcdefg1", "weak"),             # 1 issue
    ("Abcdefgh", "weak"),             # 2 issues (boundary)
    ("abcdefgh", "very weak"),        # 3 issues
    ("", "very weak"),                # 5 issues
])
def test_strength_branches(pw, expected):
    assert strength(pw) == expected


# ---------- suggest_fix ----------
@pytest.mark.parametrize("issues, expected", [
    ([], "none needed"),
    (["too short", "no digit"], "add more characters"),
    (["common"], "avoid common passwords"),
    (["no uppercase"], "add uppercase"),
    (["no special"], "add special"),
    (["too long"], "shorten it"),     # falls through every if
])
def test_suggest_fix_branches(issues, expected):
    assert suggest_fix(issues) == expected


# ---------- integration: pipeline ----------
def test_check_then_suggest():
    assert suggest_fix(check_password("letmein")) == "add more characters"
