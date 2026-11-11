from hypothesis import given, strategies as st
from password_policy import first_character_type, split_credentials, digit_ratio


# ---------- first_character_type ----------
@given(st.text() | st.none())
def test_first_character_type_no_crash(s):
    try:
        first_character_type(s)
    except Exception as e:
        assert False, f"first_character_type crashed with: {e!r}"


@given(st.text(min_size=1))
def test_first_character_type_valid_output(s):
    assert first_character_type(s) in {"digit", "letter", "symbol"}


# ---------- split_credentials ----------
@given(st.text() | st.none())
def test_split_credentials_no_crash(s):
    try:
        split_credentials(s)
    except Exception as e:
        assert False, f"split_credentials crashed with: {e!r}"


@given(st.text(alphabet=st.characters(blacklist_characters=":"), min_size=1),
       st.text(min_size=1))
def test_split_credentials_keeps_colons_in_password(user, pw):
    # passwords may legitimately contain ':' -> only the first ':' separates
    u, p = split_credentials(f"{user}:{pw}")
    assert u == user.strip()
    assert p == pw.strip()


# ---------- digit_ratio ----------
@given(st.text() | st.none())
def test_digit_ratio_no_crash(s):
    try:
        digit_ratio(s)
    except Exception as e:
        assert False, f"digit_ratio crashed with: {e!r}"


@given(st.text())
def test_digit_ratio_in_range(s):
    r = digit_ratio(s)
    assert isinstance(r, float)
    assert 0.0 <= r <= 1.0
